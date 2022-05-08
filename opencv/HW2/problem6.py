import cv2 as cv
import numpy as np

img = cv.imread("pic3.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (5, 5), cv.BORDER_DEFAULT)
canny = cv.Canny(img, 100, 200)
canny_gray = cv.Canny(blur, 125, 175)

# find the contours
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours_gray, hierarchies_gray = cv.findContours(canny_gray, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
# draw contours on the image
blank = np.zeros(img.shape, dtype="uint8")
blank_gray = np.zeros(img.shape, dtype="uint8")
cv.drawContours(blank_gray, contours_gray, -1, (0, 0, 255), 1)
cv.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv.imshow("contours drawn on grayscale", blank_gray)
cv.imshow("contours drawn original", blank)
cv.waitKey(0)
