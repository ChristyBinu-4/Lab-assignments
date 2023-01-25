import pandas as pd

df = pd.read_csv('chart.csv', index_col=0, parse_dates=True)


df = df.drop('Pre Open TATAMOTORS', axis=1)
df = df.dropna()

dfResample = df.resample('5min').ohlc()

print(dfResample)
MaximumValue = dfResample[('TATAMOTORSEQN', 'high')].max()
MinimumValue = dfResample[('TATAMOTORSEQN', 'low')].min()

print("The maximum value of stock is : ", MaximumValue)
print("The minimum value of stock is : ", MinimumValue)
