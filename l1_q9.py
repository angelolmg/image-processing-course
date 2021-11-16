import cv2
import numpy as np

path = r'images/particulas.png'

img = cv2.imread(path)
img = cv2.resize(img, None, fx = 2, fy = 2, interpolation = cv2.INTER_NEAREST)

# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(_, threshold) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

width = int(img.shape[1])
height = int(img.shape[0])
print(width, height)

# Remove particles touching the border
# Right and left
img1 = np.array(threshold)
for i in range(width):
    if img1[0][i] == 255:
        cv2.floodFill(img1, None, seedPoint=(i,0), newVal=0)
    if img1[height - 1][i] == 255:
        cv2.floodFill(img1, None, seedPoint=(i,height - 1), newVal=0)

# Up and bottom
for i in range(height):
    if img1[i][0] == 255:
        cv2.floodFill(img1, None, seedPoint=(0,i), newVal=0)
    if img1[i][width - 1] == 255:
        cv2.floodFill(img1, None, seedPoint=(width - 1,i), newVal=0)

cv2.imwrite('images/particulas1.jpg', img1)

theres_white = True
max_loop = 10
curr_loop = 0
neighbour_level = 0

img2 = np.array(img1)
# Get height level of each particle
while theres_white and curr_loop < max_loop:
    curr_loop += 1
    theres_white = False

    for i in range(width):
        for j in range(height):
            if img2[j][i] == 255:
                # Check 4 conected pixels
                if (i - 1) >= 0 and img2[j][i-1] == neighbour_level or \
                (i + 1) <= width and img2[j][i+1] == neighbour_level or \
                (j - 1) >= 0 and img2[j-1][i] == neighbour_level or \
                (j + 1) <= height and img2[j+1][i] == neighbour_level: 
                    img2[j][i] = neighbour_level + 8
                    theres_white = True
    
    neighbour_level += 8

cv2.imwrite('images/particulas2.jpg', img2)

# The number of loops or final level found corresponds to the radius + 1 of each particle
print("Final tone =", neighbour_level - 8)
print("Radius =", neighbour_level/curr_loop)
print("Number of loops =", curr_loop)

img3 = np.array(img2)
thresh_factor = 1
particles = 0
# Find location of all particles and their positions
for i in range(width):
        for j in range(height):
            if img3[j][i] >= neighbour_level - 8 * thresh_factor:
                particles += 1
                img3[j][i] = 255
            else: img3[j][i] = 0

print("Number of particles =", particles)
cv2.imwrite('images/particulas3.jpg', img3)

img4 = np.array(img3)
# If certain particle has all 4 conected pixels white, its a cluster
# get its position
positions_tofill = []
for i in range(1,width-1):
    for j in range(1,height-1):
        if img4[j][i] == 255:
            four_connected = 0
            diag_connected = 0

            # Check 4 conected neighbours
            if img4[j][i-1] == 255: four_connected += 1
            if img4[j][i+1] == 255: four_connected += 1
            if img4[j-1][i] == 255: four_connected += 1
            if img4[j+1][i] == 255: four_connected += 1

            # Check diagonal conected neighbours
            if img4[j-1][i-1] == 255: diag_connected += 1
            if img4[j+1][i+1] == 255: diag_connected += 1
            if img4[j-1][i+1] == 255: diag_connected += 1
            if img4[j+1][i-1] == 255: diag_connected += 1

            # Check in neighbour filters
            if four_connected > 3 or diag_connected > 2 or (diag_connected >= 2 and four_connected > 2):
                positions_tofill.append((i,j))
                cv2.floodFill(img4, None, seedPoint=(i,j), newVal=127)       

print("Number of clusters =", len(positions_tofill))
cv2.imwrite('images/particulas4.jpg', img4)

img5 = np.array(img1)
# Fill in clusters positions in threshold image
for pos in positions_tofill:
    cv2.floodFill(img5, None, seedPoint=pos, newVal=0)       

cv2.imwrite('images/particulas5.jpg', img5)

# Displaying the images
cv2.imshow('1', img1)
cv2.imshow('2', img2)
cv2.imshow('3', img3)
cv2.imshow('4', img4)
cv2.imshow('5', img5)

cv2.waitKey(0)
cv2.destroyAllWindows()