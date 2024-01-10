#5.Apply histogram equalization on an image and display the resultant image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path = "test1.png"
img = cv.imread(path, 0)  # Read the image as grayscale

# Calculate histogram
hist, bins = np.histogram(img.flatten(), 256, [0, 256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

# Plot histogram and CDF
plt.plot(cdf_normalized, color='b')
plt.hist(img.flatten(), 256, [0, 256], color='r')
plt.xlim([0, 256])
plt.legend(('cdf', 'histogram'), loc='upper left')
plt.show()

# Perform histogram equalization
equ = cv.equalizeHist(img)

# Display the equalized image using OpenCV
cv.imshow('Original Image', img)
cv.imshow('Equalized Image', equ)
cv.waitKey(0)
cv.destroyAllWindows()
