import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics  import accuracy_score, precision_score, recall_score

data = pd.read_csv(r'2nd Sem\TFML\Datasets\Titanic_dataset.csv')

data = data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]
data = data.dropna()
data['Sex'] = data['Sex'].map({'female': 0, 'male': 1})

x = data.drop('Survived', axis=1)
y = data['Survived']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

model = GaussianNB()
model.fit(x_train, y_train)

# Make predictions on the test data
y_pred = model.predict(x_test)

# Calculate accuracy, precision, and recall
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
