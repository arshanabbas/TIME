# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 14:06:42 2023

@author: arab
"""

import cv2
import numpy as np

def calculate_pixels_between_points(image_path, point_a, point_b, color_threshold=30):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Extract the color of Point A
    color_a = hsv_image[point_a[1], point_a[0]]

    # Initialize a counter to keep track of the number of pixels between the points
    pixel_count = 0

    # Calculate the distance between Point A and Point B
    distance = int(np.sqrt((point_b[0] - point_a[0])**2 + (point_b[1] - point_a[1])**2))

    # Iterate along the line between Point A and Point B
    for t in np.linspace(0, 1, distance):
        x = int((1 - t) * point_a[0] + t * point_b[0])
        y = int((1 - t) * point_a[1] + t * point_b[1])

        # Extract the color of the current pixel
        color_b = hsv_image[y, x]

        # Calculate the color difference between Point A and the current pixel
        color_difference = np.abs(np.subtract(color_a, color_b))

        # Check if the color difference is below the color threshold
        if np.all(color_difference <= color_threshold):
            pixel_count += 1

    return pixel_count

if __name__ == "__main__":
    # Example usage:
    image_path = 'path_to_your_image.jpg'
    point_a = (x_a, y_a)  # Replace with the coordinates of Point A (e.g., (100, 200))
    point_b = (x_b, y_b)  # Replace with the coordinates of Point B (e.g., (300, 400))
    color_threshold = 30  # Adjust the color threshold as needed

    pixels_between_points = calculate_pixels_between_points(image_path, point_a, point_b, color_threshold)
    print(f"Number of pixels between Point A and Point B with similar color: {pixels_between_points}")
