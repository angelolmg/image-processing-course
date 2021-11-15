import numpy as np
import cv2
from matplotlib import pyplot as plt

img = np.zeros([9,9])
img[2:7, 2:7] = np.ones([5,5])

original = cv2.resize(img, None, fx = 20, fy = 20, interpolation = cv2.INTER_NEAREST)
horizontal = np.array([[-1,0,1],
                       [-1,0,1],
                       [-1,0,1]])

dst = abs(cv2.filter2D(img, -1, horizontal))
print(dst)
filtered = cv2.resize(dst, None, fx = 20, fy = 20, interpolation = cv2.INTER_NEAREST)

# Plot images
plt.subplot(121),plt.imshow(original, cmap='Greys_r'),plt.title('Original')
plt.subplot(122),plt.imshow(filtered, cmap='Greys_r'),plt.title('Filtered')
plt.show()

