import time
from tkinter import *
import serial




ser = serial.Serial('COM4', 9600)


window=Tk()
window.geometry("150x200")
window.wm_title("Voltage")


main_block=Text(window,bg="pink",width=10,height=8)  #Voltaj değerlerini gösterecek olan siyah kutuların arkasına dört kutuya denk pembe renk bir main blok oluşturuluyor.
main_block.place(x=10,y=10)

title_block=Text(window,bg="white",width=7,height=0.5 , font=("Arial 16"))  #Okunacak voltaj değerlerinde "Prj Boş","Şarj 100%100"yada "Şarj" yazısını göserecek title blok oluşturulyor.
title_block.place(x=10,y=150)

#block1=Text(window,bg="black",width=10,height=2)  #Dört tane şarjı gösterecek olan kutuları ilk burda yazmıştım, aşşağdaki kodda kullandığım için bunlar burda command kısmına aldım.
#block1.place(x=10,y=10)

#block2=Text(window,bg="black",width=10,height=2)
#block2.place(x=10,y=45)

#block3=Text(window,bg="black",width=10,height=2)
#block3.place(x=10,y=80)

#block4=Text(window,bg="black",width=10,height=2)
#block4.place(x=10,y=110)

while True: ##While loop that loops forever


    value=float(ser.readline())  # COM4'ten gelecek olan değerler float olarak alınıyor.
   # print(value)


    if value <= 250:  #Bu kıssımda sadece son blok siyah olacak şekilde kutuları tanımladım.


        block1 = Text(window, bg="pink", width=10, height=2)
        block1.place(x=10, y=10)

        block2 = Text(window, bg="pink", width=10, height=2)
        block2.place(x=10, y=45)

        block3 = Text(window, bg="pink", width=10, height=2)
        block3.place(x=10, y=80)

        block4 = Text(window, bg="black", width=10, height=2)
        block4.place(x=10, y=110)






    if (value> 250 and value <=500):  #Bu kıssımda sadece son iki blok siyah olacak şekilde kutuları tanımladım.

        block1 = Text(window, bg="pink", width=10, height=2)
        block1.place(x=10, y=10)

        block2 = Text(window, bg="pink", width=10, height=2)
        block2.place(x=10, y=45)

        block3 = Text(window, bg="black", width=10, height=2)
        block3.place(x=10, y=80)

        block4 = Text(window, bg="black", width=10, height=2)
        block4.place(x=10, y=110)



    if (value >500 and value<=750):  #Bu kıssımda sadece son üç blok siyah olacak şekilde kutuları tanımladım.


        block1 = Text(window, bg="pink", width=10, height=2)
        block1.place(x=10, y=10)

        block2 = Text(window, bg="black", width=10, height=2)
        block2.place(x=10, y=45)

        block3 = Text(window, bg="black", width=10, height=2)
        block3.place(x=10, y=80)

        block4 = Text(window, bg="black", width=10, height=2)
        block4.place(x=10, y=110)




    if (value>750 )  :  #Bu kıssımda bütün bloklar siyah olacak şekilde kutuları tanımladım.


        block1 = Text(window, bg="black", width=10, height=2)
        block1.place(x=10, y=10)

        block2 = Text(window, bg="black", width=10, height=2)
        block2.place(x=10, y=45)

        block3 = Text(window, bg="black", width=10, height=2)
        block3.place(x=10, y=80)

        block4 = Text(window, bg="black", width=10, height=2)
        block4.place(x=10, y=110)

window.mainloop()  #Pencereyi çağırdım , yalnız her bloğun altına mainloop'u yazdığımda kod çalişiyor
                    # ama devamlı olarak değişime göre değişiklik gostermiyordu bu kıssımda çağırdığımdada
                    # pencere açılmıyor.














