from airflow import DAG
from airflow.operators.python_operator import PythonOperator

from datetime import datetime, timedelta
from scripts.processing import _extract_data, _upload_to_s3  

default_args = {
    'owner':'Pedrosa'
}

with DAG(
    "etl-twitter",
    start_date=datetime(2023,1,15),
    schedule_interval=timedelta(minutes=10),
    default_args=default_args,
    catchup=False
) as dag:
    extract_data = PythonOperator(
        task_id="extract_data",
        python_callable=_extract_data
    )

    upload_to_s3 = PythonOperator(
        task_id="upload_to_s3",
        python_callable=_upload_to_s3,
        op_args=['/opt/airflow/dags/data/tweets.csv', 'datalake-pedrosa-524095156763', 'staging/tweets.csv']
    )

    extract_data >> upload_to_s3