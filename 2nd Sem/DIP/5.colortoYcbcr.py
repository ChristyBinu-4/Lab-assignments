import cv2 as cv
img=cv.imread("/home/christy/Documents/Myself/Academia/PG docs/Lab-assignments/2nd Sem/DIP/WM1BX.png")

imgYCC = cv.cvtColor(img, cv.COLOR_BGR2YCR_CB)

cv.imshow('result', imgYCC)
cv.imshow('Y', imgYCC[:,:,0])
cv.imshow('cb', imgYCC[:,:,1])
cv.imshow('cr', imgYCC[:,:,2])

cv.waitKey(10000)