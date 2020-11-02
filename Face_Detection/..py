import time
import serial

ser = serial.Serial('COM4', 9600)

while True:
    value = float(ser.readline())

    if value <= 250:
        print ("250")

    elif value <=500:
        print("500")

    elif value<=750:

        print("750")

    else :
        print("100")



    time.sleep(0.5)