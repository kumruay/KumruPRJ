import time
from tkinter import *
import serial




ser = serial.Serial('COM4', 9600)


window=Tk()
window.geometry("150x200")
window.wm_title("Voltage")


main_block=Text(window,bg="pink",width=10,height=8)
main_block.place(x=10,y=10)

title_block=Text(window,bg="white",width=7,height=0.5 , font=("Arial 16"))
title_block.place(x=10,y=150)

#block1=Text(window,bg="black",width=10,height=2)
#block1.place(x=10,y=10)

#block2=Text(window,bg="black",width=10,height=2)
#block2.place(x=10,y=45)

#block3=Text(window,bg="black",width=10,height=2)
#block3.place(x=10,y=80)

#block4=Text(window,bg="black",width=10,height=2)
#block4.place(x=10,y=110)

while True: ##While loop that loops forever


    value=float(ser.readline())
   # print(value)


    if value <= 250:


        block1 = Text(window, bg="pink", width=10, height=2)
        block1.place(x=10, y=10)

        block2 = Text(window, bg="pink", width=10, height=2)
        block2.place(x=10, y=45)

        block3 = Text(window, bg="pink", width=10, height=2)
        block3.place(x=10, y=80)

        block4 = Text(window, bg="black", width=10, height=2)
        block4.place(x=10, y=110)






    if (value> 250 and value <=500):

        block1 = Text(window, bg="pink", width=10, height=2)
        block1.place(x=10, y=10)

        block2 = Text(window, bg="pink", width=10, height=2)
        block2.place(x=10, y=45)

        block3 = Text(window, bg="black", width=10, height=2)
        block3.place(x=10, y=80)

        block4 = Text(window, bg="black", width=10, height=2)
        block4.place(x=10, y=110)



    if (value >500 and value<=750):


        block1 = Text(window, bg="pink", width=10, height=2)
        block1.place(x=10, y=10)

        block2 = Text(window, bg="black", width=10, height=2)
        block2.place(x=10, y=45)

        block3 = Text(window, bg="black", width=10, height=2)
        block3.place(x=10, y=80)

        block4 = Text(window, bg="black", width=10, height=2)
        block4.place(x=10, y=110)




    if (value>750 )  :


        block1 = Text(window, bg="black", width=10, height=2)
        block1.place(x=10, y=10)

        block2 = Text(window, bg="black", width=10, height=2)
        block2.place(x=10, y=45)

        block3 = Text(window, bg="black", width=10, height=2)
        block3.place(x=10, y=80)

        block4 = Text(window, bg="black", width=10, height=2)
        block4.place(x=10, y=110)

window.mainloop()














