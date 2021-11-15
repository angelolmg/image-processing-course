import numpy as np
import cv2
from matplotlib import pyplot as plt

img = np.zeros([9,9])
img[2:7, 2:7] = np.ones([5,5])

original = cv2.resize(img, None, fx = 20, fy = 20, interpolation = cv2.INTER_NEAREST)
gx = np.array([[-1,  -2, -1],
               [0,  0,  0],
               [1,  2,  1]])
gy = np.array([[-1,0,1],
               [-2,0,2],
               [-1,0,1]])

dst1 = cv2.filter2D(img, -1, gx)
print(dst1)
dst2 = cv2.filter2D(img, -1, gy)
print(dst2)
dst3 = abs(dst1)+abs(dst2)
print(dst3)

grad_x = abs(cv2.resize(dst1, None, fx = 20, fy = 20, interpolation = cv2.INTER_NEAREST))
grad_y = abs(cv2.resize(dst2, None, fx = 20, fy = 20, interpolation = cv2.INTER_NEAREST))
grad = cv2.resize(dst3, None, fx = 20, fy = 20, interpolation = cv2.INTER_NEAREST)

# Plot images
plt.subplot(121),plt.imshow(grad_x, cmap='Greys_r'),plt.title('Gx')
plt.subplot(122),plt.imshow(grad_y, cmap='Greys_r'),plt.title('Gy')
#plt.imshow(grad, cmap='Greys_r'),plt.title('Gx + Gy')
plt.show()

