# Healthcare Data Lakehouse Pipeline

End-to-end Data Engineering project that builds a modern healthcare data pipeline using open healthcare datasets.

This project demonstrates real-world data engineering workflows including data ingestion, distributed data processing, orchestration, and analytics.

The pipeline ingests public healthcare datasets, processes them using PySpark, stores them in a data warehouse, and visualizes insights through an analytics dashboard.

---

## Architecture

Public Healthcare API  
        ↓  
Python Data Ingestion  
        ↓  
Raw Data Storage (Data Lake)  
        ↓  
PySpark Data Processing  
        ↓  
PostgreSQL Data Warehouse  
        ↓  
Apache Airflow Orchestration  
        ↓  
Metabase Analytics Dashboard

---

## Tech Stack

Python  
PySpark  
PostgreSQL  
Apache Airflow  
Docker  
GitHub Actions  
Metabase  

---

## Project Structure


healthcare-data-lakehouse
│
├── ingestion
│ └── fetch_healthcare_data.py
│
├── processing
│ └── spark_transform.py
│
├── warehouse
│ └── load_to_postgres.py
│
├── airflow
│ └── healthcare_dag.py
│
├── docker
│ └── docker-compose.yml
│
├── data
│ ├── raw
│ └── processed
│
├── .github
│ └── workflows
│ └── pipeline.yml
│
├── requirements.txt
└── README.md


---

## Data Pipeline Workflow

1. Fetch healthcare dataset from public API
2. Store raw dataset in the data lake
3. Transform dataset using PySpark
4. Load processed data into PostgreSQL warehouse
5. Schedule the pipeline using Apache Airflow
6. Visualize insights using Metabase

---

## Setup Instructions

### Clone Repository


git clone https://github.com/pvsk13/healthcare-data-lakehouse.git

cd healthcare-data-lakehouse


---

### Install Dependencies


pip install -r requirements.txt


---

### Start Services


docker-compose up


This will start:

PostgreSQL database  
Apache Airflow scheduler

---

### Run Data Pipeline

Run ingestion


python ingestion/fetch_healthcare_data.py


Run transformation


python processing/spark_transform.py


Load to warehouse


python warehouse/load_to_postgres.py


---

## Example Analytics

Hospital distribution by state

Emergency services availability

Hospital type distribution

---

## Future Improvements

Add Kafka streaming ingestion  
Implement data quality checks  
Add dbt transformations  
Deploy on AWS data lake  

---

## Author

Venkata Sai Krishna  
Data Engineer | Cloud | Distributed Data Systems