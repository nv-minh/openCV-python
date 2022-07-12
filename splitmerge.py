import cv2 as cv
import numpy as np

img = cv.imread('Bk2017.jpg')
cv.imshow('BK', img)
blank = np.zeros(img.shape[:2], dtype = 'uint8')
b, g, r = cv.split(img)
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('blue_', blue)
cv.imshow('green_', green)
cv.imshow('red_', red)


print(b.shape)
print(g.shape)
print(r.shape)
cv.imshow('blue', b)
cv.imshow('green', g)
cv.imshow('red',r)
merger = cv.merge([b, g, r])
cv.imshow('merge',merger)

cv.waitKey(0)