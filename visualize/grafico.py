from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

BASE = Path(__file__).resolve().parents[1]
CLEAN = BASE / 'data' / 'clean' / 'clean.csv'
OUT = BASE / 'outputs'
OUT.mkdir(parents=True, exist_ok=True)

def plot_time_series(df):
    daily = df.groupby('Date')['sentiment'].mean()
    plt.figure(figsize=(10,4))
    plt.plot(daily.index, daily.values)
    plt.title('Daily average sentiment')
    plt.tight_layout()
    plt.savefig(OUT / '01_daily_avg_sentiment.png')
    plt.close()

def plot_histogram(df):
    plt.figure(figsize=(6,4))
    plt.hist(df['sentiment'], bins=[-0.1,0.1,0.9,1.1])
    plt.title('Sentiment label counts')
    plt.tight_layout()
    plt.savefig(OUT / '02_sentiment_hist.png')
    plt.close()

def plot_top_words(df, n=20):
    text = ' '.join(df['headline_clean'].fillna(''))
    words = [w for w in text.split() if len(w)>2]
    common = Counter(words).most_common(n)
    labels, values = zip(*common)
    plt.figure(figsize=(8,6))
    plt.barh(labels, values)
    plt.title(f'Top {n} words')
    plt.tight_layout()
    plt.savefig(OUT / '03_top_words.png')
    plt.close()

def plot_weekday_sentiment(df):
    weekday = df.groupby('dayofweek')['sentiment'].mean()
    plt.figure(figsize=(8,4))
    plt.bar(weekday.index, weekday.values)
    plt.title('Average sentiment by weekday')
    plt.tight_layout()
    plt.savefig(OUT / '04_weekday_sentiment.png')
    plt.close()

def plot_sentiment_rolling(df):
    daily = df.groupby('Date')['sentiment'].mean().sort_index()
    rolling = daily.rolling(30).mean()
    plt.figure(figsize=(10,4))
    plt.plot(daily.index, daily.values, alpha=0.3, label='Daily')
    plt.plot(rolling.index, rolling.values, label='30D rolling')
    plt.legend()
    plt.title('Daily vs 30-day rolling sentiment')
    plt.tight_layout()
    plt.savefig(OUT / '05_rolling_sentiment.png')
    plt.close()

def main():
    df = pd.read_csv(CLEAN, parse_dates=['Date'])
    plot_time_series(df)
    plot_histogram(df)
    plot_top_words(df)
    plot_weekday_sentiment(df)
    plot_sentiment_rolling(df)
    print(f"Gráficas generadas en {OUT}")

if __name__ == '__main__':
    main()
