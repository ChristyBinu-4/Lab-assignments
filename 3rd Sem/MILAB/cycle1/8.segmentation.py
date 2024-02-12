#8.Implement any two segmentation algorithms and compare the efficiency with ground truth

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import normalized_mutual_info_score

# Create a synthetic ground truth image
np.random.seed(42)
ground_truth, _ = make_blobs(n_samples=300, centers=3, random_state=42, cluster_std=2.0)
ground_truth = StandardScaler().fit_transform(ground_truth)

# Generate image with ground truth labels
ground_truth_labels = np.argmax(ground_truth, axis=1)
ground_truth_labels = ground_truth_labels.reshape((10, 30))

# Plot ground truth
plt.figure(figsize=(12, 4))
plt.subplot(1, 3, 1)
plt.imshow(ground_truth_labels, cmap='viridis')
plt.title('Ground Truth')
plt.axis('off')

# Generate image data for clustering
data, _ = make_blobs(n_samples=300, centers=3, random_state=42, cluster_std=2.0)

# Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(data)
kmeans_labels = kmeans_labels.reshape((10, 30))

# Plot K-Means clustering result
plt.subplot(1, 3, 2)
plt.imshow(kmeans_labels, cmap='viridis')
plt.title('K-Means Clustering')
plt.axis('off')

# Apply Mean Shift clustering
bandwidth = estimate_bandwidth(data, quantile=0.2, n_samples=300)
meanshift = MeanShift(bandwidth=bandwidth, bin_seeding=True)
meanshift_labels = meanshift.fit_predict(data)
meanshift_labels = meanshift_labels.reshape((10, 30))

# Plot Mean Shift clustering result
plt.subplot(1, 3, 3)
plt.imshow(meanshift_labels, cmap='viridis')
plt.title('Mean Shift Clustering')
plt.axis('off')

plt.tight_layout()
plt.show()

# Compare clustering results with ground truth
nmi_kmeans = normalized_mutual_info_score(ground_truth_labels.flatten(), kmeans_labels.flatten())
nmi_meanshift = normalized_mutual_info_score(ground_truth_labels.flatten(), meanshift_labels.flatten())

print(f"Normalized Mutual Information (NMI) - K-Means: {nmi_kmeans:.4f}")
print(f"Normalized Mutual Information (NMI) - Mean Shift: {nmi_meanshift:.4f}")