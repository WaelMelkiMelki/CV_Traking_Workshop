import numpy as np
import cv2

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize GMG Background Subtractor
# initializationFrames: number of frames used to learn the background (default 120)
# decisionThreshold: threshold for Bayesian decision (default 0.8)
try:
    fgbg = cv2.bgsegm.createBackgroundSubtractorGMG(initializationFrames=120, decisionThreshold=0.8)
except AttributeError:
    print("Error: cv2.bgsegm not found. Please install 'opencv-contrib-python'.")
    exit()

print("Starting GMG... Please wait a few seconds for background learning (approx 120 frames).")

while(1):
    ret, frame = cap.read()
    if not ret:
        break

    # Apply the background subtractor
    fgmask = fgbg.apply(frame)

    # GMG often produces noise, it is recommended to apply morphological opening (optional here, but good practice)
    # kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    # fgmask = cv2.morphologyEx(fgmask, cv2.MORPH_OPEN, kernel)

    cv2.imshow('Original', frame)
    cv2.imshow('GMG Foreground Mask', fgmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()