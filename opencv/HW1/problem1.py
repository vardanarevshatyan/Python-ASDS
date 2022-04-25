import cv2 as cv

img1 = cv.imread("pic1.jpg")
img2 = cv.imread("pic2.jpg")
img3 = cv.imread("pic3.jpg")


cv.imshow("pic1", img1)
cv.imshow("pic2", img2)
cv.imshow("pic3", img3)
