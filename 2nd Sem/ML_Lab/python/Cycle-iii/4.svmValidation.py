import pandas as pd
import math
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.datasets import load_wine

def svm_crossVal(x, y):
    svm = SVC(kernel = 'linear')
    f1_score = cross_val_score(svm, x, y, cv=10, scoring='f1_weighted')
    return f1_score.mean()

def svm_forSplit(x, y, test_size):
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size, random_state=42)
    svm = SVC(kernel='linear')
    svm.fit(x_train, y_train)
    y_pred = svm.predict(x_test)

    f1_score_ofSplit = f1_score(y_test, y_pred, average='weighted')
    return f1_score_ofSplit

data = load_wine()
x, y = data.data, data.target

# SVM with 10-fold cross validation
f1_scoreOf_crossVal = svm_crossVal(x, y)

# ratios specified 
split_ratios = [0.8, 0.7, 0.6]
f1_scoreOf_splitRatio = []

for ratio in split_ratios:
    f1_score_ofSplit =  svm_forSplit(x, y, test_size= 1 - ratio)
    f1_scoreOf_splitRatio.append(f1_score_ofSplit) 

result = {
    "Method": ["10-fold Cross-Validation"] + [f"{int(ratio*100)}:{round((1-ratio)*100)}" for ratio in split_ratios],
    "F1 Score": [f1_scoreOf_crossVal] + f1_scoreOf_splitRatio
}

resultDf = pd.DataFrame(result)
print(resultDf)