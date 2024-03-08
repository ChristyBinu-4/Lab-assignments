import pandas as pd
import numpy as np
import urllib.request
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import precision_score, recall_score, f1_score

data = pd.read_csv("2nd Sem\TFML\Datasets\Dataset.csv")

x = data.iloc[:, 2:]
y = data.iloc[:, 1]

y = y.map({'B':0, 'M':1})

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

svm_model = SVC()
svm_model.fit(x_train, y_train)
y_pred_svm = svm_model.predict(x_test)

nb_model = GaussianNB()
nb_model.fit(x_train, y_train)
y_pred_nb = nb_model.predict(x_test)

print(y_test, y_pred_svm, sep="\n")
# # Calculate precision, recall, and F1 score for SVM classifier
precision_svm = precision_score(y_test, y_pred_svm)
recall_svm = recall_score(y_test, y_pred_svm)
f1_svm = f1_score(y_test, y_pred_svm)

# Calculate precision, recall, and F1 score for Naive Bayes classifier
precision_nb = precision_score(y_test, y_pred_nb)
recall_nb = recall_score(y_test, y_pred_nb)
f1_nb = f1_score(y_test, y_pred_nb)

# # Print the results
print("SVM Precision:", precision_svm)
print("SVM Recall:", recall_svm)
print("SVM F1 Score:", f1_svm)
print("Naive Bayes Precision:", precision_nb)
print("Naive Bayes Recall:", recall_nb)
print("Naive Bayes F1 Score:", f1_nb)
