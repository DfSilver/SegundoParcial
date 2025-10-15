# SegundoParcial

# 🧠 Proyecto ETL Dow Jones — Análisis de Sentimiento y Tendencias del Mercado

## 📘 Descripción General

Este proyecto implementa un **pipeline ETL (Extract, Transform, Load)** sobre un dataset del **índice Dow Jones**, que contiene información sobre análisis de sentimiento y comportamiento del mercado bursátil.

El objetivo principal es **extraer**, **limpiar**, **transformar** y **visualizar** los datos para identificar relaciones entre el **sentimiento del mercado** y las **variaciones del índice Dow Jones**, permitiendo comprender cómo el análisis de sentimiento puede influir en las decisiones financieras.

---

## 🧩 Estructura del Proyecto

├── data/
│ ├── stock_senti_analysis.csv # Dataset original
│ └── processed_data.csv # Dataset limpio y transformado
│
├── output/
│ └── plots/ # Carpeta con las visualizaciones generadas
│
├── src/
│ ├── extract.py # Script de extracción de datos
│ ├── transform.py # Limpieza y transformación
│ ├── load.py # Carga y almacenamiento del dataset procesado
│ └── visualize.py # Generación de gráficas
│
├── main.py # Archivo principal que ejecuta todo el pipeline ETL
├── requirements.txt # Dependencias del proyecto
└── README.md # Documentación general del proyecto

markdown

---

## ⚙️ Flujo ETL Implementado

### 1️⃣ Extracción
El módulo `extract.py` se encarga de **leer el dataset original** desde la carpeta `data/stock_senti_analysis.csv` usando **pandas**.

### 2️⃣ Transformación
En `transform.py`, los datos son **limpiados, normalizados y tipificados**:
- Conversión de fechas.
- Eliminación de valores nulos y duplicados.
- Conversión de columnas numéricas.
- Normalización de variables de sentimiento.

### 3️⃣ Carga
El módulo `load.py` guarda el resultado limpio como `processed_data.csv` dentro de la carpeta `data/`.

### 4️⃣ Visualización
En `visualize.py` se generan **5 gráficos analíticos**:
1. Tendencia del sentimiento promedio en el tiempo.  
2. Distribución general de sentimientos (positivo, negativo, neutro).  
3. Volumen promedio de trading por sentimiento.  
4. Comparación entre sentimiento promedio e índice Dow Jones.  
5. Correlación entre sentimiento y rendimiento diario.

Los gráficos se guardan en `output/plots/`.

---

## 💻 Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
2️⃣ Crear y activar entorno virtual (opcional)
bash

python -m venv venv
source venv/bin/activate     # En macOS / Linux
venv\Scripts\activate        # En Windows
3️⃣ Instalar dependencias
bash

pip install -r requirements.txt
4️⃣ Ejecutar el pipeline completo
bash

python main.py
📊 Resultados Esperados
Tras la ejecución, el proyecto genera:

data/processed_data.csv → dataset limpio y normalizado.

5 gráficas analíticas en output/plots/ que evidencian las relaciones entre sentimiento e indicadores del mercado.

Ejemplo de salida esperada:

bash
✅ Extracción de datos completada.
✅ Transformación de datos finalizada.
✅ Archivo procesado guardado en /data/processed_data.csv
✅ 5 visualizaciones generadas en /output/plots/
🧱 Commits y Ramas
Este proyecto sigue una estructura de control de versiones profesional:

Rama	Propósito
main	Versión estable final
development	Integración de nuevas funciones
feature/etl	Desarrollo del pipeline ETL

Flujo de trabajo:
bash

feature/etl  →  development  →  main
Cada etapa del ETL se asocia a un commit:

Estructura base del proyecto

Extracción de datos

Transformación de datos

Carga de datos procesados

Visualizaciones y documentación

🧰 Dependencias
Declaradas en requirements.txt:

nginx
Copiar código
pandas
numpy
matplotlib

👨‍💻 Autor
Daniel Moreno
Proyecto académico — Ingeniería de Software
Universidad de San Buenaventura
2025

