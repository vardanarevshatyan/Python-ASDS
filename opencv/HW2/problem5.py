import cv2 as cv
import numpy as np

# pic2 is too small for this, using pic3
img = cv.imread("pic3.jpg")
cv.imshow("pic3", img)

# translate the image to go down by 200 pixels and to the right by 50 pixels
translated = cv.warpAffine(img, np.float32([[1, 0, 50], [0, 1, 200]]), (img.shape[1], img.shape[0]))
cv.imshow("Translated", translated)

# rotate the image around its center by 50 degrees
rotated = cv.warpAffine(
    translated,
    cv.getRotationMatrix2D((translated.shape[1] // 2, translated.shape[0] // 2), 50, 1.0),
    (translated.shape[1], translated.shape[0]),
)
cv.imshow("Rotated", rotated)
# flip the image both vertically and horizontally
flipped = cv.flip(rotated, -1)
cv.imshow("Flipped", flipped)
cv.waitKey(0)
