import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/ChristyBinu-4/Lab-assignments/main/ASKR/chart.csv", 
                index_col = 0, parse_dates = True)

df = df.drop('Pre Open TATAMOTORS', axis=1)
df = df.dropna()

dfResample = df.resample('5min').ohlc()

print(dfResample)
MaximumValue = dfResample[('TATAMOTORSEQN', 'high')].max()
MinimumValue = dfResample[('TATAMOTORSEQN', 'low')].min()

print("The maximum value of stock is : ", MaximumValue)
print("The minimum value of stock is : ", MinimumValue)

timestampOfMaxValue = dfResample.index[dfResample[('TATAMOTORSEQN', 'high')] == MaximumValue][0]
timestampOfMinValue = dfResample.index[dfResample[('TATAMOTORSEQN', 'low')] == MinimumValue][0]

print("The Timestamp of maximum value  stock is : ", timestampOfMaxValue)
print("The Timestamp of minimum value  stock is : ", timestampOfMinValue)