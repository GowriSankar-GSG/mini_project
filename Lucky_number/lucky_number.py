import random
from tkinter import *

from playsound import playsound

root = Tk()
root.geometry("1000x600")


def mydelete():
    Label(playsound("click.mp3"))
    myLabel2.destroy()
    myButton1["state"] = NORMAL
    delbutton1["state"] = DISABLED


myLabel2 = Label(root, text="", font=("Times", 40))


def click():
    Label(playsound("click.mp3"))
    global myLabel2
    myLabel2 = Label(root, text="", font=("Times", 40))

    name = myEntry1.get()
    no_letter = len(name)
    if no_letter <= 3:
        lucky_number1 = random.randint(0, no_letter * 33)
    elif no_letter >= 10:
        lucky_number1 = random.randint(0, no_letter * 3)
    else:
        lucky_number1 = random.randint(0, no_letter * 11)
    str_lnum = str(lucky_number1)
    if no_letter == 0:
        myLabel2 = Label(root, text="Enter your name to receive a lucky number.", font=("Times", 40))
    else:
        myLabel2 = Label(root, text=name + ",Your Lucky number for today is " + str_lnum + ".", font=("Times", 40))
    myLabel2.pack()
    delbutton1["state"] = DISABLED
    myButton1["state"] = DISABLED
    delbutton1["state"] = NORMAL


myEntry1 = Entry(root, width=20, font=("Times", 40))
myLabel3 = Label(root, text="Enter Your Name:", font=("Times", 40))
myButton1 = Button(root, text="GET LUCKY!!!", font=('Times', 15, 'bold'), padx=100, pady=20, command=click,
                   bg="#cba7ef",
                   activebackground="#f5edc1", relief="solid")
delbutton1 = Button(root, text="Restart", font=('Times', 15, 'bold'), command=mydelete, padx=135, pady=20,
                    bg="#cba7ef",
                    activebackground="#f5edc1", relief="solid")

myLabel3.pack()
myEntry1.pack()
myButton1.pack()
delbutton1.pack()

root.mainloop()
