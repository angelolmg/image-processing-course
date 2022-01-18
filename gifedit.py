import numpy as np
import cv2
import os

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

image_folder = 'gif'
video_name = 'video.avi'

images = [img for img in os.listdir(image_folder) if img.endswith(".jpg")]
frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

l1 = height/4
l2 = 3*height/4
d = 50

mask = buildMask(l1,l2,d)
mask_inv = 1 - mask

video = cv2.VideoWriter(video_name, 0, 1, (width,height))

for image in images:
    img1 = cv2.imread(os.path.join(image_folder, image))
    img2 = cv2.GaussianBlur(img1, (17,17), 0)   # Build blured version and set it as top

    img_top = img1/255 * mask + img2/255 * mask_inv    # Update with mask

    video.write(img_top)

cv2.destroyAllWindows()
video.release()