from tkinter import *

usa = Tk()


def f35():
    usa.destroy()
    import f35

def b2():
    usa.destroy()
    import b2

def alcm():
    usa.destroy()
    import alcm

def mim104():
    usa.destroy()
    import patriot

usa.title("USA - Classified")
usa.geometry('800x800+350+15')
usa.configure(bg="white")
usa.resizable(False, False)

f35frame = Frame(usa, width=400, height=400, bg="white")
f35frame.place(x=0, y=0)

f35img = PhotoImage(file="f35.png")
f35button = Button(f35frame, image=f35img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=f35)
f35button.place(x=24, y=25)

b2frame = Frame(usa, width=400, height=400, bg="white")
b2frame.place(x=400, y=0)

b2img = PhotoImage(file="b2.png")
b2button = Button(b2frame, image=b2img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=b2)
b2button.place(x=24, y=25)

alcmframe = Frame(usa, width=400, height=400, bg="white")
alcmframe.place(x=0, y=400)

alcmimg = PhotoImage(file="alcm.png")
alcmbutton = Button(alcmframe, image=alcmimg, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=alcm)
alcmbutton.place(x=24, y=24)

mim104frame = Frame(usa, width=400, height=400, bg="white")
mim104frame.place(x=400, y=400)

mim104img = PhotoImage(file="mim104.png")
mim104button = Button(mim104frame, image=mim104img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=mim104)
mim104button.place(x=24, y=24)

usa.mainloop()
