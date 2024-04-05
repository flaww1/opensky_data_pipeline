FROM apache/airflow:2.8.4-python3.9

COPY requirements.txt /opt/airflow/

RUN pip install --no-cache-dir -r /opt/airflow/requirements