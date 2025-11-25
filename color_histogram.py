import cv2
import numpy as np
from matplotlib import pyplot as plt

# Try to load an image from file
image_path = 'test_image.jpg'
img = cv2.imread(image_path)

# If image not found, capture one from webcam
if img is None:
    print(f"Could not find {image_path}, capturing a frame from webcam...")
    cap = cv2.VideoCapture(0)
    ret, img = cap.read()
    cap.release()
    if not ret:
        print("Failed to capture image.")
        exit()
    print("Image captured.")

# Display the chosen image
cv2.imshow('Target Image', img)

# Calculate and plot histogram for each channel (Blue, Green, Red)
colors = ('b', 'g', 'r')
plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins (Pixel Value)")
plt.ylabel("# of Pixels")

for i, color in enumerate(colors):
    # cv2.calcHist(images, channels, mask, histSize, ranges)
    # channels: [0]=Blue, [1]=Green, [2]=Red
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

print("Close the plot window to finish the script.")
plt.show()

cv2.destroyAllWindows()