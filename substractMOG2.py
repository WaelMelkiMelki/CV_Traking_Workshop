import numpy as np
import cv2

# Initialize video capture from webcam
cap = cv2.VideoCapture(0)

# Create MOG2 Background Subtractor
# Parameters you can vary (Question 5):
# history: Length of the history (default 500)
# varThreshold: Threshold on the squared Mahalanobis distance (default 16). Lower values = more false positives.
# detectShadows: If True, shadows are shown in gray (127)
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

while(1):
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the background subtractor to get the mask
    fgmask = fgbg.apply(frame)

    # Display the original frame and the mask
    cv2.imshow('Original', frame)
    cv2.imshow('MOG2 Foreground Mask', fgmask)

    # Exit on 'Esc' key
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()