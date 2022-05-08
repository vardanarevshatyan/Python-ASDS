import cv2 as cv

img1 = cv.imread("pic1.jpg")
img1_c = img1.copy()
width, height = img1.shape[:2]
# Draw a line starting from the left lower corner and ending in the right upper corner of the image
# pic1.jpg.
line_img1 = cv.line(img1, (0, width), (height, 0), (0, 255, 0), thickness=2)

cv.imshow("Img1", img1_c)
cv.imshow("Line", line_img1)
cv.waitKey(0)
