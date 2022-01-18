import cv2
import numpy as np
from matplotlib import pyplot as plt

path = r'images/poligono.png'

img = cv2.imread(path)
#img = cv2.resize(img, None, fx = 2, fy = 2, interpolation = cv2.INTER_NEAREST)

# Converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
(_, threshold) = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
width = int(img.shape[1])
height = int(img.shape[0])

# Filters
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

diag = np.array([[-2,   -1, 0],
                 [-1,  0,  1],
                 [0,   1, 2]])

diag2 = np.array([[0,   -1, -2],
                 [1,  0,  -1],
                 [2,   1, 0]])
# Applying filters
img_horiz = np.array(threshold) 
img_horiz = cv2.filter2D(img_horiz,-1,horizontal)

img_vert = np.array(threshold) 
img_vert = cv2.filter2D(img_vert,-1,vertical)

img_diag = np.array(threshold) 
img_diag = cv2.filter2D(img_diag,-1,diag2)

img_laplacian = np.array(threshold) 
img_laplacian = cv2.filter2D(img_laplacian,-1,laplacian)

img_lapgauss = np.array(threshold) 
img_lapgauss = cv2.filter2D(img_lapgauss,-1,gauss)
img_lapgauss = cv2.filter2D(img_lapgauss,-1,laplacian)

# Displaying the images
cv2.imshow('polygon', np.where((255 - threshold) < 128, 255, threshold+128))
cv2.imshow('horizontal', np.where((255 - img_horiz) < 128, 255, img_horiz+128))
cv2.imshow('vertical', np.where((255 - img_vert) < 128, 255, img_vert+128))
cv2.imshow('diagonal', np.where((255 - img_diag) < 128, 255, img_diag+128))
cv2.imshow('laplacian', np.where((255 - img_laplacian) < 128, 255, img_laplacian+128))
cv2.imshow('lapgauss', np.where((255 - img_lapgauss) < 128, 255, img_lapgauss+128))

cv2.waitKey(0)
cv2.destroyAllWindows()