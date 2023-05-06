import cv2 as cv
import numpy as np

img1 = cv.imread(r"C:\Users\91703\Documents\PG docs\Lab-assignments\2nd Sem\DIP\img1.png")
img2 = cv.imread(r"C:\Users\91703\Documents\PG docs\Lab-assignments\2nd Sem\DIP\img2.jpg")

res = cv.addWeighted(img1, 0.5, img2, 0.4, 0)

cv.imshow('res', res)
cv.waitKey(0)

