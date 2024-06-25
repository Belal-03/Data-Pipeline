#!/bin/bash
source /home/belal/airflow_env_pandas_2.1/bin/activate
python3 /home/belal/airflow/scripts/mysql_to_airflow.py
deactivate
