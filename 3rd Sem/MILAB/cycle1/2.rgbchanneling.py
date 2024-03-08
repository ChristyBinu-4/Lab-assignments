#Read an image and display the RGB channel images separately.
from PIL import Image
import matplotlib.pyplot as plt

def display_rgb_channels(image_path):
    img = Image.open(image_path)
    
    # Convert the image to RGB mode if it's not already in RGB
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Split the image into RGB channels
    r, g, b = img.split()
    
    # Display each channel separately
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 3, 1)
    plt.title('Red Channel')
    plt.imshow(r, cmap='gray')
    plt.axis('off')
    
    plt.subplot(1, 3, 2)
    plt.title('Green Channel')
    plt.imshow(g, cmap='gray')
    plt.axis('off')
    
    plt.subplot(1, 3, 3)
    plt.title('Blue Channel')
    plt.imshow(b, cmap='gray')
    plt.axis('off')
    
    plt.tight_layout()
    plt.show()

# Provide the path to the image file
image_path = "rgb.png"  # Replace with your image file path
display_rgb_channels(image_path)
