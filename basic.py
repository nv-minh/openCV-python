import cv2 as cv

img = cv.imread('Bk2017.jpg')
cv.imshow('BK', img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

#blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# Edge Cascade
canny = cv.Canny(gray, 125, 175)
cv.imshow('Canny', canny)

#Dilating the image
dilated = cv.dilate(gray, (7, 7), iterations = 1)
cv.imshow('Dilated', dilated)

#Eroding
eroded = cv.erode(dilated, (3, 3), iterations = 1)
cv.imshow('Eroded', eroded)

#Resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)

#Cropping 
cropped = img[50:200, 200:400]
cv.imshow('Cropped',cropped)
cv.waitKey(0)