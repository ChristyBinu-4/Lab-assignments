import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error, r2_score

df = pd. read_excel('/home/christy/Documents/Myself/Academia/PG docs/Lab-assignments/2nd Sem/TFML/Datasets/Power Plant.xlsx')

x = df[['AT', 'V', 'AP', 'RH']]
y = df['PE']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)


model = LinearRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

mean_squared_err = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error (MSE):", mean_squared_err)
print("R-squared (R2) Score:", r2)