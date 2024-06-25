from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime, timedelta
import sys
import logging

# My path to the scripts 
sys.path.append('/home/belal/airflow/scripts/')

# Import my scripts
import data_transformation
import data_loading
import view_data  

# Configure logging
logging.basicConfig(level=logging.INFO, filename='/home/belal/airflow/logs/etl_pipeline.log', filemode='a', format='%(name)s - %(levelname)s - %(message)s')

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 5, 27),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='A simple ETL pipeline',
    schedule_interval=timedelta(days=1),
    concurrency=8,  # Setting concurrency to allow multiple tasks to run in parallel
    max_active_runs=1,  
)

def get_start_index():
    start_index = Variable.get("start_index", default_var=0)
    logging.info(f"Retrieved start index: {start_index}")
    return int(start_index)

def update_start_index(**kwargs):
    ti = kwargs['ti']
    start_index = ti.xcom_pull(task_ids='get_start_index_task')
    logging.info(f"Start index from XCom: {start_index}")
    with open("/home/belal/airflow/scripts/processed_count.txt", "r") as f:
        processed_count = int(f.read().strip())
        logging.info(f"Processed count read from file: {processed_count}")
    next_start_index = start_index + processed_count
    Variable.set("last_processed_index", start_index)
    Variable.set("start_index", next_start_index)
    logging.info(f"Updated start index to {next_start_index}")
    logging.info(f"Updated last processed index to {start_index}")

fetch_game_ids_task = BashOperator(
    task_id='fetch_game_ids',
    bash_command='python3 /home/belal/airflow/scripts/fetch_all_game_ids.py',
    dag=dag,
)

get_start_index_task = PythonOperator(
    task_id='get_start_index_task',
    python_callable=get_start_index,
    dag=dag,
)

extract_game_data_task = BashOperator(
    task_id='extract_game_data',
    bash_command='python3 /home/belal/airflow/scripts/extract_game_data.py {{ task_instance.xcom_pull(task_ids="get_start_index_task") }}',
    dag=dag,
)

update_start_index_task = PythonOperator(
    task_id='update_start_index',
    python_callable=update_start_index,
    provide_context=True,
    dag=dag,
)

def transform():
    try:
        logging.info("Starting data transformation")
        data_transformation.main()
        logging.info("Data transformation completed successfully")
    except Exception as e:
        logging.error(f"Data transformation failed: {e}")
        raise

def load():
    try:
        logging.info("Starting data loading")
        data_loading.main()
        logging.info("Data loading completed successfully")
    except Exception as e:
        logging.error(f"Data loading failed: {e}")
        raise

def view_data_task():
    try:
        logging.info("Viewing data from PostgreSQL")
        view_data.view_data()
        logging.info("Data viewing completed successfully")
    except Exception as e:
        logging.error(f"Data viewing failed: {e}")
        raise

preprocess_task = BashOperator(
    task_id='preprocess',
    bash_command='bash /home/belal/airflow/scripts/preprocess.sh ',
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    dag=dag,
)

transfer_task = BashOperator(
    task_id='transfer',
    bash_command='bash /home/belal/airflow/scripts/run_mysql_to_airflow.sh ',
    dag=dag,
)

view_data_operator = PythonOperator(
    task_id='view_data',
    python_callable=view_data_task,
    dag=dag,
)

# Task dependencies
fetch_game_ids_task >> get_start_index_task >> extract_game_data_task >> update_start_index_task >> preprocess_task >> transform_task >> load_task >> transfer_task >> view_data_operator







