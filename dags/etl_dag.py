import os
import sys
from datetime import datetime
from airflow import DAG

try:
    from airflow.providers.standard.operators.python import PythonOperator
except ImportError:
    from airflow.operators.python import PythonOperator

# Asegurar la ruta raíz del proyecto en sys.path
ruta_proyecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_proyecto not in sys.path:
    sys.path.append(ruta_proyecto)

from src.etl import (
    extraer_fuente_1_csv,
    extraer_fuente_2_api,
    extraer_fuente_3_csv_masivo,
    ejecutar_pipeline_etl,
)

default_args = {
    'owner': 'laura_torres',
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
}

with DAG(
    dag_id='pipeline_etl_cali_3_fuentes',
    default_args=default_args,
    schedule='@daily',  # <--- Corregido de schedule_interval a schedule
    catchup=False,
    description='Pipeline ETL automatizado con 3 fuentes (CSV, API, CSV Masivo) hacia SQLite',
) as dag:

    t1 = PythonOperator(
        task_id='extraer_fuente_1_csv_historico',
        python_callable=extraer_fuente_1_csv,
    )

    t2 = PythonOperator(
        task_id='extraer_fuente_2_api_publica',
        python_callable=extraer_fuente_2_api,
    )

    t3 = PythonOperator(
        task_id='extraer_fuente_3_csv_masivo',
        python_callable=extraer_fuente_3_csv_masivo,
    )

    t_load = PythonOperator(
        task_id='transformar_y_cargar_sqlite',
        python_callable=ejecutar_pipeline_etl,
    )

    [t1, t2, t3] >> t_load