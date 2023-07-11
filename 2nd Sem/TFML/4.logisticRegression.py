import numpy as np

import pandas as pd
from sklearn.model_selection import train_test_split
#from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

class LogisticRegression:
    def __init__(self, learning_rate=0.01, num_iterations=1000):
        self.learning_rate = learning_rate
        self.num_iterations = num_iterations
        self.weights = None
        self.bias = None

    def _sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def _initialize_parameters(self, num_features):
        self.weights = np.zeros(num_features)
        self.bias = 0

    def fit(self, X, y):
        num_samples, num_features = X.shape
        self._initialize_parameters(num_features)

        for _ in range(self.num_iterations):
            linear_model = np.dot(X, self.weights) + self.bias
            y_pred = self._sigmoid(linear_model)

            dw = (1 / num_samples) * np.dot(X.T, (y_pred - y))
            db = (1 / num_samples) * np.sum(y_pred - y)

            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict(self, X):
        linear_model = np.dot(X, self.weights) + self.bias
        y_pred = self._sigmoid(linear_model)
        y_pred_classes = np.where(y_pred > 0.5, 1, 0)
        return y_pred_classes


dataFrame = pd.read_csv('Breast Cancer.csv')

x = dataFrame.drop('Class', axis=1)
y = dataFrame['Class']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print(y_pred, y_test, sep='\n\n')
# accuracy = accuracy_score(y_test, y_pred)
# print("Accuracy : ", accuracy)

# confusionMatrix = confusion_matrix(y_test, y_pred)
# print("Confusion Matrix:")
# print(confusionMatrix)
