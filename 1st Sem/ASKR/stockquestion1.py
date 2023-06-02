#Question 1 : Download the stock market data of any two script datas from 
#             Official website of Nse. Read 5 minute candle data from script 
#             data and find following : 
#
#             i) The maximum and minimum values
#             ii) Print the time stamp of maximum and minimum values
#             iii) The candle with maximum movement

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


#function for finding candle with maximum movements
def findCandleWithMaxMove(dfResample):
  stockName = dfResample.columns[0][0]
  highValues = dfResample[(stockName, 'high')]
  lowValues = dfResample[(stockName, 'low')]

  candleMovement = []
  dataLength = len(dfResample.index)

  for i in range(dataLength):
    candleMovement.append(highValues[i] - lowValues[i])

  dfResample[(stockName, 'candle movement')] = candleMovement

  candleValues = dfResample[(stockName, 'candle movement')]
  candleWithMaxMove = candleValues.max()
  maxMovedCandleDetails = dfResample.loc[dfResample.index[candleValues == candleWithMaxMove]]

  return maxMovedCandleDetails


#importing stock data from my github page
stock_tata = pd.read_csv("https://raw.githubusercontent.com/ChristyBinu-4/Lab-assignments/main/ASKR/Tata_Motors_Stock.csv", 
                index_col = 0, parse_dates = True)
stock_reliance = pd.read_csv("https://raw.githubusercontent.com/ChristyBinu-4/Lab-assignments/main/ASKR/Reliance_Stock.csv",
                index_col = 0, parse_dates = True)

#Using stock datas to find answers to above mentioned questions
for stock in [stock_tata, stock_reliance]:

  stock = stock.drop(stock.columns[0], axis=1)#dropping pre open columns
  stock = stock.dropna()#dropping NaN valued rows

  print("\n","--------------------------------------------------------------------------------")

  nameOfStock = str(stock.columns[0])[:-3]#Stripping last word EQN for printing name of stock
  print("Name of stock : ", nameOfStock)

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

  

  #print the Candle with maximum movement
  maxMovedCandleDetails = findCandleWithMaxMove(dfResample)
  print("Candle with maximum movement is : ", maxMovedCandleDetails, sep='\n\n')
  print("--------------------------------------------------------------------------------")