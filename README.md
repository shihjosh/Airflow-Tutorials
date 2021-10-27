# Airflow-Tutorial
https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html

OS:Ubuntu

升級Docker-Compose到v1.29以上才能用

```bash

#創建必要的資料夾
mkdir -p ./dags ./logs ./plugins

#創建設定檔
echo -e "AIRFLOW_UID=$(id -u)" > .env

#初始化 airflow
docker-compose up airflow-init

#背景啟動
docker-compose up -d
```

check:
http://127.0.0.1:8080
