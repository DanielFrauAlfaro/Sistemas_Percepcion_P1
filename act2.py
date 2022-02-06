import cv2 as cv
import numpy as np

img = cv.imread("balls.jpg")
img = cv.resize(img, (500,500))
img_g = cv.GaussianBlur(img,(35,35),0)

img2 = 255 - img_g[:,:,2]
aux,dst = cv.threshold(img2,170,255,cv.THRESH_BINARY)
contours,h = cv.findContours(dst,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print("Hay",len(contours),"pelotas azules")

img2 = 255 - img_g[:,:,1]
aux,dst = cv.threshold(img2,190,255,cv.THRESH_BINARY)
contours,h = cv.findContours(dst,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print("Hay",len(contours),"pelotas rojas")

img2 = 255 - img_g[:,:,0]
aux,dst = cv.threshold(img2,250,255,cv.THRESH_BINARY)
contours,h = cv.findContours(dst,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
print("Hay",len(contours),"pelotas amarillas")
