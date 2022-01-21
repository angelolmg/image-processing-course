import numpy as np
from random import randrange, shuffle
import cv2 as cv

# initial pointlist variables
step = 3
jitter = 3
radius = 4

# canny variables
slider_start = 70
slider_max = 200
thresh_factor = 2

def cannyfunc(slider_val):
    global edges
    edges = cv.Canny(image=img, threshold1=slider_val, threshold2=thresh_factor*slider_val)
    cv.imshow('Canny', edges)

    # update point screen
    pointillism(1)

def pointillism(val):

    step = cv.getTrackbarPos('STEP', 'Points') 
    jitter = cv.getTrackbarPos('JITTER', 'Points')
    radius = cv.getTrackbarPos('RADIUS', 'Points')

    if step == 0: step = 1
    if jitter == 0: jitter = 1
    if radius == 0: radius = 1

    xrange = list(range(0,int(hh/step),1))
    yrange = list(range(0,int(ww/step),1))

    for i in range(len(xrange)):
        xrange[i] = int(xrange[i]*step+step/2)
    for i in range(len(yrange)):
        yrange[i] = int(yrange[i]*step+step/2)

    shuffle(xrange)
    newpoints = np.full_like(img, 255)


    for i in xrange:
        shuffle(yrange)
        for j in yrange:
            x = i + randrange(2*jitter) - jitter + 1
            y = j + randrange(2*jitter) - jitter + 1

            if  x < hh and y < ww and \
                x > 0   and y > 0:
                newpoints = cv.circle(newpoints, (y,x), radius, int(img[x,y]), -1)

    # last pass to cover the borders
    # we first get the current canny threshold
    # we use half of current radius size and jitter for painting details
    edge_thresh = cv.getTrackbarPos('Canny Lower Threshold', 'Canny')
    edges = cv.Canny(image=img, threshold1=edge_thresh, threshold2=thresh_factor*edge_thresh)
    for i in range(hh):
        for j in range(ww):
            if edges[i, j] == 255:
                x = i + randrange(jitter) - int(jitter/2) + 1
                y = j + randrange(jitter) - int(jitter/2) + 1

                if  x < hh and y < ww and \
                    x > 0   and y > 0:
                        newpoints = cv.circle(newpoints, (y,x), int(radius/2), int(img[x,y]), -1)
    
    cv.imshow('Points', newpoints)

# read input and convert to grayscale
img = cv.imread('images/biel.png', cv.IMREAD_GRAYSCALE)
hh, ww = img.shape[:2]

# Canny Edge Detection
edges = cv.Canny(image=img, threshold1=slider_start, threshold2=thresh_factor*slider_start)

# Display Canny Edge Detection Image
cv.imshow('Canny', edges)

cv.createTrackbar('Canny Lower Threshold', 'Canny', slider_start, slider_max, cannyfunc)

points = np.full_like(img, 255)

cv.imshow('Points', points)

cv.createTrackbar('STEP', 'Points', step, 10, pointillism)
cv.createTrackbar('JITTER', 'Points', jitter, 10, pointillism)
cv.createTrackbar('RADIUS', 'Points', radius, 10, pointillism)

pointillism(1)

cv.waitKey(0)
