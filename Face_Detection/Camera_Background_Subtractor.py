import cv2
import numpy as np




camera1=cv2.VideoCapture(0)
camera2=cv2.VideoCapture(1)

font=cv2.FONT_HERSHEY_SIMPLEX  #İki kamera görüntüsünü birleştirmek için kullanılan kod.

idn=cv2.createBackgroundSubtractorMOG2()
#denem=cv2.createButton(buton,f)  #creatButton 'u unutmamak için yazdım ama bunun sadece java'da kullanıdığını öğrendim.

while True:
    ret1,frame1=camera1.read() #ret gelen datada sorun olup olmadığına bakıyor.
    rer2,frame2=camera2.read()

    frameCombined = np.hstack((frame1, frame2))
    idnmask=idn.apply(frameCombined)


    cv2.imshow("fg",idnmask)  #Burda kamera görüntüsü değil sadece yei oluşturulan görüntüyü çağıdım.

    k=cv2.waitKey(30) & 0xff
    if k == 27:
        pass


camera1.release()
camera2.release()
cv2.destroyAllWindows()