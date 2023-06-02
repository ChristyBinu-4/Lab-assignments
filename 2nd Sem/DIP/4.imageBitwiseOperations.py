import cv2 as cv
import numpy as np

img1 = cv.imread(r"C:\Users\91703\Documents\PG docs\Lab-assignments\2nd Sem\DIP\img1.png")
img2 = cv.imread(r"C:\Users\91703\Documents\PG docs\Lab-assignments\2nd Sem\DIP\img2.jpg")

res_and = cv.bitwise_and(img1, img2)
res_or = cv.bitwise_or(img1, img2)
res_xor = cv.bitwise_xor(img1, img2)
res_not = cv.bitwise_not(img1, img2)

cv.imshow("AND", res_and)
cv.imshow("OR", res_or)
cv.imshow("XOR", res_xor)
cv.imshow("not", res_not)

cv.waitKey(0)
