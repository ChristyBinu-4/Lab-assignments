from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# Load the MNIST dataset
mnist = fetch_openml('mnist_784')
X = mnist.data
y = mnist.target

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Perform PCA for dimensionality reduction
pca = PCA(n_components=500)
X_train_pca = pca.fit_transform(X_train)
X_test_pca = pca.transform(X_test)

# Apply the K-means algorithm
kmeans = KMeans(n_clusters=20, random_state=42)
kmeans.fit(X_train_pca)

# Assign cluster labels
y_train_pred = kmeans.labels_

# Map cluster labels to class labels
label_mapping = {}
for cluster_label in range(20):
    mask = (y_train_pred == cluster_label)
    mapped_label = y_train[mask].mode()[0]
    label_mapping[cluster_label] = mapped_label

y_train_pred_mapped = [label_mapping[cluster_label] for cluster_label in y_train_pred]

# Calculate classification accuracy
accuracy = accuracy_score(y_train, y_train_pred_mapped)
print("Training Accuracy:", accuracy)
