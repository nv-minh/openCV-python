import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype = 'uint8')
#cv.imshow('Blank', blank)

# 1. paint the image a certain colour
blank[0:50,0:50] = 0,0,255
#cv.imshow('Red', blank)
# 2. Draw a Rectangle
rectangle = cv.rectangle(blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness = -1)
cv.imshow('rectangle',rectangle)
# 3. Draw a  circle
cv.circle(rectangle, (blank.shape[1]//2, blank.shape[0]//2), 40, (0, 0, 255), thickness = -1)
cv.imshow('circle', rectangle)
# 4. Draw a line
cv.line(rectangle, (0, 0), (blank.shape[1]//2, blank.shape[0]//2), (215, 155, 225), thickness = 2)
cv.imshow('line',rectangle)
cv.waitKey(0)


