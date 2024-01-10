#Read an image and convert it into binary image using threshold.
from PIL import Image
import matplotlib.pyplot as plt

def convert_to_binary(image_path, threshold_value):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to grayscale
    img = img.convert('L')
    
    # Apply thresholding to create a binary image
    binary_img = img.point(lambda p: 0 if p < threshold_value else 255, '1')
    
    # Display the original and binary images
    plt.figure(figsize=(8, 4))
    
    plt.subplot(1, 2, 1)
    plt.title('Original Image')
    plt.imshow(img, cmap='gray')
    plt.axis('off')
    
    plt.subplot(1, 2, 2)
    plt.title('Binary Image (Threshold={})'.format(threshold_value))
    plt.imshow(binary_img, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Provide the path to the image file and the threshold value
image_path = "test1.png"  # Replace with your image file path
threshold = 129  # Replace with your threshold value (0 to 255)

convert_to_binary(image_path, threshold)
