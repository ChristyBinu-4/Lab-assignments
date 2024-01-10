#5.Apply histogram equalization on an image and display the resultant image
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

path = "test1.png"
img = cv.imread(path)



equ = cv.equalizeHist(cv.cvtColor(img, cv.COLOR_BGR2GRAY))

cv.imshow("image",cv.cvtColor(img, cv.COLOR_BGR2GRAY))
cv.imshow("equalised", equ)
cv.waitKey(0)
cv.destroyAllWindows()