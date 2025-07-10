from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="healthcare_pipeline",
    start_date=datetime(2024,1,1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    ingest = BashOperator(
        task_id="fetch_data",
        bash_command="python ingestion/fetch_healthcare_data.py"
    )

    transform = BashOperator(
        task_id="transform_data",
        bash_command="python processing/spark_transform.py"
    )

    load = BashOperator(
        task_id="load_data",
        bash_command="python warehouse/load_to_postgres.py"
    )

    ingest >> transform >> load