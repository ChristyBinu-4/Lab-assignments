#Display the histogram of the gray scale image.
from PIL import Image
import matplotlib.pyplot as plt

def display_histogram(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Convert the image to grayscale if it's not already in grayscale
    img = img.convert('L')
    
    # Calculate the histogram
    histogram = img.histogram()
    
    # Display the histogram
    plt.figure(figsize=(8, 4))
    plt.title('Histogram of Grayscale Image')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.hist(histogram, bins=256, range=(0, 256), color='gray', alpha=0.7)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

# Provide the path to the image file
image_path = "grayscale_image.jpg"  # Replace with your image file path

display_histogram(image_path)
