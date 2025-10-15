from pathlib import Path
import sqlite3
import pandas as pd

BASE = Path(__file__).resolve().parents[1]
CLEAN = BASE / 'data' / 'clean' / 'clean.csv'
DB = BASE / 'data' / 'clean' / 'etl_db.sqlite'

def load():
    df = pd.read_csv(CLEAN, parse_dates=['Date'])
    conn = sqlite3.connect(DB)
    df.to_sql('news_sentiment', conn, if_exists='replace', index=False)
    conn.close()
    print(f"Cargado en SQLite: {DB} -> tabla news_sentiment")

if __name__ == '__main__':
    load()
