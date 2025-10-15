from pathlib import Path
import pandas as pd
import numpy as np
import re

BASE = Path(__file__).resolve().parents[1]
RAW = BASE / 'data' / 'raw' / 'raw.csv'
CLEAN_DIR = BASE / 'data' / 'clean'
CLEAN_DIR.mkdir(parents=True, exist_ok=True)
CLEAN = CLEAN_DIR / 'clean.csv'

def clean_text(s):
    if pd.isna(s):
        return ''
    s = str(s).lower()
    s = re.sub(r'http\\S+|www\\.[^\\s]+', '', s)
    s = re.sub(r'[^a-z0-9\\s]', ' ', s)
    s = re.sub(r'\\s+', ' ', s).strip()
    return s

def transform():
    df = pd.read_csv(RAW, encoding='latin1')
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    top_cols = [c for c in df.columns if c.lower().startswith('top')]
    df['headline'] = df[top_cols].fillna('').agg(' '.join, axis=1)
    df['headline_clean'] = df['headline'].apply(clean_text)
    df['sentiment'] = pd.to_numeric(df['Label'], errors='coerce').fillna(0).astype(int)
    df = df.dropna(subset=['Date'])
    df = df.drop_duplicates(subset=['Date', 'headline_clean'])
    df['year'] = df['Date'].dt.year
    df['month'] = df['Date'].dt.month
    df['dayofweek'] = df['Date'].dt.day_name()

    df.to_csv(CLEAN, index=False, encoding='utf-8')
    print(f"Transformado y guardado: {CLEAN}")
    return df

if __name__ == '__main__':
    transform()
