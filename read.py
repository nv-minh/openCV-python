import cv2 as cv
img = cv.imread('D:\Python & DA\Computer Vision\Bk2017.jpg')


cv.imshow('picture', img)
cv.waitKey(0)

def rescaleFrame(frame, scale = 0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimension = (width, height)
    return cv.resize(frame, dimension, interpolation = cv.INTER_AREA)
img_rescale = rescaleFrame(img, scale = 2)
cv.imshow('img_rescale', img_rescale)
cv.waitKey(0)

def changeRes(width, height):
    #live video
    capture.set(3, width)
    capture.set(4, height) 

# capture = cv.VideoCapture('link')

# while True:
#     isTrue, frame = capture.read()

# frame_rescale = rescaleFrame(frame)
# cv.imshow('Video_rescale', frame_rescale)
#     cv.imshow('video', frame)
#     if cv.waitKey(20) & 0xFF == ord('q'):
#         break
# cv.release()
# cv.destroyAllWindows()
