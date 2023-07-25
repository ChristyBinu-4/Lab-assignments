import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.ensemble import VotingClassifier

data = pd.read_csv('2nd Sem\TFML\Datasets\iris.csv', index_col=0)

x = data.iloc[:, :-1]  
y = data.iloc[:, -1] 

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

svm_linear = SVC(kernel='linear')
svm_rbf = SVC(kernel='rbf')
svm_poly = SVC(kernel='poly')

voting_model = VotingClassifier(estimators=[('svm_linear', svm_linear), ('svm_rbf', svm_rbf), ('svm_poly', svm_poly)], voting='hard')

voting_model.fit(x_train, y_train)

#predict the labels for test data
y_pred = voting_model.predict(x_test)

accuracy = accuracy_score(y_true=y_test, y_pred=y_pred)

# Print the accuracy
print("Accuracy:", accuracy)

