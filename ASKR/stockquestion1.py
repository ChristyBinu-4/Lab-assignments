import pandas as pd

df = pd.read_csv('chart (1).csv', index_col=0, parse_dates=True)


df = df.drop('Pre Open RELIANCE', axis=1)
df = df.dropna()

dfResample = df.resample('15min').ohlc()

print(dfResample)