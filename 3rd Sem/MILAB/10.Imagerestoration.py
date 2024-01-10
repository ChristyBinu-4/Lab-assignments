#10. Implement any image restoration algorithm

import cv2
import numpy as np
import matplotlib.pyplot as plt

def wiener_filter(image, kernel, noise_var):
    # Perform Wiener deconvolution
    fft_image = np.fft.fft2(image)
    fft_kernel = np.fft.fft2(kernel, s=image.shape)
    
    # Wiener filter formula
    wiener_filter = np.conj(fft_kernel) / (np.abs(fft_kernel)**2 + noise_var)
    
    restored_image = np.fft.ifft2(fft_image * wiener_filter).real
    return np.uint8(np.clip(restored_image, 0, 255))

# Read the blurred and noisy image
image_path = "LAB\Machine ntelligence\Cycle-1\converted_image.jpg"
blurred_noisy_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Simulate a known kernel (for demonstration purposes)
kernel_size = 5
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)

# Simulate known noise variance (for demonstration purposes)
noise_var = 25.0

# Perform Wiener deconvolution
restored_image = wiener_filter(blurred_noisy_image, kernel, noise_var)

# Display the results
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(blurred_noisy_image, cmap='gray')
plt.title('Blurred and Noisy Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(kernel, cmap='gray')
plt.title('Blur Kernel')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(restored_image, cmap='gray')
plt.title('Restored Image (Wiener Filter)')
plt.axis('off')

plt.tight_layout()
plt.show()