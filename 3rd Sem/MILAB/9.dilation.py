# Input an image and perform the following morphological operations
# i) Dilation
# ii) Erosion
# iii) Opening
# iv) Closing
# Display the results.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('test1.png')  # Replace with your image file

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the kernel for morphological operations
kernel = np.ones((5, 5), np.uint8)  # You can adjust the size of the kernel as needed

# Perform morphological operations
dilated_image = cv2.dilate(gray_image, kernel, iterations=1)
eroded_image = cv2.erode(gray_image, kernel, iterations=1)
opened_image = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel)
closed_image = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)

# Display the original and processed images

cv2.imshow('Original',image)

cv2.imshow('Dilated', dilated_image)

cv2.imshow('Eroded', eroded_image)

cv2.imshow('Opened', opened_image)

cv2.imshow('Closed', closed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

