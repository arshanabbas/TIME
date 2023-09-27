from PIL import Image

# Open the image
image_path = 'F:/Arshan_Abbas/Fabian/Task2/Img/Welle_1_spur_1_0.png'  # Replace with the path to your image
image = Image.open(image_path)

# Define the coordinates of point A and point B
point_a = (100, 100)  # Replace with the (x, y) coordinates of point A
point_b = (100, 300)  # Replace with the (x, y) coordinates of point B

# Ensure point_a is above point_b
if point_a[1] > point_b[1]:
    point_a, point_b = point_b, point_a

# Width of each vertical line
line_width = 1  # This represents the width of the vertical line (1 pixel)

# Initialize variables to keep track of total pixels
total_pixels = 0

# Iterate through vertical lines from point A to point B
x = point_a[0]
while x <= point_b[0]:
    # Extract a vertical line region
    y = point_a[1]
    height = point_b[1] - point_a[1]
    vertical_line_region = image.crop((x, y, x + line_width, y + height))

    # Get the dimensions (width and height) of the cropped vertical line
    line_height = vertical_line_region.size[1]

    # Add the pixel count of this vertical line to the total
    total_pixels += line_height

    # Move to the next vertical line
    x += line_width

print(f"Total number of pixels along the vertical lines from point A to point B: {total_pixels}")
