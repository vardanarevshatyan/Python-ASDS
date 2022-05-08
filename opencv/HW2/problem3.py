import cv2 as cv

img = cv.imread("pic2.jpg")
cv.imshow("pic2", img)
# detect edges with Canny
canny = cv.Canny(img, 125, 175)
cv.imshow("Canny", canny)
blurred = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
canny_blurred = cv.Canny(blurred, 125, 175)
cv.imshow("Blurred", canny_blurred)
cv.waitKey(0)
