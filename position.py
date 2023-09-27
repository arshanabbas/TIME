# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:00:37 2023

@author: arab
"""

import cv2
import numpy as np
from PIL import Image

# Load an image
image_path = 'F:/Arshan_Abbas/Fabian/Task2/Img/Welle_1_spur_1_0.png'  # Replace with the path to your image
image = cv2.imread(image_path)
image_open = Image.open(image_path)
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert BGR to RGB
cv2.namedWindow('Image with Dot', cv2.WINDOW_NORMAL)

# Define the position and color of the dot
#dot_position = (1, 1000)  # (x, y) coordinates of the dot
start_point = (100, 950)
end_point = (100, 1250)
dot_color = (255, 255, 255)     # Color of the dot (in RGB)

# Get the dimensions (width and height) of the image
width, height = image_open.size

# Calculate the total number of pixels in width and height
total_pixels_width = width
total_pixels_height = height

# Draw the dot on a copy of the image
image_with_dot = np.copy(image)
cv2.rectangle(image_with_dot, start_point, end_point, color=dot_color, thickness=10)

print(f"Width of the image: {width} pixels")
print(f"Height of the image: {height} pixels")

# Display the image with the dot
cv2.imshow('Image with Dot', image_with_dot)
cv2.waitKey(0)
cv2.destroyAllWindows()
