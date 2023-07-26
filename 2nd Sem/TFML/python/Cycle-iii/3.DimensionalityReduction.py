import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score

data = pd.read_csv(r"2nd Sem\TFML\Datasets\1000_features.csv")

x = data.drop(data.columns[0], axis=1)
y = data[data.columns[0]]

pca_dimensions = [300, 400, 500]
result = []

for dimensions in pca_dimensions:

    pca = PCA(n_components=dimensions)
    x_pca = pca.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(x_pca, y, test_size=0.2, random_state=42)
    svm = SVC()
    svm.fit(x_train, y_train)
    y_pred = svm.predict(x_test)

    precision = precision_score(y_test, y_pred, average='macro', zero_division=1)
    recall = recall_score(y_test, y_pred, average='macro', zero_division=1)
    f1 = f1_score(y_test, y_pred, average='macro', zero_division=1)

    result.append({'Dimension': dimensions, 'Precision' : precision, 'Recall' : recall, 'F1 score': f1})

result = pd.DataFrame(result) #making result as a dataframe for printing

print(result)

