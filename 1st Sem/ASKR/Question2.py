import pandas as pd
from math import sqrt

def getMean(column):
    sum = 0 
    for i in column:
        sum += i
    mean = sum / len(column)
    return mean

def standard_deviation(column):
    length, mean, sumDifference  = len(column), getMean(column), 0
    
    for i in column:
        sumDifference += (i - mean) ** 2
    standardDeviation = sqrt(sumDifference/(length-1)) 
    return standardDeviation
    


file = pd.read_csv("data.csv")
print(file)

columns = file.columns

for i in  columns:
    if i == "Unnamed: 0":
        continue
    print(standard_deviation(file[i]))