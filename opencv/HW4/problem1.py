import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("pic1.jpg")

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("pic1")
plt.show()


# plot the histogram of pixel intensities
hist = cv.calcHist([gray], [0], None, [256], [0, 256]).flatten()
x = np.arange(256)

plt.plot(x, hist)
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.show()

plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("pic1")
plt.show()
