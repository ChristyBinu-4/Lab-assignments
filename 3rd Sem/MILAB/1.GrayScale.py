#Read an image and convert it into gray scale image without using builtin function for the function

from PIL import Image
import PIL
def convert_to_grayscale(image_path):
    # Open the image
    img = Image.open(image_path)
    
    # Get the size of the image
    width, height = img.size
    
    # Create a new image in grayscale
    grayscale_img = Image.new('L', (width, height))
    
    # Process each pixel to convert to grayscale
    for y in range(height):
        for x in range(width):
            # Get pixel value at x, y
            pixel = img.getpixel((x, y))
            
            # Calculate grayscale value using luminosity method (weighted average)
            gray_value = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
            
            # Set pixel in the new grayscale image
            grayscale_img.putpixel((x, y), gray_value)
    
    # Save or display the grayscale image
    grayscale_img.show()
    grayscale_img.save("grayscale_image.jpg")  # Uncomment to save the image

# Provide the path to the image file
image_path = "test1.png"  # Replace with your image file path
convert_to_grayscale(image_path)
