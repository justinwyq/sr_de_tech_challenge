from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from section1 import pipeline

default_args = {
    "owner": "your_name",
    "depends_on_past": False,
    "start_date": datetime(2023, 2, 18),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "process_membership_applications",
    default_args=default_args,
    description="DAG for processing membership applications",
    schedule_interval="0 0 * * *",
)

process_applications_task = PythonOperator(
    task_id="pipeline",
    python_callable=pipeline,
    dag=dag,
)

process_applications_task