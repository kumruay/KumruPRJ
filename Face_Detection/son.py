import cv2
import numpy as np
import serial

ser = serial.Serial('COM3', 9600)

font=cv2.FONT_HERSHEY_SIMPLEX
camera1=cv2.VideoCapture(0)
camera2=cv2.VideoCapture(1)

human_detector=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


while True:
    try:

        ret1,frame1=camera1.read()
        ret2,frame2=camera2.read()
        frameCombined=np.hstack((frame1,frame2))
        grey=cv2.cvtColor(frameCombined,cv2.COLOR_BGR2GRAY)
        body=human_detector.detectMultiScale(grey,1.1,3)

        for(x,y,w,h) in body:


            cv2.rectangle(frameCombined,(x,y),(x+w,y+h),(255,0,0),3)


        cv2.imshow("CAM",frameCombined)

        if (len(body))==0:
            ser.write("C".encode())

        elif (len(body))==1:
            ser.write("O".encode())


    except:
        pass



    if cv2.waitKey(5) & 0xFF==ord("q"):
        camera1.release()
        camera2.release()
        cv2.destroyAllWindows()
        exit(0)

        break

