import cv2 as cv

pic2 = cv.imread("pic2.jpg")
width, height = pic2.shape[:2]
# draw orange rectangle in the middle pic2
rectangle_pic2 = cv.rectangle(pic2, (width // 2, height // 2), (width, height), (0, 255, 0), thickness=cv.FILLED)
)

cv.imshow('Original', pic2)
cv.imshow("Rectangle", rectangle_pic2)
