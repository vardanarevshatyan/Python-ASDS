import cv2 as cv
import numpy as np

blank = np.zeros((400, 400), dtype="uint8")


rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), (128, 128, 128), -1)
circle = cv.circle(blank.copy(), (200, 200), 200, (128, 128, 128), -1)

# perform xor on rectangle and circle
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("bitwise_xor", bitwise_xor)


# perform bitwise or on rectangle and circle
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise_or", bitwise_or)


# draw a pink rectangle and a circle
pixel_pink = (255, 0, 255)
pink_rectangle = cv.rectangle(blank.copy(), (30, 30), (370, 370), pixel_pink, -1)
pink_circle = cv.circle(blank.copy(), (200, 200), 200, pixel_pink, -1)
bitwise_xor_pink = cv.bitwise_xor(pink_rectangle, pink_circle)
cv.imshow("bitwise_xor_pink", bitwise_xor_pink)
cv.waitKey(0)
