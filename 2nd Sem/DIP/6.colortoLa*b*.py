import numpy as np
import cv2 as cv

img = cv.imread("/home/christy/Documents/Myself/Academia/PG docs/Lab-assignments/2nd Sem/DIP/WM1BX.png")
LAB = cv.cvtColor(img, cv.COLOR_BGR2LAB)

cv.imshow('LAB',LAB)

cv.imshow('L', LAB[:,:,0])
cv.imshow('a', LAB[:,:,1])
cv.imshow('b', LAB[:,:,2])

cv.waitKey(10000)
