# Informe Técnico Integrado - Siniestralidad Vial en Santiago de Cali

## 1. Objetivos Refinados y ODS
* *ODS 3 (Salud y Bienestar):* Reducción de muertes y lesiones por accidentes de tráfico.
* *ODS 11 (Ciudades y Comunidades Sostenibles):* Sistemas de transporte seguros y accesibles.

## 2. Arquitectura de Ingesta (3 Fuentes)
1. *Fuente 1 (Archivo CSV):* Consolidado histórico de homicidios por condición de víctima.
2. *Fuente 2 (API REST Pública):* Conexión con datos abiertos de la Alcaldía de Cali (datos.cali.gov.co).
3. *Fuente 3 (Archivo CSV Masivo):* Registro detallado de incidentes viales con más de 10,000 registros.

## 3. Almacenamiento y Modelo Relacional (SQLite)
Los datos limpios se procesan y almacenan localmente en data/processed/accidentes.sqlite, bajo un esquema relacional optimizado para consultas SQL.

## 4. Hallazgos del EDA y V de Cramér
Se implementó el cálculo formal de asociación categórica mediante la *V de Cramér*, identificando correlaciones clave entre las comunas de Cali y la severidad de los siniestros viales.