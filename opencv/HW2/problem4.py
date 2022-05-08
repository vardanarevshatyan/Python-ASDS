import cv2 as cv

img = cv.imread("pic2.jpg")
height, width = img.shape[:2]
cv.imshow("pic2", img)
# resize x2 width and same height, interpolate inter_area
resize1 = cv.resize(img, (width * 2, height), interpolation=cv.INTER_AREA)
# 2 times smaller height and the same width, interpolate inter_cubic
resize2 = cv.resize(img, (width, height // 2), interpolation=cv.INTER_CUBIC)
# show resized versions
cv.imshow("Resize1", resize1)
cv.imshow("Resize2", resize2)
cv.waitKey(0)
