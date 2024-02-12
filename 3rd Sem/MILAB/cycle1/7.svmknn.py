#7.Download any OCR dataset and perform the classification with SVM and KNN. Compare the obtained result
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_openml

import numpy as np

mnist = fetch_openml('mnist_784')

x = np.array(mnist.data, 'int16')
y = np.array(mnist.target, 'int')

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=42)



# Create an SVM classifier
svm_classifier = SVC(kernel='linear')  # You can experiment with different kernels

# Train the SVM classifier
svm_classifier.fit(x_train, y_train)
svm_predictions = svm_classifier.predict(x_test)
svm_accuracy = accuracy_score(y_test, svm_predictions)


# Create a KNN classifier
knn_classifier = KNeighborsClassifier(n_neighbors=5)  # You can experiment with different values of k

knn_classifier.fit(x_train, y_train)
knn_predictions = knn_classifier.predict(x_test)
knn_accuracy = accuracy_score(y_test, knn_predictions)

print("SVM Accuracy:", svm_accuracy)
print("KNN Accuracy:", knn_accuracy)

# Compare the results
if svm_accuracy > knn_accuracy:
    print("SVM performs better.")
elif knn_accuracy > svm_accuracy:
    print("KNN performs better.")
else:
    print("Both classifiers perform equally.")