import numpy as np
import cv2 as cv

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

def take_screnshoot(val):
    s = cv.getTrackbarPos('Screenshot','image')
    if s == 1:
        cv.imwrite('images/tiltshift.jpg', img_top*255)

def on_change(top):
    global img_top

    # Get current mask values
    # Use it to build updated mask and inverse
    focus_height = cv.getTrackbarPos('Focus','mask') * height/100
    center_position = cv.getTrackbarPos('Center','mask') * height/100
    decay = cv.getTrackbarPos('Decay','mask')
    
    l1 = center_position + focus_height/2
    l2 = center_position - focus_height/2
    #print(l1, l2, decay)

    mask = buildMask(l2, l1, decay)
    #print(mask.shape)
    mask_inv = 1 - mask

    # Build final composition with images and masks
    img_top = img1/255 * mask + img2/255 * mask_inv

    # Display both
    cv.imshow('mask', mask)
    cv.imshow('image', img_top)
    #cv.imwrite('images/tiltshiftmask1.jpg', mask*255)
    #cv.imwrite('images/tiltshiftmask2.jpg', mask_inv*255)
    
# Read main image
img1 = cv.imread(r'images/cars.jpg')

# Build blured version and set it as top
img2 = cv.GaussianBlur(img1, (17,17), 0)
img_top = np.array(img2)

height = int(img1.shape[0])
width = int(img1.shape[1])

cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.namedWindow('mask', cv.WINDOW_NORMAL)
cv.imshow('image', img_top)

# Create mask sliders
cv.createTrackbar('Focus', 'mask', 50, 100, on_change)
cv.createTrackbar('Decay', 'mask', 50, 100, on_change)
cv.createTrackbar('Center', 'mask', 50, 100, on_change)
cv.createTrackbar('Screenshot', 'mask', 0, 1, take_screnshoot)

# Initial update
on_change(0)

cv.waitKey(0)
cv.destroyAllWindows()