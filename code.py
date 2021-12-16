import cv2 as cv
import numpy as np

img = cv.imread('Images\input3.jpg')
cv.imshow('palm image',img)
cv.waitKey()

hsvim = cv.cvtColor(img, cv.COLOR_BGR2HSV)
lower = np.array([0, 40, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")
skinRegionHSV = cv.inRange(hsvim, lower, upper)
blurred = cv.blur(skinRegionHSV, (2,2))
ret,thresh = cv.threshold(blurred,0,255,cv.THRESH_BINARY)
cv.imshow("thresh", thresh)
cv.waitKey()
cv.imwrite(r'Images\thresh.jpg', thresh)
