import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 

iris = pd.read_csv('/home/christy/Documents/Myself/Academia/PG docs/Lab-assignments/2nd Sem/TFML/iris.csv')
iris = iris[["Petal.Width", "Petal.Length"]]

x = iris['Petal.Length']
y = iris['Petal.Width']

plt.scatter(x, y)
plt.xlabel('petal length')
plt.ylabel('petal width')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size= 0.4, random_state= 23)

x_train = np.array(x_train).reshape(-1, 1)
x_test = np.array(x_test).reshape(-1, 1)

lr = LinearRegression()

lr.fit(x_train, y_train)
c = lr.intercept_
m = lr.coef_

y_pred_train = m * x_train + c

print(y_pred_train)
