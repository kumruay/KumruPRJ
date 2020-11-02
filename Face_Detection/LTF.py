import serial
from drawnow import *

randomNumberArray=[]
arduinoData=serial.Serial("COM4",9600)
plt.ion() # Tell matplotlib you want interactive mode to plot live data
count=0

def makeFig():
    plt.ylim(0,100)
    plt.title("My Live Streaming Random Data")
    plt.grid(True)  ##Turn the grid on
    plt.ylabel("Random Number")
    plt.plot(randomNumberArray,color="red",marker="o",markerfacecolor="blue",label="Random Number")
    plt.legend(loc="upper left")  ## plot the legend

while True: ##While loop that loops forever
    while (arduinoData.inWaiting()==0): ##Wait here until there is data
        pass

    #arduinoString =arduinoData.readline()  ## read the line of text from the serial port

    #dataArray=arduinoString  ## Split it into an array called dataArray
    #randomNumber = float(daraArray)   ##Convert first element to floating number and put it randomNumber
    randomNumber=float(arduinoData.readline())
    print (randomNumber)

    randomNumberArray.append(randomNumber)  #Built our randomNumberArray array by appanding randomNumber reading

    drawnow(makeFig)
    plt.pause(.000001)
    count=count +1
    if (count>50):
        randomNumberArray.pop(0)



