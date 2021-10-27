from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.sftp_operator import SFTPOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.contrib.hooks.ssh_hook import SSHHook

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2019, 10, 8),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG('a_ssh_test', default_args=default_args, schedule_interval=timedelta(days=1))

# 定義 SSHHook 存要連線主機的資訊
myhook = SSHHook(
    remote_host='192.168.172.193',
    username='sv',
    password='sv28991410)(*',
    port='22',
)

my_flow = SSHOperator(
    task_id="my_flow",
    ssh_hook=myhook,
    command='ls',
    dag=dag
)

my_flow