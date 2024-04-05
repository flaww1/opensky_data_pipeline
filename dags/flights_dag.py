from airflow import DAG
import datetime

with DAG("flights_dag",
        start_date = datetime(2024,4,4),
        schedule_interval="@daily",  
        catchup=False) as dag:
  

