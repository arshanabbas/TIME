# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 12:01:30 2023

@author: arab
"""

import cv2
import numpy as np


# Load an image
image_path = 'G:/F/Work/TIME/Fabian/Task3/Images/1.jpg'  # Replace with the path to your image
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
#cv2.namedWindow('Color 1 Regions', cv2.WINDOW_NORMAL)
#cv2.namedWindow('Color 2 Regions', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color 3 Regions', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color 4 Regions', cv2.WINDOW_NORMAL)
#cv2.namedWindow('Color 5 Regions', cv2.WINDOW_NORMAL)
cv2.namedWindow('Color 6 Regions', cv2.WINDOW_NORMAL)

# Define color ranges for your two colors (in HSV)
lower_color_1 = np.array([100, 80, 30])
upper_color_1 = np.array([140, 255, 255])

lower_color_2 = np.array([0, 80, 30])
upper_color_2 = np.array([20, 255, 255])

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# Create masks for each color
mask_color_1 = cv2.inRange(hsv_image, lower_color_1, upper_color_1)
mask_color_2 = cv2.inRange(hsv_image, lower_color_2, upper_color_2)

#replace mask color
replacement_color_2 = (0, 0, 255)  # Blue
image_masked = np.copy(image)
image_masked[mask_color_1 > 0] = replacement_color_1

# Apply masks to the original image
color_1_regions = cv2.bitwise_not(image, image, mask=mask_color_1)
color_2_regions = cv2.bitwise_or(image, image, mask=mask_color_2)

# Display the results
#cv2.imshow('Color 1 Regions', color_1_regions)
#cv2.imshow('Color 2 Regions', color_2_regions)
cv2.imshow('Color 3 Regions', image)
cv2.imshow('Color 4 Regions', mask_color_1)
#cv2.imshow('Color 5 Regions', mask_color_2)
cv2.imshow('Color 6 Regions', image_masked)
cv2.waitKey(0)
cv2.destroyAllWindows()