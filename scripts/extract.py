import os
import requests
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def extract_csv(file_path: str) -> pd.DataFrame:
    """Extrae datos del CSV manejando automáticamente delimitadores (coma/punto y coma) y codificación."""
    try:
        # Intento 1: lectura estándar
        return pd.read_csv(file_path)
    except (pd.errors.ParserError, UnicodeDecodeError):
        try:
            # Intento 2: delimitador punto y coma y codificación latina (común en datasets colombianos)
            return pd.read_csv(file_path, sep=';', encoding='latin-1')
        except Exception:
            # Intento 3: detección automática de separador con motor de Python
            return pd.read_csv(file_path, sep=None, engine='python', encoding='utf-8-sig')

        
def extract_supabase(table_name: str = "homicidios_victima") -> pd.DataFrame:
    """Extrae datos de la base de datos PostgreSQL en Supabase."""
    db_url = os.getenv("SUPABASE_DB_URL")
    if not db_url:
        raise ValueError("No se encontró SUPABASE_DB_URL en el archivo .env")
    engine = create_engine(db_url)
    return pd.read_sql(f"SELECT * FROM {table_name}", con=engine)

def extract_api_weather(start_date: str = "2024-01-01", end_date: str = "2024-01-31") -> pd.DataFrame:
    """Extrae datos climáticos de Cali desde la API Open-Meteo."""
    url = "https://archive-api.open-meteo.com/v1/archive"
    params = {
        "latitude": 3.4516,
        "longitude": -76.5320,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ["temperature_2m", "precipitation", "rain", "weather_code"],
        "timezone": "America/Bogota"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    df = pd.DataFrame(data["hourly"])
    df['time'] = pd.to_datetime(df['time'])
    return df

if __name__ == "__main__":
    # Verificación de conexión a las 3 fuentes
    df_csv = extract_csv("data/raw/siniestros_cali.csv")
    df_db = extract_supabase()
    df_api = extract_api_weather()

    print(f"✅ CSV cargado correctamente: {df_csv.shape}")
    print(f"✅ Supabase cargado correctamente: {df_db.shape}")
    print(f"✅ API Clima cargada correctamente: {df_api.shape}")