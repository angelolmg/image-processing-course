import numpy as np
import cv2

# read input and convert to grayscale
img = cv2.imread('images/biel_ilum.png', cv2.IMREAD_GRAYSCALE)
hh, ww = img.shape[:2]

def homomorficFilter(val):
    newmask = np.zeros_like(img, dtype=np.float64)

    gamah = cv2.getTrackbarPos('gamaH','mask')
    gamal = cv2.getTrackbarPos('gamaL','mask')
    d0 = cv2.getTrackbarPos('d0','mask')
    c = cv2.getTrackbarPos('c','mask')

    for i in range(hh):
        for j in range (ww):
            d2 = (i - hh/2)**2 + (j - ww/2)**2
            exp = -c*(d2/(d0**2))
            fh = (gamah - gamal)*(1 - np.exp(exp)) + gamal
            newmask[i][j] = fh/100
    
    mymask = newmask

    '''
    # create black circle on white background for high pass filter
    radius = 13
    mask = np.zeros_like(img, dtype=np.float64)
    cy = mask.shape[0] // 2
    cx = mask.shape[1] // 2
    cv2.circle(mask, (cx,cy), radius, 1, -1)
    mask = 1 - mask

    # antialias mask via blurring
    mask = cv2.GaussianBlur(mask, (47,47), 0)
    '''

    # apply mask to dft_shift
    dft_shift_filtered = np.multiply(dft_shift, mymask)

    # shift origin from center to upper left corner
    back_ishift = np.fft.ifftshift(dft_shift_filtered)

    # do idft saving as complex
    img_back = np.fft.ifft2(back_ishift, axes=(0,1))

    # combine complex real and imaginary components to form (the magnitude for) the original image again
    img_back = np.abs(img_back)

    # apply exp to reverse the earlier log
    img_homomorphic = np.exp(img_back, dtype=np.float64)

    # scale result
    img_homomorphic = cv2.normalize(img_homomorphic, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)

    #cv2.imshow("gauss", mask)
    cv2.imshow("mask", mymask)
    cv2.imshow("filtered", img_back)
    cv2.imshow("homomorfic", img_homomorphic)

    # write result to disk
    #cv2.imwrite("images/ex7_mask.png", (255*mymask).astype(np.uint8))
    #cv2.imwrite("images/ex7_homomorphic.png", img_homomorphic)


# take ln of image
img_log = np.log(np.float64(img), dtype=np.float64)

# do dft saving as complex output
dft = np.fft.fft2(img_log, axes=(0,1))

# apply shift of origin to center of image
dft_shift = np.fft.fftshift(dft)

mask = np.zeros_like(img, dtype=np.float64)
cv2.imshow("mask", mask)
cv2.imshow("original", img)
cv2.imshow("filtered", img)
cv2.imshow("homomorfic", img)

cv2.createTrackbar('gamaH', 'mask', 100, 100, homomorficFilter)
cv2.createTrackbar('gamaL', 'mask', 20, 100, homomorficFilter)
cv2.createTrackbar('d0', 'mask', 100, 100, homomorficFilter)
cv2.createTrackbar('c', 'mask', 90, 100, homomorficFilter)

homomorficFilter(1)

cv2.waitKey(0)
cv2.destroyAllWindows()