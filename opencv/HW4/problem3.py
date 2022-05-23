import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("pic1.jpg")

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("pic1")
plt.show()

# choosing a relatively low thresholding value yields better results
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
threshold, adaptive_thresh = cv.threshold(gray, 85, 255, cv.THRESH_BINARY)

plt.imshow(cv.cvtColor(adaptive_thresh, cv.COLOR_BGR2RGB))
plt.title("Thresholding Result")
plt.show()


# threshold with adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 31, 10)

plt.imshow(cv.cvtColor(adaptive_thresh, cv.COLOR_BGR2RGB))
plt.title("Adaptive Thresholding Result")
plt.show()


# threshold with gaussian thresholding
gaussian_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 31, 10)

plt.imshow(cv.cvtColor(gaussian_thresh, cv.COLOR_BGR2RGB))
plt.title("Gaussian Thresholding Result")
plt.show()
