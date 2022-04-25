import cv2 as cv

capture = cv.VideoCapture("vid1.mp4")

while True:
    frame_loaded, frame = capture.read()
    if frame_loaded:
        cv.imshow("Video", frame)
    else:
        print("empty frame")
        exit(1)

    if cv.waitKey(20) & 0xFF == ord("d"):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
