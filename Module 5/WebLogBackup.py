# Simple Apache Airflow pipeline with bash operators to ETL IP logs from the web server.
# These logs are archived in weblog.tar, which serves as a backup.

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
from datetime import timedelta

default_args = {
    'owner': 'Name',
    'start_date': days_ago(0),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'process_web_log',
    default_args=default_args,
    description='ETL the server IP logs to tar',
    schedule_interval=timedelta(days=1))

extract_data = BashOperator(
    task_id = "extract_data",
    bash_command= 'cut /home/project/airflow/dags/proj/accesslog.txt -d " " -f1 > /home/project/airflow/dags/proj/extracted_data.txt',
    dag=dag,
)

transform_data = BashOperator(
    task_id = "transform_data",
    bash_command= 'cat /home/project/airflow/dags/proj/extracted_data.txt | grep -v 198.46.149.143 > /home/project/airflow/dags/proj/transformed_data.txt',
    dag=dag,
)

load_data = BashOperator(
    task_id = "load_data",
    bash_command= 'tar -cf weblog.tar /home/project/airflow/dags/proj/transformed_data.txt',
    dag=dag,
)

extract_data >> transform_data >> load_data
