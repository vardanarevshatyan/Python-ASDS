import cv2 as cv


def rescale_frame(frame, scale=0.75):

    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


capture = cv.VideoCapture("vid1.mp4")


while True:
    frame_loaded, frame = capture.read()

    if frame is not None:  # or if isTrue
        frame_rescaled = rescale_frame(frame, 0.5)
        cv.imshow("Video", frame)
        cv.imshow("Video_rescaled", frame_rescaled)
    else:
        print("empty frame")
        exit(1)\
    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
