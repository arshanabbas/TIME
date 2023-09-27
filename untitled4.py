# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 13:43:56 2023

@author: arab
"""

import cv2
import numpy as np

# load image
img = cv2.imread('R:/Arshan Abbas/Images_Fabian/HIP-LMD/Mask_Images/Welle_1_Spur_1_0.png')
cv2.namedWindow('mask', cv2.WINDOW_NORMAL)

# convert to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h,s,v = cv2.split(hsv)

# create mask for blue color in hsv
# blue is 240 in range 0 to 360, so for opencv it would be 120
lower = (0, 255, 128)
upper = (60, 255, 128)
mask = cv2.inRange(hsv, lower, upper)

# count non-zero pixels in mask
count=np.count_nonzero(mask)
print('count:', count)

# save output
cv2.imwrite('blue_bag_mask.png', mask)

# Display various images to see the steps
cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()