#6.Display the edge map of an image with any edge detection algorithm
import cv2
import matplotlib.pyplot as plt

# Read the image
image_path = "test1.png"  # Replace with your image file path
img = cv2.imread(image_path, 0)  # Read image in grayscale

# Apply Canny edge detection
edges = cv2.Canny(img, 100, 200)  # Adjust threshold values for best results

# Display the original and edge-detected images
cv2.imshow("Original", img)
cv2.imshow("canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()