# 🚦 Proyecto ETL: Segunda Entrega - Siniestralidad Vial en Santiago de Cali

Repositorio oficial para la segunda entrega del curso de **ETL (G51)** del programa de Ingeniería de Datos e Inteligencia Artificial de la Universidad Autónoma de Occidente (UAO). El proyecto implementa un pipeline de datos automatizado, reproducible y robusto enfocado en el análisis de accidentalidad vial y movilidad urbana en Santiago de Cali.

---

## 👥 Equipo de Trabajo
* **Laura Torres** – Documentación, Coordinación y Arquitectura
* **Juliana Serrano** – Análisis de Datos, EDA y Validación
* **Juan Hernández** – Desarrollo Back-end e Ingesta
* **Juan López** – Visualización y Reporte Integrado

---

## 🎯 1. Requerimientos Refinados y Objetivos 
El objetivo principal de este pipeline es extraer, transformar, validar y cargar datos de múltiples fuentes heterogéneas para analizar los patrones temporales, espaciales y las condiciones de las víctimas en los siniestros viales de Santiago de Cali. 
* **Alineación con los ODS:**
  * **ODS 3 (Salud y Bienestar):** Meta 3.6 - Reducir globalmente las muertes y lesiones por accidentes de tráfico.
  * **ODS 11 (Ciudades y Comunidades Sostenibles):** Meta 11.2 - Proporcionar acceso a sistemas de transporte seguros y sostenibles.

---

## 📥 2. Ingesta de Datos: Arquitectura de 3 Fuentes 
El pipeline implementa de forma automatizada **tres tareas distintas de extracción** en Apache Airflow, abarcando las tipologías exigidas:
1. **Fuente 1 (Archivo CSV - Primera Entrega):** Consolidado histórico de homicidios por condición de víctima (2004-2021) provisto por la Secretaría de Salud / Medicina Legal.
2. **Fuente 2 (API REST Pública):** Datos en tiempo real o catálogos abiertos de la Alcaldía de Santiago de Cali (`datos.cali.gov.co`) sobre infraestructura y reportes viales.
3. **Fuente 3 (Archivo CSV Masivo Adicional):** Dataset detallado de incidentes y lesionados viales que supera las 10,000 filas analíticas, cumpliendo holgadamente con los requerimientos de volumetría.

---

## ⚙️ 3. Transformación de Datos 
* Estandarización de nombres de columnas a minúsculas y eliminación de espacios.
* Normalización de fechas y limpieza de valores nulos o marcas institucionales (como `"SD"` o cadenas vacías).
* Enriquecimiento y cruce de las tres fuentes en un dataset unificado y consistente.

---

## 🛡️ 4. Validación de Calidad con Great Expectations 
* Se implementó una suite de validación integrada directamente en el flujo de Airflow.
* Valida reglas de integridad (ausencia de nulos en llaves primarias, rangos de conteos positivos y tipos de datos correctos).
* **Política de Carga:** El pipeline registra los resultados y **bloquea la carga** hacia el esquema final si los datos no cumplen con los umbrales de calidad establecidos.

---

## 🗄️ 5. Modelado y Carga de Datos - Data Warehouse 
* **Almacenamiento:** Base de datos relacional **SQLite** ubicada en `data/processed/accidentes.sqlite` (excluida del control de versiones mediante `.gitignore` para optimizar espacio).
* **Modelo:** Estructurado bajo un esquema relacional con tablas staging, dimensiones normalizadas y una tabla de hechos central que alimenta directamente las consultas analíticas.

---

## 📈 6. Visualizaciones y Reporte Integrado 
* Se eliminaron las gráficas estáticas aisladas. Las visualizaciones se consolidan en un **reporte técnico integrado** dentro de la carpeta `reports/`, consumiendo de manera exclusiva las consultas SQL ejecutadas sobre el Data Warehouse en SQLite.
* **EDA Avanzado:** Incorpora el cálculo formal de asociación categórica mediante la **V de Cramér** y pruebas de Chi-cuadrado para evaluar la relación entre variables como la comuna y la gravedad del incidente.

---

## 🚀 7. Guía de Ejecución y Despliegue Local

### Requisitos Previos
* Python 3.11 o 3.12 instalado.
* Git para control de versiones.

### Instrucciones de Instalación y Ejecución (PowerShell / Linux)

1. **Clonar el repositorio y abrir la terminal en la raíz:**
   ```bash
   git clone [https://github.com/juanH40-ING/Delivery_2.git](https://github.com/juanH40-ING/Delivery_2.git)
   cd Delivery_2



pandas==2.2.1
requests==2.31.0
sqlalchemy==2.0.28
psycopg2-binary==2.9.9
great-expectations==0.18.12
jupyter==1.0.0
matplotlib==3.8.3
seaborn==0.13.2
python-dotenv==1.0.1
