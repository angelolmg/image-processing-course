import numpy as np
import cv2

# Tiltshift function used 
def a(x, l1, l2, d):
    return 0.5*(np.tanh((x-l1)/d) - np.tanh((x-l2)/d))

def buildMask(l1, l2, d):
    # Clamp decay to avoid zero division
    if d == 0: d = 1

    # Init blank column
    mask_column = np.zeros((height, 1, 3))

    # Get results for all values
    for i in range(height):
        mask_column[i] = a(i, l1, l2, d)

    # Tile columns horizontally to build matrix
    mask = np.tile(mask_column, (1, width, 1))

    return mask


width = 640
height = 480
FPS = 30

# Setting up IP Webcam
cap = cv2.VideoCapture('http://xxx:xxx@ip/video')

# Define the codec and create VideoWriter object
#fourcc = cv2.VideoWriter_fourcc(*'mp4v') 
#out = cv2.VideoWriter('images/tiltshiftvideo.mp4', fourcc, FPS, (width, height))

#delay = int(1000/FPS)
l1 = height/4
l2 = 3*height/4
d = 50

mask = buildMask(l1,l2,d)
mask_inv = 1 - mask

while(True):
    ret, frame = cap.read()
    img1 = cv2.resize(frame, (width, height))   # Resize image
    img2 = cv2.GaussianBlur(img1, (17,17), 0)   # Build blured version and set it as top

    img_top = img1/255 * mask + img2/255 * mask_inv    # Update with mask

    #out.write(img_top)
    cv2.imshow('video', img_top)                # Display

    #cv2.waitKey(delay)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
#out.release()
cv2.destroyAllWindows()