from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# Load the MNIST dataset
mnist = fetch_openml('mnist_784')
X = mnist.data
y = mnist.target

# Perform PCA for dimensionality reduction
pca = PCA(n_components=500)
X_pca = pca.fit_transform(X)

# Apply the K-means algorithm
kmeans = KMeans(n_clusters=20, random_state=42)
kmeans.fit(X_pca)

# Assign cluster labels
y_pred = kmeans.labels_

# Map cluster labels to class labels
label_mapping = {}
for cluster_label in range(20):
    mask = (y_pred == cluster_label)
    mapped_label = y[mask].mode()[0]
    label_mapping[cluster_label] = mapped_label

y_pred_mapped = [label_mapping[cluster_label] for cluster_label in y_pred]

# Calculate classification accuracy
accuracy = accuracy_score(y, y_pred_mapped)
print("Training Accuracy:", accuracy)
