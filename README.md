# 🔁 Data Pipeline with Apache Airflow – Steam Store ETL Project

This project demonstrates how to build a complete data pipeline using Apache Airflow. It focuses on extracting batch data from the Steam Store API, transforming and preprocessing the data using Python and Bash scripts, and loading it into a MySQL database. The ETL pipeline is integrated into an Apache Airflow DAG for automated and scheduled execution.

---

## 🎯 Project Objective

- Build a robust Extract, Transform, Load (ETL) pipeline using Apache Airflow.
- Extract real-world data from the **Steam Store API** in batch format.
- Perform **Bash-based preprocessing** and **Python-based transformations**.
- Load the processed data into a **MySQL** database.
- Automate and schedule the workflow using **Apache Airflow DAGs**.

---

## 🗃️ Dataset Overview

- Source: [Steam Store API](https://nikdavis.github.io/posts/2019/steam-data-collection/)
- Format: JSON
- Data Includes:
  - Game titles
  - Prices
  - Release dates
  - User reviews
  - Additional metadata

---

## 🧩 Task Breakdown

### ⚙️ Task 1: ETL Pipeline Development

#### 🟠 1. Data Extraction
- Develop a Python script to fetch **batch data** from the Steam Store API.
- Ensure efficient data retrieval by using batch or paginated requests.

#### 🟠 2. Data Preprocessing
- Write a **Bash script** that performs at least one data cleaning or formatting task.
- Example: Removing nulls, renaming files, adjusting encoding.
- Integrate this script using **Airflow's BashOperator**.

#### 🟠 3. Data Transformation
- Create a Python script to:
  - Clean and filter records
  - Normalize and reformat fields
  - Apply at least **three transformation tasks**
- Prepare data for database loading.

#### 🟠 4. Data Loading
- Write a Python script to load the transformed data into a **MySQL** database.
- Ensure schema compatibility and data integrity with existing records.

---

### 🛠️ Task 2: Workflow Orchestration with Apache Airflow

#### 🗂️ DAG Setup
- Create an **Apache Airflow DAG** named `steam_pipeline`.
- Configure:
  - `start_date`
  - `schedule_interval` (set to hourly)
  - `catchup`, `retries`, and DAG-level defaults

#### 🧱 Task Definitions
- Define each ETL step as a separate task:
  - `PythonOperator` for **Extraction**, **Transformation**, and **Loading**
  - `BashOperator` for **Preprocessing**
- Establish proper **task dependencies** to maintain execution order.

#### 📈 Monitoring and Error Handling
- Implement monitoring logs for task success/failure tracking.
- Add retry mechanisms and exception handling within each script and DAG.

#### ▶️ DAG Execution
- Trigger the DAG manually or wait for scheduled runs.
- Ensure all operators execute as expected and data flows correctly through the pipeline.

---

## 📦 Deliverables

- ✅ Python script for **data extraction**
- ✅ Bash script for **data preprocessing**
- ✅ Python script for **data transformation**
- ✅ Python script for **data loading**
- ✅ Complete Airflow DAG (`steam_pipeline.py`)
- ✅ Documentation and comments for each script

---

## 🧠 Key Tools & Technologies

| Tool              | Purpose                                  |
|-------------------|------------------------------------------|
| Apache Airflow    | Workflow orchestration and scheduling    |
| Steam Store API   | Real-world data source (JSON format)     |
| Python            | Data extraction, transformation, loading |
| Bash              | Preprocessing automation                 |
| MySQL             | Database for storing structured data     |

---

## 📊 Evaluation Criteria

- ✅ Functional and efficient ETL pipeline
- ✅ Proper integration with Apache Airflow DAG
- ✅ Use of Bash scripting in a real-world context
- ✅ Code clarity and well-documented scripts
- ✅ Monitoring, logging, and error-handling mechanisms
