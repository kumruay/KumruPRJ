import cv2
import numpy as np

font=cv2.FONT_HERSHEY_SIMPLEX
camera1 = cv2.VideoCapture(1)
camera2=cv2.VideoCapture(0)
human_detector=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


while True:


    ret1, frame1 = camera1.read()
    ret2, frame2 = camera2.read()

    grey1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    body1 = human_detector.detectMultiScale(grey1, 1.1, 3)
    grey2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    body2 = human_detector.detectMultiScale(grey2, 1.1, 3)

    cv2.line(frame1, (100, 500), (100, 0), (0, 255, 0), 2)
    cv2.line(frame1, (400, 500), (400, 0), (0, 255, 0), 2)
    cv2.line(frame2, (100, 500), (100, 0), (0, 255, 0), 2)
    cv2.line(frame2, (400, 500), (400, 0), (0, 255, 0), 2)


    for (x, y, w, h) in body1:
        if x>100 and x<300:
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (255, 0, 0), 2)
            break

    for (a, b, c, d) in body2:
        if a>100 and a<300:
            cv2.rectangle(frame2, (a, b), (a + c, b + d), (255, 0, 0), 2)
            break

    frameCombined = np.hstack((frame1, frame2))
    cv2.imshow("CAM", frameCombined)



    if cv2.waitKey(5) & 0xFF == ord("q"):
        camera2.release()
        camera1.release()
        cv2.destroyAllWindows()
        exit(0)
        break