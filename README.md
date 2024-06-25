# Data-Pipeline
Worked With My Friend To Build a Data Pipeline and Workflow Operations



Requirements:
Objective: This assignment aims to provide hands-on experience in developing a robust Extract,
Transform, Load (ETL) pipeline using Apache Airflow. You will work with the Steam Store API
to gather batch data, preprocess it, and integrate it into a scheduled workflow using Airflow.
Additionally, you will create a Bash script to perform a data preprocessing task.
Dataset:
For this assignment, you will use the Steam Store API to gather data about games. The data will
be in JSON format and will include various attributes like game titles, prices, release dates, and
more. Please read the documentation of how to use Storm API : https://nikdavis.github.io/posts/2019/steam-data-collection/
Operations (Tasks):

Task 1: ETL Implementation
1. Data Extraction:
 Write a Python script to fetch batch data from the Steam Store API. This script will
gather the data in batches to ensure efficient data retrieval.
2. Data Preprocessing
 Create a Bash script to perform at least one data preprocessing task and then
integrate this script into your Apache Airflow DAG using the BashOperator
3. Data Transformation:
 Write a Python script for cleaning, filtering, and transforming the dataset. Apply
a minimum of three tasks related to cleaning and transforming the data.
4. Data Loading:
 Write a Python script to load the transformed data into a MySQL database on
localhost. Please make sure that the data is integrated with the loaded data.

Task 2: Building Data Pipeline with Apache Airflow
Objective: Integrate the ETL process into an Apache Airflow DAG for scheduled execution.
1. Apache Airflow DAG Setup:
 Establish an Apache Airflow DAG named 'Stream_pipeline'
 Define the DAG's start date, schedule interval (set to run hourly), and other
necessary configurations.
2. Task Definitions:
 Create individual PythonOperator tasks within the DAG for each ETL subtask
(data extraction, transformation and data loading). Also, a BashOperator for the
data preprocessing task
 Set up dependencies between tasks based on their execution order.
3. Monitoring and Error Handling:
 Implement monitoring mechanisms within the Apache Airflow DAG for tracking
performance.
 Establish effective error-handling strategies to handle potential issues during
execution.
4. Workflow orchestration :
 Execute the DAG to verify that both the PythonOperators and the BashOperator
are performed correctly.

Submission:
 Submit your Python scripts for data extraction, transformation, and loading.
 Submit your Apache Airflow DAG definition.
 Submit your Bash script for data preprocessing.
 Ensure your scripts are well-documented and include comments explaining each step.

Evaluation Criteria:
 Correctness and efficiency of the ETL pipeline.
 Proper integration and scheduling using Apache Airflow.
 Effective use of Bash scripting for preprocessing.
 Quality of documentation and code readability.
 Handling of errors and implementation of monitoring mechanisms.
