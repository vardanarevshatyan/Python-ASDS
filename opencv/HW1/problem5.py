import cv2 as cv

img2 = cv.imread("pic2.jpg")

width, height = img2.shape[:2]
img2_c = img2.copy()
circled_img2 = cv.circle(img2, (width // 2, height // 2), 50, (0, 0, 255), thickness=cv.FILLED)
cv.imshow("Img2", img2_c)
cv.imshow("Circled Img2", circled_img2)
cv.waitKey(0)
