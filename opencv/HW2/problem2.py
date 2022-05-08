import cv2 as cv

img = cv.imread("pic1.jpg")
# gaussian blur with (3, 3) kernel size
blurred_img1 = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
blurred_img2 = cv.GaussianBlur(img, (11, 11), cv.BORDER_DEFAULT)
cv.imshow("pic1", img)
cv.imshow("Blurred1", blurred_img1)
cv.imshow("Blurred2", blurred_img2)
cv.waitKey(0)
