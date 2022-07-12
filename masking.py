import cv2 as cv
import numpy as np
from numpy.lib.twodim_base import mask_indices
img = cv.imread('Bk2017.jpg')
cv.imshow('BK', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 +45, img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
masks = cv.circle(blank, (img.shape[1]//2 +45, img.shape[0]//2), 100, 255, -1)
weird_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('weird shape',weird_shape)  

cv.imshow('mask',masks)
masked = cv.bitwise_and(img,img,mask=weird_shape)
cv.imshow('masked',masked)

cv.waitKey(0)