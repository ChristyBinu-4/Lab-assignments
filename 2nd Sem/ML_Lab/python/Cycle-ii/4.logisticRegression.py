import numpy as np

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score


dataFrame = pd.read_csv('/home/christy/Documents/Myself/Academia/PG docs/Lab-assignments/2nd Sem/TFML/Datasets/Breast Cancer.csv')

x = dataFrame.drop('Class', axis=1)
y = dataFrame['Class']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)


accuracy = accuracy_score(y_test, y_pred)
print("Accuracy : ", accuracy)

confusionMatrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(confusionMatrix)
