import numpy as np
import cv2

cap = cv2.VideoCapture(0)

# Take first frame
ret, frame = cap.read()
if not ret:
    print("Failed to read video")
    exit()

print("1. Select the object with your mouse.")
print("2. Press SPACE or ENTER to start tracking.")

# 1. Select ROI
x, y, w, h = cv2.selectROI("Select Object to Track", frame, fromCenter=False, showCrosshair=True)
cv2.destroyWindow("Select Object to Track")

track_window = (x, y, w, h)

# 2. Set up the ROI for tracking
roi = frame[y:y+h, x:x+w]
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# Mask out low saturation/lightness
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))

# 3. Calculate Histogram
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

# Termination criteria
term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)

while(1):
    ret, frame = cap.read()
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # 4. Calculate Back Projection
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        
        # 5. Apply CamShift
        # rect returns ((center_x, center_y), (width, height), angle)
        rect, track_window = cv2.CamShift(dst, track_window, term_crit)
        
        # 6. Draw the rotated rectangle
        pts = cv2.boxPoints(rect)
        # FIX: Use np.int32 instead of np.int0
        pts = np.int32(pts) 
        img2 = cv2.polylines(frame, [pts], True, 255, 2)
        
        cv2.imshow('CamShift Tracking', img2)
        
        k = cv2.waitKey(30) & 0xff
        if k == 27: # Esc
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()