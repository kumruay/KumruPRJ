from tkinter import *

root=Tk()
root.title("Chay Bot")
root.geometry('400x500')

file_menu=Menu(root)
file_menu.add_command(label="File..")
file_menu.add_command(label="Save as..")
file_menu.add_command(label="Exit")

main_menu=Menu(root)
main_menu.add_cascade(label="File",menu= file_menu)
main_menu.add_command(label="Edit")
main_menu.add_command(label="Quit")
root.config(menu=main_menu)

chat_Window=Text(root,bd=1,bg="black",width=50,height=8)
chat_Window.place(x=6,y=6,width=370,height=385)

message_Window=Text(root,bd=1,bg="black",width=10,height=2)
message_Window.place(x=125,y=400,width=260,height=80)

button=Button(root,text="Send",bg='blue',activebackground="light blue",width=12,height=5,font=('Arial,12'))
button.place(x=6,y=400,width=120,height=88)

scroll_bar=Scrollbar(root,command=chat_Window.yview())
scroll_bar.place(x=375,y=5,height=385)


root.mainloop()
