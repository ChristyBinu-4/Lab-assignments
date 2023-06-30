#Bilinear Interpolation
import cv2 
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, floor 
import math




img = cv2.imread("2nd Sem/DIP/butterfly.png")
size = img.shape
row = size[0]
column = size[1]


enlargeScale = 2
dimension = (row*enlargeScale, column*enlargeScale)

new_image = cv2.resize(img, dimension, interpolation=cv2.INTER_LINEAR)


cv2.imshow("original",img)
cv2.waitKey(10000)


cv2.imshow("NNI", new_image)
cv2.waitKey(10000)
