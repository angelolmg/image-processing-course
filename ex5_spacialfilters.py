import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

path = r'images/biel.png'
img = cv.imread(path)

# Filters
average = np.array([[0.1111,0.1111,0.1111],
                  [0.1111,0.1111,0.1111],
                  [0.1111,0.1111,0.1111]])

gauss = np.array([[0.0625,  0.125,  0.0625],
                  [0.125,   0.25,   0.125],
                  [0.0625,  0.125,  0.0625]])

horizontal = np.array([[-1,0,1],
                       [-2,0,2],
                       [-1,0,1]])
vertical = np.array([[-1,   -2, -1],
                     [0,    0,  0],
                     [1,    2,  1]])
laplacian = np.array([[0,   -1, 0],
                      [-1,  4,  -1],
                      [0,   -1, 0]])
boost = np.array([[0,   -1,     0],
                  [-1,  5.2,    -1],
                  [0,   -1,     0]])

# Default filter
curr_filter = average
title = 'Average'

# Filter selection
mode = input("Select the filter:\nAverage = a\nGauss = g\nHorizontal = h\nVertical = v\nLaplacian = l\nBoost = b\nLaplacian of Gaussian = lg\n")

if mode == 'a': 
    curr_filter = average
    title = 'Average'
elif mode == 'g':
    curr_filter = gauss
    title = 'Gaussian'
elif mode == 'h':
    curr_filter = horizontal
    title = 'Horizontal'
elif mode == 'v':
    curr_filter = vertical
    title = 'Vertical'
elif mode == 'l':
    curr_filter = laplacian
    title = 'Laplacian'
elif mode == 'b':
    curr_filter = boost
    title = 'Boost'
elif mode == 'lg':
    dst = cv.filter2D(img,-1,gauss)
    dst = cv.filter2D(dst,-1,laplacian)
    title = 'Laplacian of Gaussian'

# Apply filter
if mode != 'lg':
    dst = cv.filter2D(img,-1,curr_filter)

# Plot images
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title(title)
plt.xticks([]), plt.yticks([])
plt.show()