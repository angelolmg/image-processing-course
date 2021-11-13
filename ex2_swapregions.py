import cv2
import numpy as np

path = r'images/biel.png'

# Using 0 to read image in grayscale mode
img = cv2.imread(path, 0)
width = int(img.shape[0])
height = int(img.shape[1])
newimg = np.zeros((height,width), dtype = np.uint8)

half_width = int(img.shape[0]/2)
half_height = int(img.shape[1]/2)

rois = [img[0:half_height,      0:half_width],      # 1º quadrant
        img[half_height:height, 0:half_width],      # 2º quadrant
        img[0:half_height,      half_width:width],  # 3º quadrant
        img[half_height:height, half_width:width]]  # 4º quadrant

newimg[0:half_height,      0:half_width] = rois[3]     # Swap 1 and 4
newimg[half_height:height, half_width:width] = rois[0]
newimg[half_height:height, 0:half_width] = rois[2]     # Swap 2 and 3
newimg[0:half_height,      half_width:width] = rois[1]

# Displaying the image
cv2.imshow('image', newimg)
cv2.imwrite('images/swapped.jpg', newimg)

cv2.waitKey(0)
cv2.destroyAllWindows()