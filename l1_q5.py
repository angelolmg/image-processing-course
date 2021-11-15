import numpy as np
import cv2
from matplotlib import pyplot as plt

img = np.array([[0,  5, 7, 7, 5, 8, 7, 8],
                [7,  2, 6, 2, 6, 5, 6, 8],
                [6,  9, 7, 7, 0, 7, 2, 7],
                [6,  6, 1, 7, 6, 7, 7, 5],
                [9,  6, 0, 7, 8, 2, 6, 7],
                [2,  8, 8, 2, 7, 6, 7, 8],
                [7,  3, 2, 6, 1, 7, 5, 8],
                [9,  9, 5, 6, 7, 7, 7, 7]])

original = cv2.resize(img.astype(np.uint8), None, fx = 30, fy = 30, interpolation = cv2.INTER_NEAREST)

# Plot original
cv2.imshow('Original', original)
cv2.imwrite('images/original_l1q5.jpg', original)

# find histogram of an image
plt.hist(img.ravel(),256,[0,255]),plt.title('Histograma do original')
plt.savefig('images/histogram_l1q5.jpg')
plt.show()

# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
img2 = cv2.equalizeHist(img.astype(np.uint8))
equalized = cv2.resize(img2, None, fx = 30, fy = 30, interpolation = cv2.INTER_NEAREST)

cv2.imshow('Equalizado', equalized)
cv2.imwrite('images/equalization_l1q5.jpg', equalized)

# find histogram of an image
plt.hist(img2.ravel(),256,[0,255]),plt.title('Histograma do equalizado')
plt.savefig('images/histogram2_l1q5.jpg')
plt.show()



