# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 14:35:53 2023

@author: arab
"""

import cv2
import numpy as np

# Load an image
image_path = 'F:/Arshan_Abbas/Fabian/Task2/Img/Welle_1_spur_1_0.png'  # Replace with the path to your image
image = cv2.imread(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Masked Image', cv2.WINDOW_NORMAL)

# Define color ranges and replacement colors
lower_color_1 = np.array([0, 50, 50])
upper_color_1 = np.array([20, 255, 255])
replacement_color_1 = (0, 0, 255)  # Blue

lower_color_2 = np.array([100, 50, 50])
upper_color_2 = np.array([140, 255, 255])
replacement_color_2 = (255, 0, 0)  # Red

# Convert the image to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

# Create masks for each color
mask_color_1 = cv2.inRange(hsv_image, lower_color_1, upper_color_1)
mask_color_2 = cv2.inRange(hsv_image, lower_color_2, upper_color_2)

# Replace masked regions with replacement colors
image_masked = np.copy(image)
image_masked[mask_color_1 > 0] = replacement_color_1
image_masked[mask_color_2 > 0] = replacement_color_2

# Display the original and masked images
cv2.imshow('Original Image', image)
cv2.imshow('Masked Image', image_masked)
cv2.waitKey(0)
cv2.destroyAllWindows()
