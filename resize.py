import numpy as np
import cv2
import matplotlib as plt

img = cv2.imread('1.jpg')
(h, w, d) = img.shape
print("width={}, height={}, depth={}".format(w, h, d))
scale_percent = 120 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
A = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',A.shape)
 
cv2.imshow("Resized image", A)
cv2.waitKey(0)
cv2.destroyAllWindows()