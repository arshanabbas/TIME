# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 11:56:27 2023

@author: arab
"""

import cv2
import numpy as np

img = cv2.imread('R:/Arshan Abbas/Images_Fabian/HIP-LMD/Mask_Images/Welle_1_Spur_1_0.png')
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Image GRAY', cv2.WINDOW_NORMAL)
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 50, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = {}".format(str(len(contours))))
print('contours {}'.format(contours[0]))

cv2.drawContours(img, contours, -1, (255, 255, 255), 2)
cv2.drawContours(imgray, contours, -1, (255, 255, 255), 2)

# counting the number of pixels
number_of_green_pix = np.sum(img[:,:,1] == 255, where=((img[:,:,0] == 0) & (img[:,:,2] == 0)))
number_of_black_pix = np.sum(img == 0)
  
print('Number of white pixels:', number_of_green_pix)
print('Number of black pixels:', number_of_black_pix)

#cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()

