import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
import numpy as np
import serial

# import Opencv module
import cv2

from ui_main_window import *
font=cv2.FONT_HERSHEY_SIMPLEX
human_detector=cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
ser = serial.Serial('COM3', 9600)

class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        # set control_bt callback clicked  function
        self.ui.control_bt.clicked.connect(self.controlTimer)

    # view camera
    def viewCam(self):
        global body,imageCombined,grey
        # read image in BGR format
        ret2, image1 = self.cap1.read()
        ret2,image2=self.cap2.read()
        imageCombined = np.hstack((image1, image2))
        grey = cv2.cvtColor(imageCombined, cv2.COLOR_BGR2GRAY)
        body = human_detector.detectMultiScale(grey, 1.1, 3)
        # convert image to RGB format
        imageCombined = cv2.cvtColor(imageCombined, cv2.COLOR_BGR2RGB)
        for (x, y, w, h) in body:
            cv2.rectangle(imageCombined, (x, y), (x + w, y + h), (255, 0, 0), 3)


        if (len(body)) == 0:
            ser.write("C".encode())

        elif (len(body)) == 1:
            ser.write("O".encode())




        # get image infos
        height, width, channel = imageCombined.shape
        step = channel * width
        # create QImage from image
        qImg = QImage(imageCombined.data, width, height, step, QImage.Format_RGB888)
        # show image in img_label
        self.ui.image_label.setPixmap(QPixmap.fromImage(qImg))

    # start/stop timer
    def controlTimer(self):
        # if timer is stopped
        if not self.timer.isActive():
            # create video capture
            self.cap1= cv2.VideoCapture(0)
            self.cap2 = cv2.VideoCapture(1)




            # start timer
            self.timer.start(20)
            # update control_bt text
            self.ui.control_bt.setText("Stop")
        # if timer is started
        else:
            # stop timer
            self.timer.stop()
            # release video capture
            self.cap1.release()
            self.cap2.release()

            # update control_bt text
            self.ui.control_bt.setText("Start")


if __name__ == '__main__':

    app = QApplication(sys.argv)

    # create and show mainWindow

    mainWindow = MainWindow()
    mainWindow.show()


    sys.exit(app.exec_())

