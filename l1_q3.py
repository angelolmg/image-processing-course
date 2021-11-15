import cv2
import numpy as np

def floodFill(x, y, img):
    toFill = set()
    toFill.add((x,y))
    it = 0

    while len(toFill) > 0:
        (x,y) = toFill.pop()

        if x < 0 or x > width or y < 0 or y > height:
            continue

        val = img[x][y]
        if val == 255:
            continue

        it += 1
        img[x][y] = 255
        toFill.add((x-1,y))
        toFill.add((x+1,y))
        toFill.add((x,y-1))
        toFill.add((x,y+1))

    return it

path = r'images/formas.png'

img = cv2.imread(path)

# converting image into grayscale image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

(_, threshold) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
width = int(img.shape[0])
height = int(img.shape[1])

# Remove objects touching the borders
# Right and left
img1 = np.array(threshold)
for i in range(width):
    if img1[i][0] < 255:
        cv2.floodFill(img1, None, seedPoint=(0,i), newVal=255)
    if img1[i][height - 1] < 255:
        cv2.floodFill(img1, None, seedPoint=(height - 1,i), newVal=255)

# Up and bottom
for i in range(height):
    if img1[0][i] < 255:
        cv2.floodFill(img1, None, seedPoint=(i,0), newVal=255)
    if img1[width - 1][i] < 255:
        cv2.floodFill(img1, None, seedPoint=(i,width - 1), newVal=255)

cv2.imwrite('images/formas1.jpg', img1)


# Counting objects
img2 = np.array(img1)
nobj = 0
for i in range(width):
    for j in range(height):
        if img2[i][j] == 0:
            nobj += 1
            cv2.floodFill(img2, None, seedPoint=(j, i), newVal=i)

print("Number of objects = " + str(nobj))
cv2.imwrite('images/formas2.jpg', img2)


# Counting area of the objects
img3 = np.array(img1)
obj_areas = []
obj_pos = []
for i in range(width):
    for j in range(height):
        if img3[i][j] == 0:
            area = floodFill(i, j, img3)
            obj_areas.append(area)
            obj_pos.append((i,j))
            img3[i][j] = 127

print("Positions: " + str(obj_pos))
print("Areas: " + str(obj_areas))

# using a findContours() function
img4 = np.array(img1)
img4 = cv2.resize(img4, None, fx = 4, fy = 4, interpolation = cv2.INTER_NEAREST)
contours, _ = cv2.findContours(img4, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img4 = cv2.cvtColor(img4, cv2.COLOR_GRAY2BGR)  
i = 0

# list for storing names of shapes

for contour in contours:
    # here we are ignoring first counter because 
    # findcontour function detects whole image as shape
    if i == 0:
        i = 1
        continue
  
    # cv2.approxPloyDP() function to approximate the shape
    approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
      
    # using drawContours() function
    cv2.drawContours(img4, [contour], 0, (0, 0, 255), 2)
    
    # finding center point of shape
    M = cv2.moments(contour)
    if M['m00'] != 0.0:
        x = int(M['m10']/M['m00'])
        y = int(M['m01']/M['m00'])
  
    # putting shape name at center of each shape
    if len(approx) == 3:
        cv2.putText(img4, 'Triangle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (127, 127, 127), 3)
    elif len(approx) == 4:
        cv2.putText(img4, 'Square', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (127, 127, 127), 3)
    else:
        cv2.putText(img4, 'circle', (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (127, 127, 127), 3)
    
cv2.imwrite('images/formas3.jpg', img4)

# Displaying the images
cv2.imshow('threshold', threshold)
cv2.imshow('1', img1)
cv2.imshow('2', img2)
cv2.imshow('3', img3)
cv2.imshow('4', img4)

cv2.waitKey(0)
cv2.destroyAllWindows()