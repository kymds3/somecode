# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2
img = cv2.imread("C:\comp9517\DataSamples\s2.jpg")
#img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
Size = img.shape# shape: (1024,393,3)
high = int(Size[0]/3)# 341
width = Size[1]# 393
img1 = img[:341,:393]
img2 = img[341:682,:393]
img3 = img[682:1023,:393]
b = img1[:,:,0]
g = img2[:,:,1]
r = img3[:,:,2]
#cv2.imshow('blue',b)
#cv2.waitKey(0)
imgf = cv2.merge((b,g,r))
cv2.imshow('Image',imgf)
cv2.waitKey(0)