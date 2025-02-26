import cv2
import os

image_path = "beach.jpg"
image_name = os.path.splitext(os.path.basename(image_path))[0]
image = cv2.imread(image_path)

if image is None:
    print("Error: Image not loaded properly!")
    exit()

max_width, max_height = 800, 600
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
cv2.namedWindow(image_name, cv2.WINDOW_AUTOSIZE)
cv2.imshow(image_name, image_resized)
cv2.waitKey(0)

gray_image = cv2.cvtColor(image_resized, cv2.COLOR_BGR2GRAY)
cv2.namedWindow(f"{image_name} grayscale", cv2.WINDOW_AUTOSIZE)
cv2.imshow(f"{image_name} grayscale", gray_image)
cv2.waitKey(0)

inverted_image = 255 - gray_image
cv2.namedWindow(f"{image_name} inverted", cv2.WINDOW_AUTOSIZE)
cv2.imshow(f"{image_name} inverted", inverted_image)
cv2.waitKey(0)

blurred = cv2.GaussianBlur(inverted_image, (21, 21), 0)
inverted_blurred = 255 - blurred
pencil_sketch = cv2.divide(gray_image, inverted_blurred, scale=220.0)
cv2.namedWindow(f"{image_name} sketch", cv2.WINDOW_AUTOSIZE)
cv2.imshow(f"{image_name} sketch", pencil_sketch)
cv2.waitKey(0)

cv2.destroyAllWindows()
