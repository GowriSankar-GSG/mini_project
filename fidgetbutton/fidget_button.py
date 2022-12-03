from tkinter import *

from playsound import playsound


def click():
    myLabel1 = Label(file=playsound("1.mp3"))
    myLabel1.pack()


root = Tk()

myButton = Button(root, text="Click Me!!", font=('Times', 150, 'bold'), padx=200, pady=150, command=click, bg="#cba7ef",
                  activebackground="#f5edc1", relief="solid")
myButton.pack()

root.mainloop()

