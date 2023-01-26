#Download the stock market data of any two script 

import pandas as pd

#function for finding Maximum and minimum values of stock
def findMaxAndMin(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]

  MaximumValue = highValues.max()
  MinimumValue = lowValues.min()

  return MaximumValue, MinimumValue

#function for finding Time stamps of Maximum and minimum values of stock
def timeStampOfMaxMin(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]

  MaximumValue, MinimumValue = findMaxAndMin(dfResample)

  timestampOfMaxValue = dfResample.index[highValues == MaximumValue][0]
  timestampOfMinValue = dfResample.index[lowValues == MinimumValue][0]

  return timestampOfMaxValue, timestampOfMinValue

def findCandleWithMaxMove(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]

  candleMovement = []
  for i in range(dataLength):
    candleMovement.append(highValues[i] - lowValues[i])

  dfResample[(stockName, 'candle movement')] = candleMovement

  candleValues = dfResample[(stockName, 'candle movement')]
  candleWithMaxMove = candleValues.max()
  maxMovedCandleDetails = dfResample.loc[dfResample.index[candleValues == candleWithMaxMove]]

  return maxMovedCandleDetails

stock_tata = pd.read_csv("https://raw.githubusercontent.com/ChristyBinu-4/Lab-assignments/main/ASKR/Tata_Motors_Stock.csv", 
                index_col = 0, parse_dates = True)

for stock in [stock_tata]:
  stock = stock.drop(stock.columns[0], axis=1)#dropping pre open columns
  stock = stock.dropna()#dropping NaN valued rows

  print("Name of stock : ", stock.columns[0])

  date = str(stock.index[1])[0:11]
  print("Date : ", date, "\n")

  dfResample = stock.resample('5min').ohlc()

  #print the Maximum and Minimum values of Stock
  MaximumValue, MinimumValue = findMaxAndMin(dfResample)
  print("The maximum value of stock is : ", MaximumValue)
  print("The minimum value of stock is : ", MinimumValue, '\n')

  #print the timestamp of Stock 
  timestampOfMaxValue, timestampOfMinValue = timeStampOfMaxMin(dfResample)
  print("The Timestamp of maximum value  stock is : ", timestampOfMaxValue)
  print("The Timestamp of minimum value  stock is : ", timestampOfMinValue, end='\n\n')

  dataLength = len(dfResample.index)

  #print the Candle with maximum movement
  maxMovedCandleDetails = findCandleWithMaxMove(dfResample)
  print("Candle with maximum movement is : ", maxMovedCandleDetails, sep='\n\n')