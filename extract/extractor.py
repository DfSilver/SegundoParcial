import os
import shutil
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DATA = BASE / 'data'
RAW = DATA / 'raw'
RAW.mkdir(parents=True, exist_ok=True)

SOURCE = DATA / 'stock_senti_analysis.csv'
TARGET = RAW / 'raw.csv'

def extract():
    """Copia el CSV original a data/raw/raw.csv (simula extracción)."""
    if not SOURCE.exists():
        raise FileNotFoundError(f"No se encontró {SOURCE}. Sube el CSV a data/")
    shutil.copy2(SOURCE, TARGET)
    print(f"Extraído: {TARGET}")

if __name__ == '__main__':
    extract()
