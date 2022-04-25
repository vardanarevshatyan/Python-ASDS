import cv2 as cv

img2 = cv.imread("pic2.jpg")

width, height = img2.shape[:2]

circled_img2 = cv.circle(img2, (width // 2, height // 2), 50, (0, 255, 0), thickness=cv.FILLED)
cv.imshow("Img2", img2)
cv.imshow("Circled Img2", circled_img2)
