import numpy as np
import cv2 as cv

img = cv.imread("/home/christy/Documents/Myself/Academia/PG docs/Lab-assignments/2nd Sem/DIP/WM1BX.png")

LUV = cv.cvtColor(img, cv.COLOR_BGR2LUV)
cv.imshow('LAB',LUV)

cv.imshow('L', LUV[:,:,0])
cv.imshow('U', LUV[:,:,1])
cv.imshow('V', LUV[:,:,2])

cv.waitKey(10000)
