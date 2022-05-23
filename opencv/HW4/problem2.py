import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("pic1.jpg")
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
plt.title("pic1")
plt.show()

# color codes
cs = ("b", "g", "r")

# plot histogram for each color
for i, col in enumerate(cs):
    hist = cv.calcHist([img], [i], None, [256], [0, 256])
    x = np.arange(256)
    plt.plot(x, hist, color=col)
    plt.title("Color Histogram")
    plt.xlabel("Bins")
    plt.ylabel("# of pixels")
plt.show()
