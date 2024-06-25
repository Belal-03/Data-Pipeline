import pandas as pd
from sqlalchemy import create_engine
import mysql.connector
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    mysql_host = 'localhost'
    mysql_user = 'belal_khaled'
    mysql_password = 'Bkshbm1234#_'
    mysql_db = 'games'
    table_name = 'steam_games'
    airflow_db_connection_string = 'postgresql+psycopg2://airflow:Bkshbm1234#_@localhost/airflow'
    airflow_table_name = 'steam_games'

    try:
        logging.info("Connecting to MySQL database")
        mysql_conn = mysql.connector.connect(host=mysql_host, user=mysql_user, password=mysql_password, database=mysql_db)
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql(query, mysql_conn)
        logging.info(f"Loaded {len(df)} records from MySQL table {table_name}")
    except Exception as e:
        logging.error(f"MySQL operation failed: {e}")
        return
    finally:
        if mysql_conn.is_connected():
            mysql_conn.close()
            logging.info("MySQL connection closed")

    try:
        logging.info("Connecting to Airflow PostgreSQL database")
        airflow_engine = create_engine(airflow_db_connection_string)
        logging.info("Engine created successfully")

        # Transferring data
        df.to_sql(airflow_table_name, airflow_engine, if_exists='replace', index=False)
        logging.info("Data transfer to Airflow PostgreSQL completed successfully")
    except Exception as e:
        logging.error(f"PostgreSQL operation failed: {e}")

if __name__ == "__main__":
    main()


