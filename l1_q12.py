import cv2
import numpy as np
from matplotlib import pyplot as plt

# Build image
height = 256
width = 256
r1 = 158
r2 = 44
r3 = 95

img = np.zeros((height,width), np.uint8)
img[:,:] = r1
img[128:191, 128:191] = r3
img[144:175, 144:175] = r2

# Save image
cv2.imwrite('images/gray_l1q12.jpg', img)

# Build image histogram
plt.hist(img.ravel(),256,[0,256]),plt.title('Histograma do original')
plt.savefig('images/histogram_l1q12.jpg')
plt.show()

# Equalize image
equ = cv2.equalizeHist(img)
cv2.imwrite('images/equalized_l1q12.jpg', equ)

# Build equalized histogram
plt.hist(equ.ravel(),256,[0,256]),plt.title('Histograma equalizado')
plt.savefig('images/histogram2_l1q12.jpg')
plt.show()

# Displaying the images
cv2.imshow('gray', img)
cv2.imshow('equalized', equ)
cv2.waitKey(0)
cv2.destroyAllWindows()