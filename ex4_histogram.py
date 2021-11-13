import cv2
import numpy as np
from matplotlib import pyplot as plt

path = r'images/biel.png'

# Using 0 to read image in grayscale mode
img = cv2.imread(path, 0)

# find histogram of an image
plt.hist(img.ravel(),256,[0,256])
plt.savefig('images/histogram1.jpg')
plt.show()

# creating a Histograms Equalization
# of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)

# stacking images side-by-side
res = np.hstack((img, equ))

# Displaying the image
cv2.imshow('image', res)
cv2.imwrite('images/histogram2.jpg', res)

cv2.waitKey(0)
cv2.destroyAllWindows()