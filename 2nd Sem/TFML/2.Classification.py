from sklearn.cluster import KMeans

dataframe = [
    [1.713, 1.586, 0],
    [0.180, 1.786, 1],
    [0.353, 1.240, 1],
    [0.940, 1.566, 0],
    [1.486, 0.759, 1],
    [1.266, 1.106, 0],
    [1.540, 0.419, 1],
    [0.459, 1.799, 1],
    [0.773, 0.186, 1]
]

test = [.906, .606]

x = [[point[0], point[1]] for point in dataframe]
y = [point[2] for point in dataframe]

k = 3

kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(x)

cluster_prediction = kmeans.predict([test])

cluster_points = [point[2] for point, cluster in zip(dataframe, kmeans.labels_) if cluster == cluster_prediction]
predicted_class = max(set(cluster_points), key=cluster_points.count)

print("Predicted class:", predicted_class)