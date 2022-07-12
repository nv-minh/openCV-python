import cv2 as cv
import numpy as np
img = cv.imread('Bk2017.jpg')

cv.imshow('BK', img)

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
canny = cv.Canny(img, 125, 155)
cv.imshow('canny edge', canny)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f"{len(contours)} contour(s) found!")
cv.drawContours(blank, contours, -1, (0, 0, 255), 3)
cv.imshow('draw contour',blank)
cv.imshow('threshold', thresh)
cv.waitKey(0)