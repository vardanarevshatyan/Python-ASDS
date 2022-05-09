import cv2 as cv

img = cv.imread("pic1.jpg")
cv.imshow("pic1", img)


# convert to rgb
rgb_image = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb_image)

# convert to hsv
hsv_image = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv_image)

# convert to lab
lab_image = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab_image)

# convert to grayscale
gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray_image)

cv.waitKey(0)
