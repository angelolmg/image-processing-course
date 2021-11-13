import cv2

# Coordinates of negative block
px1 = int(input("Px1 = "))
py1 = int(input("Py1 = "))
px2 = int(input("Px2 = "))
py2 = int(input("Py2 = "))

path = r'images/biel.png'

# Using 0 to read image in grayscale mode
img = cv2.imread(path, 0)

for i in range(px1, px2):
    for j in range(py1, py2):
        img[i][j] = 255 - img[i][j]

# Displaying the image
cv2.imshow('image', img)
cv2.imwrite('images/negative.jpg', img)

cv2.waitKey(0)
cv2.destroyAllWindows()