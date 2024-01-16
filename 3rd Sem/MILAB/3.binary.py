from PIL import Image
import matplotlib.pyplot as plt

def convert_to_binary(image_path, threshold_value):

    img = Image.open(image_path)
    img = img.convert('L')
    

    binary_img = img.point(lambda p: 0 if p < threshold_value else 255, '1')
    
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


image_path = "test1.png"
threshold = 129  

convert_to_binary(image_path, threshold)
