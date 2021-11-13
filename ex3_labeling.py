# Counting circles and holes in a binary image

# The current algorithm is limited to labeling only 255 different objects
# One way to increase this number would be to use RGB
# That way we would have 255*255*255 labels to use

import cv2

path = r'images/bolhas.png'

# Using 0 to read image in grayscale mode
img = cv2.imread(path, 0)
width = int(img.shape[0])
height = int(img.shape[1])

# Remove objects touching the borders
# Right and left
for i in range(width):
    if img[i][0] == 255:
        cv2.floodFill(img, None, seedPoint=(0,i), newVal=0)
    if img[i][height - 1] == 255:
        cv2.floodFill(img, None, seedPoint=(height - 1,i), newVal=0)

# Up and bottom
for i in range(height):
    if img[0][i] == 255:
        cv2.floodFill(img, None, seedPoint=(i,0), newVal=0)
    if img[width - 1][i] == 255:
        cv2.floodFill(img, None, seedPoint=(i,width - 1), newVal=0)

cv2.imwrite('images/labeling1.jpg', img)

# Counting objects
nobj = 0
for i in range(width):
    for j in range(height):
        if img[i][j] == 255:
            nobj += 1
            cv2.floodFill(img, None, seedPoint=(j, i), newVal=nobj)

print("Number of objects = " + str(nobj))
cv2.imwrite('images/labeling2.jpg', img)

# Changing background color
cv2.floodFill(img, None, seedPoint=(0, 0), newVal=255)
cv2.imwrite('images/labeling3.jpg', img)

# Counting number of objects with holes
nobj_wh = 0
current_obj = (0,0)
for i in range(width):
    for j in range(height):
        if img[i][j] != 255:
            if img[i][j] == 0:
                nobj_wh += 1
            cv2.floodFill(img, None, seedPoint=(j, i), newVal=255)

print("Number of objects with holes = " + str(nobj_wh))

# Displaying the image
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()