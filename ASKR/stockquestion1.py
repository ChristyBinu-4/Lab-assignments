import plotly.graph_objects as go
from numpy import Inf
import pandas as pd

def getMean(column):
    sum = 0 
    for i in column:
        sum += i
    mean = sum / len(column)
    return mean

def getMin(column):
    min = Inf
    for i in column:
        if i < min :
            min = i
    return min

def getMax(column):
    max = 0 
    for i in column:
        if i > max :
            max = i
    return max

df = pd.read_csv('chart.csv')

time = df.columns[0]
stock = df.columns[1]

oneMinutePrice = dict()

#Entering all data values into a dictionary
for index, datetime in enumerate(df[time]):
  if(datetime not in oneMinutePrice.keys()):
    oneMinutePrice.update({datetime : [df[stock][index]]})
  else: 
    oneMinutePrice[datetime].append(df[stock][index])

#finding mean of prices in specfic minutes
for key in oneMinutePrice:
  meanOfKey = getMean(oneMinutePrice[key])
  minOfKey = getMin(oneMinutePrice[key])
  maxOfKey = getMax(oneMinutePrice[key])
  oneMinutePrice.update({key : [meanOfKey, minOfKey, maxOfKey]})
  print(key , " = > ", oneMinutePrice[key])