import cv2 as cv
import numpy as np

img = cv.imread('Bk2017.jpg')
cv.imshow('BK', img)
# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Averaging',average)
# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian', gauss)
# Medium Blur
median = cv.medianBlur(img, 5)
cv.imshow('median', median)
# Bilateral
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilteral', bilateral)

cv.waitKey(0)