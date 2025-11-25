import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Using MOG2 as the base subtractor
fgbg = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=False)

while(1):
    ret, frame = cap.read()
    if not ret:
        break

    # 1. Get the raw mask
    raw_mask = fgbg.apply(frame)

    # 2. Define the kernel (structure element)
    # A 5x5 matrix of 1s. Larger kernel = stronger effect.
    kernel = np.ones((5,5), np.uint8)

    # 3. Apply Morphological Opening (Erosion followed by Dilation)
    # This removes small white noise from the background
    clean_mask = cv2.morphologyEx(raw_mask, cv2.MORPH_OPEN, kernel)

    # Optional: Apply Closing to fill holes inside the detected object
    # clean_mask = cv2.morphologyEx(clean_mask, cv2.MORPH_CLOSE, kernel)

    # Display results
    cv2.imshow('Original', frame)
    cv2.imshow('Raw Mask (Noisy)', raw_mask)
    cv2.imshow('Clean Mask (Morphology)', clean_mask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()