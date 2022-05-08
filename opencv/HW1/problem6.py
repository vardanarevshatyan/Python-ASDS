import cv2 as cv

pic2 = cv.imread("pic2.jpg")
width, height = pic2.shape[:2]
pic2_c = pic2.copy()
# draw orange rectangle in the middle pic2
rectangle_pic2 = cv.rectangle(pic2, (width // 2, height // 2), (width, height), (0, 165, 255), thickness=cv.FILLED)

cv.imshow("Original", pic2_c)
cv.imshow("Rectangle", rectangle_pic2)
cv.waitKey(0)
