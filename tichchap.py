import cv2
import numpy as np
import matplotlib.pyplot as plt

def Tich_chap(img, mask):
    x, y = img.shape
    img_new = np.zeros([x, y])
    for i in range(1, x-1):
        for j in range(1, y-1):
            temp = img[i-1, j-1]*mask[0, 0] + img[i-1, j]*mask[0, 1] + img[i-1, j+1]*mask[0, 2] + img[i, j-1]*mask[1, 0] + img[i, j]*mask[1, 1] + img[i, j+1]*mask[1, 2] + img[i+1, j-1]*mask[2, 0] + img[i+1, j]*mask[2, 1] + img[i+1, j+1]*mask[2, 2]
            img_new[i,j] = temp
    img_new = img_new.astype(np.uint8)
    return img_new
    
      
img = np.array([[1,2,3],[4,5,6],[7,8,9]])
mask = np.array([[-1,0,-1],[0,0,0],[1,0,1]])
img1 = Tich_chap(img, mask)
print(img1)
                 
                
