import numpy as np
import cv2



#import time

font=cv2.FONT_HERSHEY_SIMPLEX
#dtav=0

video_capture_0=cv2.VideoCapture(0)
video_capture_1=cv2.VideoCapture(1)

#startTime=time.time()

while True:
##try  expect

    ret,frame0=video_capture_0.read()
    ret,frame1= video_capture_1.read()

    #frame1=cv2.resize(frame1,(320,480))
    frameCombined=np.hstack((frame0,frame1))

    cv2.imshow("Cam",frameCombined)





    if cv2.waitKey(1) & 0xFF == ord("q"):
        break





video_capture_0.release()
video_capture_1.release()
cv2.destroyAllWindows()