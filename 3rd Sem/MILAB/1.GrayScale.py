from PIL import Image
import PIL
def convert_to_grayscale(image_path):
    
    img = Image.open(image_path)
    width, height = img.size
    
    grayscale_img = Image.new('L', (width, height))
    
    for y in range(height):
        for x in range(width):
    
            pixel = img.getpixel((x, y))
            gray_value = int(0.299 * pixel[0] + 0.587 * pixel[1] + 0.114 * pixel[2])
            grayscale_img.putpixel((x, y), gray_value)
    

    grayscale_img.show()
    grayscale_img.save("grayscale_image.jpg")  

image_path = "test1.png"
convert_to_grayscale(image_path)
