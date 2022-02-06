import cv2
import numpy as np

# sudo apt get install python3: para instalar el python3 por si acaso
# pip3 install opencv-python

img = cv2.imread("balls.jpg")
img = cv2.resize(img, (500,500))

img = cv2.GaussianBlur(img,(31,31),0)

img2 = 255 - img[:,:,2]

aux,dst = cv2.threshold(img2,170,255,cv2.THRESH_BINARY)

cv2.imshow("Act1", dst)
#cv.waitKey(0)
