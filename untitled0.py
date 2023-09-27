# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 10:09:24 2023

@author: arab
"""

import cv2
import numpy as np

def differentiate_colors(image_path, lower_color, upper_color):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the color range to differentiate (lower and upper bounds)
    lower_bound = np.array(lower_color, dtype=np.uint8)
    upper_bound = np.array(upper_color, dtype=np.uint8)

    # Create a binary mask to isolate the specified color range
    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    # Apply the mask to the original image to extract the specific color
    color_only = cv2.bitwise_and(image, image, mask=mask)

    # Show the original image and the color-only image
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Color Only', cv2.WINDOW_NORMAL)
    cv2.imshow('Original Image', image)
    cv2.imshow('Color Only', color_only)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Example usage:
    # Specify the path to the image and the color range you want to differentiate
    image_path = 'R:/Arshan Abbas/Images_Fabian/HIP-LMD/Mask_Images/Welle_1_Spur_1_0.png'
    lower_color = [0, 255, 128]  # Lower range for the color in HSV
    upper_color = [60, 255, 128]  # Upper range for the color in HSV
    differentiate_colors(image_path, lower_color, upper_color)

"""
HSV green = 120,100,50
HSV Red = 0,100,50
"""

