#Question 2 : Download the stock market data of any two script datas from 
#             Official website of Nse. Read 5 minute candle data from script 
#             data and find following : 
#
#             i) Trend of scripts
#             ii) The moving average of five candles

import pandas as pd


#Function for finding trend of a stock 
def trend_Finder(stock):
  stockName = stock.columns[0][0]
  
  dataLength = len(dfResample.index)
  
  openValue = stock[(stockName, 'open')][0]
  closingValue = stock[(stockName, 'close')][dataLength - 1]

  if openValue < closingValue :
    return "Bullish trend"
  elif closingValue < openValue:
    return "Bearish trend"
  else :
    return "neutral"
  

#Function for finding average of movements of multiple candles
def find_average_of_candles(no_of_Candles, dfResample):
  stockName = dfResample.columns[0][0]
  
  candleMovement = []
  dataLength = len(dfResample.index)

  for i in range(dataLength):
    candleMovement.append(dfResample[(stockName, 'high')][i] - dfResample[(stockName, 'low')][i])

  dfResample[(stockName, 'candle movement')] = candleMovement

  candleValues = dfResample[(stockName, 'candle movement')]
  sum = 0
  for i in range(no_of_Candles):
    sum +=  candleValues[i]
  average_Of_FiveCandles = sum/no_of_Candles

  return average_Of_FiveCandles


#importing stock data from my github page
stock_tata = pd.read_csv("https://raw.githubusercontent.com/ChristyBinu-4/Lab-assignments/main/ASKR/Tata_Motors_Stock.csv", 
                index_col = 0, parse_dates = True)
stock_reliance = pd.read_csv("https://raw.githubusercontent.com/ChristyBinu-4/Lab-assignments/main/ASKR/Reliance_Stock.csv",
                index_col = 0, parse_dates = True)

for stock in [stock_tata, stock_reliance]:

  stock = stock.drop(stock.columns[0], axis=1)#dropping pre open columns
  stock = stock.dropna()#dropping NaN valued rows                

  print("\n","--------------------------------------------------------------------------------")

  nameOfStock = str(stock.columns[0])[:-3]#Stripping last word EQN for printing name of stock
  print("Name of stock : ", nameOfStock)

  date = str(stock.index[1])[0:11]
  print("Date : ", date, "\n")

  dfResample = stock.resample('5min').ohlc()

  #To print the trend of stock
  print("Trend of stock : ", trend_Finder(dfResample))

  # To print moving average of five candles
  print("Moving average of five candles in a stock is : {: .2f}".format(find_average_of_candles(5, dfResample)))
