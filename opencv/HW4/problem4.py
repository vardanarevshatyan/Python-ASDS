import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("pic2.jpg")
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

plt.title("pic2")
plt.show()

# grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# apply gaussian blur to smooth out the image
blur = cv.GaussianBlur(gray, (5, 5), 0)
plt.imshow(cv.cvtColor(blur, cv.COLOR_BGR2RGB))


# apply sobel operator and use weighting before combining
sobelx = cv.Sobel(blur, cv.CV_64F, 1, 0, ksize=5)
sobely = cv.Sobel(blur, cv.CV_64F, 0, 1, ksize=5)

sobelx = cv.convertScaleAbs(sobelx)
sobely = cv.convertScaleAbs(sobely)
combined_sobel = cv.bitwise_or(sobelx, sobely)
combined_sobel_weighted = cv.addWeighted(sobelx, 0.7, sobely, 0.3, 0.1)

plt.imshow(cv.cvtColor(combined_sobel, cv.COLOR_BGR2RGB))
plt.title("Sobel(Basic) Edge Detection")
plt.show()

plt.imshow(cv.cvtColor(combined_sobel_weighted, cv.COLOR_BGR2RGB))
plt.title("Sobel(Weighted) Edge Detection")
plt.show()
