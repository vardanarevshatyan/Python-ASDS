import cv2 as cv
import numpy as np

img = cv.imread("pic1.jpg")

# separate channels
b, g, r = cv.split(img)

# blank for the image
blank = np.zeros(img.shape[:2], np.uint8)

# show channels as grayscale
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)


# merge  with blank
merged_b = cv.merge((b, blank, blank))
merged_g = cv.merge((blank, g, blank))
merged_r = cv.merge((blank, blank, r))

cv.imshow("merged_b", merged_b)
cv.imshow("merged_g", merged_g)
cv.imshow("merged_r", merged_r)

cv.waitKey(0)
