from random import randint
import numpy as np
import cv2 as cv

nclusters = 8
attempts = 1

img = cv.imread('images/sushi.jpg')
image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
#img = cv.resize(img, (0,0), fx=0.5, fy=0.5) 
samples = img.reshape((-1,3))

# convert to np.float32
samples = np.float32(samples)

# define criteria, number of clusters and apply kmeans()
# out -> labels: the classification of each pixel
# out -> centers: RGB value class of each cluster
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 10000, 0.0001)
_, labels, centers = cv.kmeans(samples, nclusters, None, criteria, attempts, cv.KMEANS_RANDOM_CENTERS)

# Now convert back into uint8, and make the original image
centers = np.uint8(centers)
#centers[1:]= [255, 255, 255]
vals = centers[labels.flatten()]
newimg = vals.reshape((img.shape))

cv.imshow('New Image', newimg)

#cv.imwrite("images/ex9_k8_" + str(randint(0,10000)) + ".jpg", newimg)

cv.waitKey(0)
cv.destroyAllWindows()