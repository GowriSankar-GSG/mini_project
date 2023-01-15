from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()

root.title("Digital Clock")


def none():
    text = strftime(' %H:%M:%S ')
    lbl.config(text=text)
    lbl.after(1000, none)


lbl = Label(root, font=('digital-7', 100, 'bold'), background='black', foreground="red")
lbl.pack(anchor='center')
none()
mainloop()
