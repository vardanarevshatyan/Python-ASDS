import cv2 as cv

scale_factor = 0.5
img1 = cv.imread("pic1.jpg")
width, height = img1.shape[:2]
rescaled_img1 = cv.resize(img1, (int(width * scale_factor), int(height * scale_factor)))

cv.imshow("Pic1", img1)
cv.imshow("Pic1_rescaled", rescaled_img1)
cv.waitKey(0)
