import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Take first frame of the video
ret, frame = cap.read()
if not ret:
    print("Failed to read video")
    exit()

print("1. A window will open.")
print("2. Select the object with your mouse.")
print("3. Press SPACE or ENTER to start tracking.")

# 1. Select ROI
# returns (x, y, w, h) -> (top-left x, top-left y, width, height)
x, y, w, h = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select Object to Track")

# Setup the initial tracking window
track_window = (x, y, w, h)

# 2. Set up the ROI for tracking
# Note: Image slicing is [y:y+h, x:x+w]
roi = frame[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Create a mask to ignore low saturation/lightness (removes dark/white background noise)
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

# 3. Calculate the histogram of the ROI
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Setup the termination criteria
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while(1):
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # 4. Calculate Back Projection
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        
        # 5. Apply MeanShift
        ret, track_window = cv2.meanShift(dst, track_window, term_crit)
        
        # Draw the result
        x, y, w, h = track_window
        img2 = cv2.rectangle(frame, (x,y), (x+w,y+h), 255, 2)
        
        cv2.imshow('MeanShift Tracking', img2)
        
        k = cv2.waitKey(30) & 0xff
        if k == 27: # Esc key
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()