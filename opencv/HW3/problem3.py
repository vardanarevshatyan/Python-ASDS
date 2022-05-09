import cv2 as cv

img = cv.imread("pic2.jpg")
cv.imshow("pic2", img)

# average bluring
av_blur = cv.blur(img, (5, 5))
cv.imshow("av_blur", av_blur)
# bilateral bluring


# larger values for sigmacolor bring the influence of the white background and thus make everything more blurry and white
# for larger values of sigmaspace I couldn't notice any significant differences due to the simplicity of the image
bil_blur = cv.bilateralFilter(img, 5, 15, 500)
cv.imshow("bil_blur", bil_blur)
cv.waitKey(0)
