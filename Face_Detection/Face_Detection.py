import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer

import cv2
import numpy as np
from ui_main_window import *


font=cv2.FONT_HERSHEY_SIMPLEX
camera1=cv2.VideoCapture(0)
camera2=cv2.VideoCapture(1)

human_detector=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")  #Yüz görüntüsünü algılamak için gerekli datalar.


while True:
    try:  #Esas kod.

        ret1,frame1=camera1.read()
        ret2,frame2=camera2.read()
        frameCombined=np.hstack((frame1,frame2))
        grey=cv2.cvtColor(frameCombined,cv2.COLOR_BGR2GRAY)
        body=human_detector.detectMultiScale(grey,1.1,3)

        for(x,y,w,h) in body:


            cv2.rectangle(frameCombined,(x,y),(x+w,y+h),(255,0,0),3)

            cv2.imshow("CAM",frameCombined)

    except:  #Problem durumunda çağırılacak kod.


        ret2,frame2=camera2.read()

        grey=cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)
        body=human_detector.detectMultiScale(grey,1.1,3)

        for(x,y,w,h) in body:

            cv2.rectangle(frame2,(x,y),(x+w,y+h),(255,0,0),3)
            cv2.imshow("CAM",frame2)

        if cv2.waitKey(5) & 0xFF == ord("q"):

            camera2.release()
            cv2.destroyAllWindows()
            exit(1)
            break









    if cv2.waitKey(5) & 0xFF==ord("q"):
        camera1.release()
        camera2.release()
        cv2.destroyAllWindows()
        exit(0)

        break



