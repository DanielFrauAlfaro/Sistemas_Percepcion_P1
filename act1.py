import cv2 as cv
import numpy as np

# sudo apt get install python3: para instalar el python3 por si acaso
# pip3 install opencv-python

img = cv.imread("balls.jpg")
img = cv.resize(img, (500,500))

img = cv.GaussianBlur(img,(31,31),0)

img2 = 255 - img[:,:,2]

aux,dst = cv.threshold(img2,170,255,cv.THRESH_BINARY)

cv.imshow("Act1", dst)
cv.waitKey(0)
