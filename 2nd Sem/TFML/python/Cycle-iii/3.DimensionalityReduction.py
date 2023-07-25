import pandas as pd
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score

data = pd.read_csv(r"2nd Sem\TFML\Datasets\1000_features.csv")

x = data.drop(data.columns[0], axis=1)
y = data[data.columns[0]]

pca_dimensions = [300, 400, 500]

for dimensions in pca_dimensions:

    pca = PCA(n_components=dimensions)
    
