import cv2
import os

# Configuration
image_path = "beach.jpg"
max_width, max_height = 800, 600
sketch_intensity = 220.0  # Adjustable sketch intensity (higher = darker sketch)

# Load image
image = cv2.imread(image_path)

if image is None:
    print(f"Error: Unable to load image '{image_path}'")
    print("Please ensure the image file exists in the current directory.")
    exit()

# Extract image name for window titles
image_name = os.path.splitext(os.path.basename(image_path))[0]

# Resize image while maintaining aspect ratio
h, w = image.shape[:2]
aspect_ratio = w / h

if w > max_width or h > max_height:
    if w > h:
        new_w = max_width
        new_h = int(new_w / aspect_ratio)
    else:
        new_h = max_height
        new_w = int(new_h * aspect_ratio)
else:
    new_w, new_h = w, h

image_resized = cv2.resize(image, (new_w, new_h))

# Display original image
cv2.namedWindow(image_name, cv2.WINDOW_AUTOSIZE)
cv2.imshow(image_name, image_resized)
cv2.waitKey(0)

# Step 1: Convert to grayscale
gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
cv2.namedWindow(f"{image_name} - Grayscale", cv2.WINDOW_AUTOSIZE)
cv2.imshow(f"{image_name} - Grayscale", gray_image)
cv2.waitKey(0)

# Step 2: Invert grayscale image
inverted_image = 255 - gray_image
cv2.namedWindow(f"{image_name} - Inverted", cv2.WINDOW_AUTOSIZE)
cv2.imshow(f"{image_name} - Inverted", inverted_image)
cv2.waitKey(0)

# Step 3: Apply Gaussian blur and create pencil sketch
blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=sketch_intensity)

# Display final pencil sketch
cv2.namedWindow(f"{image_name} - Pencil Sketch", cv2.WINDOW_AUTOSIZE)
cv2.imshow(f"{image_name} - Pencil Sketch", pencil_sketch)
cv2.waitKey(0)

cv2.destroyAllWindows()

print(f"Sketch conversion completed successfully for '{image_name}'!")
