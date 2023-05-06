import cv2 as cv
img=cv.imread(r"C:\Users\91703\Documents\PG docs\Lab-assignments\2nd Sem\DIP\rgb.png")


b,g,r=cv.split(img)
cv.imshow("Red",r)
cv.imshow("Green",g)
cv.imshow("Blue",b)
cv.waitKey(0)