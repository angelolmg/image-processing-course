import cv2
import numpy as np
from matplotlib import pyplot as plt

height = 80
width = 80

# Build first image
img1 = np.zeros((height,width), np.uint8)
img1[:, :width//2] = 255
cv2.imwrite('images/a_l1q13.jpg', img1)

# Build second image
img2 = np.zeros((height,width), np.uint8)
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0: color = 255
        else: color = 0
        img2[j*height//8:(j+1)*height//8, i*width//8:(i+1)*width//8] = color
cv2.imwrite('images/b_l1q13.jpg', img2)

# Filters
average = np.array([[0.1111,0.1111,0.1111],
                  [0.1111,0.1111,0.1111],
                  [0.1111,0.1111,0.1111]])

dst1 = cv2.filter2D(img1,-1,average)
dst2 = cv2.filter2D(img2,-1,average)

res1 = np.hstack((img1, dst1))
res2 = np.hstack((img2, dst2))

cv2.imwrite('images/a2_l1q13.jpg', res1)
cv2.imwrite('images/b2_l1q13.jpg', res2)

# Histograms
plt.hist(img1.ravel(),256,[0,256]),plt.title('Histograma (a) original')
plt.savefig('images/histogram_a1_l1q13.jpg')
plt.show()
plt.hist(dst1.ravel(),256,[0,256]),plt.title('Histograma (a) borrado')
plt.savefig('images/histogram_a2_l1q13.jpg')
plt.show()

plt.hist(img2.ravel(),256,[0,256]),plt.title('Histograma (b) original')
plt.savefig('images/histogram_b1_l1q13.jpg')
plt.show()
plt.hist(dst2.ravel(),256,[0,256]),plt.title('Histograma (b) borrado')
plt.savefig('images/histogram_b2_l1q13.jpg')
plt.show()

# Displaying the images
cv2.imshow('1', res1)
cv2.imshow('2', res2)
cv2.waitKey(0)
cv2.destroyAllWindows()