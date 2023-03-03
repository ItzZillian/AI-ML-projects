import cv2


window = 'OpenCV_window'
cam = cv2.VideoCapture(0)
print(cam, 'is open', cam.isOpened())
while True:
    cv2.namedWindow(window)
    ready, frame = cam.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow(window, frame)
    if cv2.waitKey(1) & 0xFF == ord(' '):
        break


cv2.destroyAllWindows()
cam.release()
