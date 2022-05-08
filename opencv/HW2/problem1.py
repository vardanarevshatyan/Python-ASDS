import cv2 as cv

img = cv.imread("pic1.jpg")

gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


cv.imshow("pic1", img)
cv.imshow("gray", gray_img)
cv.waitKey(0)
