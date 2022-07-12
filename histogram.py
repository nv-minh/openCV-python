import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
img = cv.imread('BK2017.jpg')
cv.imshow('BK', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)
blank = np.zeros(img.shape[:2], dtype='uint8')
mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 200, 255,-1 )
# cv.imshow('circle',circle)
# mask = cv.bitwise_and(gray, circle)
# #gray_hist = cv.calcHist([gray], [0], None, [256], [0,256])

masked = cv.bitwise_and(img, img,mask =mask)
# gray_hist = cv.calcHist([mask], [0], mask, [256], [0,256])
# cv.imshow('mask', mask)
# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# or pixel')
# #plt.plot(gray_hist)
# plt.plot(mask)
# plt.xlim([0,256])
# plt.show()

# Colour histogram
cv.imshow('mask', masked)
colours = ('b', 'g', 'r')
for i,col in enumerate(colours):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)