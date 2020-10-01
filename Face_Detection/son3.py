import cv2
import numpy as np
from tkinter import *
import serial
from PIL import Image,ImageTk



ser = serial.Serial('COM3', 9600)
human_detector=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")


window=Tk()
window.geometry("600x300")


font=cv2.FONT_HERSHEY_SIMPLEX
camera1=cv2.VideoCapture(0)
camera2=cv2.VideoCapture(1)
idn=cv2.createBackgroundSubtractorMOG2()

frame1=Frame(window,width=300,height=200)
frame1.grid(row=0,column=0)
frame2=Frame(window,width=300,height=200)
frame2.grid(row=0,column=1)




def button():
    global  frame1,frame2
    ret1,frame1=camera1.read()
    rer2,frame2=camera2.read()

    frameCombined = np.hstack((frame1, frame2))
    idnmask=idn.apply(frameCombined)
    cv2.imshow("fg",idnmask)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        pass
    camera1.release()
    camera2.release()
    cv2.destroyAllWindows()
    exit(0)
    window.mainloop()

Button(window,text="Change",command="button").grid(row=1,column=0,padx=600,pady=20)


while True:
    try:
        ret1, frame1 = camera1.read()
        ret2, frame2 = camera2.read()
        frameCombined = np.hstack((frame1, frame2))
        grey = cv2.cvtColor(frameCombined, cv2.COLOR_BGR2GRAY)
        body = human_detector.detectMultiScale(grey, 1.1, 3)

        for (x, y, w, h) in body:
            cv2.rectangle(frameCombined, (x, y), (x + w, y + h), (255, 0, 0), 3)

        cv2.imshow("CAM", frameCombined)

        if (len(body)) == 0:

            ser.write("O".encode())

        elif (len(body)) == 1:
            ser.write("C".encode())







    except:
        pass






    if cv2.waitKey(5) & 0xFF==ord("q"):


        camera1.release()
        camera2.release()
        cv2.destroyAllWindows()
        window.mainloop()
        exit(0)


        break


