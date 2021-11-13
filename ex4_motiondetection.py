import cv2
import numpy as np
from matplotlib import pyplot as plt

# Setting up IP Webcam
cap = cv2.VideoCapture('http://xxx:xxx@ip/video')

# Get first frame for reference
ret, frame = cap.read()
grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
currHist = cv2.calcHist(grayFrame, [0], None, [256], [0,256])
currCorr = 999

# Correlation threshold
thresh = 0.12

motion_count = 0

while(True):
    ret, frame = cap.read()
    cv2.namedWindow("frames", cv2.WINDOW_NORMAL)            # Create window with freedom of dimensions
    frame = cv2.resize(frame, (640, 400))                   # Resize image
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)     # Convert to grayscale

    lastHist = currHist
    currHist = cv2.calcHist(grayFrame, [0], None, [256], [0,256])
    lastCorr = currCorr
    currCorr = cv2.compareHist(lastHist, currHist, cv2.HISTCMP_CORREL)     # Correlation method
    
    # Calculate correlation score based on the last two histograms
    score = abs(currCorr - lastCorr)                        
    if score > thresh and score < 1:
        motion_count += 1
        print("MOTION DETECTED! -> " + str(motion_count))

    equ = cv2.equalizeHist(grayFrame)                       # Equalize grayscale frame
    res = np.hstack((grayFrame, equ))                       # Put frames side by side
    cv2.imshow('frames', res)                               # Display
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
