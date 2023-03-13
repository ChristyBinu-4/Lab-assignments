import pandas as pd 
from numpy import Inf

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

df = pd.read_csv("data.csv")
print(df.to_string())

print("Mean, Minimum and Maximum value  of each column :\n")
for i in df.columns:
        if i == "Unnamed: 0":
            continue
        print(i,getMean(df[i]),getMin(df[i]),getMax(df[i]),sep="||")