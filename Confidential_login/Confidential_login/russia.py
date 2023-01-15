from tkinter import *

russia = Tk()


def su57():
    russia.destroy()
    import su57

def mig31():
    russia.destroy()
    import mig31

def avangard():
    russia.destroy()
    import avangard

def s400():
    russia.destroy()
    import s400

russia.title("Russia - Classified")
russia.geometry('800x800+350+15')
russia.configure(bg="white")
russia.resizable(False, False)

su57frame = Frame(russia, width=400, height=400, bg="white")
su57frame.place(x=0, y=0)

su57img = PhotoImage(file="su57.png")
su57button = Button(su57frame, image=su57img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=su57)
su57button.place(x=24, y=25)

mig31frame = Frame(russia, width=400, height=400, bg="white")
mig31frame.place(x=400, y=0)

mig31img = PhotoImage(file="mig31.png")
mig31button = Button(mig31frame, image=mig31img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=mig31)
mig31button.place(x=24, y=25)

avangardframe = Frame(russia, width=400, height=400, bg="white")
avangardframe.place(x=0, y=400)

avangardimg = PhotoImage(file="avangard.png")
avangardbutton = Button(avangardframe, image=avangardimg, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=avangard)
avangardbutton.place(x=24, y=24)

s400frame = Frame(russia, width=400, height=400, bg="white")
s400frame.place(x=400, y=400)

s400img = PhotoImage(file="s400.png")
s400button = Button(s400frame, image=s400img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=s400)
s400button.place(x=24, y=24)

russia.mainloop()
