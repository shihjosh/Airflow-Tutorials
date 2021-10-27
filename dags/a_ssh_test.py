import base64
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.contrib.operators.sftp_operator import SFTPOperator
from airflow.contrib.operators.ssh_operator import SSHOperator
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.operators.dummy_operator import DummyOperator

'''
SSH 遠端連線
取得資訊
Python3 解碼 base64
'''


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2021, 10, 27),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def _decode_message(task_name, ti):
    message = ti.xcom_pull(task_name)
    print(message)
    return base64.b64decode(message).decode()

# ssh test
with DAG('a_ssh_test', default_args=default_args,schedule_interval='15 1 * * *') as dag:
    
    myhook = SSHHook(
        remote_host='192.168.172.194',
        username='sv',
        password='sv28991410)(*',
        port='22',
    )

    my_flow = SSHOperator(
        task_id="my_flow",
        ssh_hook=myhook,
        command='kubectl top pod'
    )

    decode = PythonOperator(
        task_id='decode',
        python_callable=_decode_message,
        op_args=[
            'my_flow',
        ],
    )

    do_nothing = DummyOperator(task_id='do_nothing')

    my_flow >> decode >> do_nothing

