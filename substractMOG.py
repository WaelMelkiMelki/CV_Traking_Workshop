import numpy as np
import cv2

# Initialize video capture
# 0 selects the default webcam. If you have a video file, replace 0 with 'filename.mp4'
cap = cv2.VideoCapture(0)

# Initializing subtractor (MOG - Mixture of Gaussians)
# Note: This requires opencv-contrib-python
try:
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
except AttributeError:
    print("Error: cv2.bgsegm not found. Please install 'opencv-contrib-python'.")
    exit()

while(1):
    # Read frame from camera
    ret, frame = cap.read()
    
    if not ret:
        break

    # Applying background subtraction on each frame
    fgmask = fgbg.apply(frame)

    # Display the result
    cv2.imshow('Original', frame)
    cv2.imshow('MOG Foreground Mask', fgmask)

    # Exit if 'Esc' key (code 27) is pressed
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()