from tkinter import *

china = Tk()


def j20():
    china.destroy()
    import j20

def df41():
    china.destroy()
    import df41

def fc31():
    china.destroy()
    import fc31

def qi17():
    china.destroy()
    import qi17

china.title("china - Classified")
china.geometry('800x800+350+15')
china.configure(bg="white")
china.resizable(False, False)

j20frame = Frame(china, width=400, height=400, bg="white")
j20frame.place(x=0, y=0)

j20img = PhotoImage(file="j20.png")
j20button = Button(j20frame, image=j20img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=j20)
j20button.place(x=24, y=25)

df41frame = Frame(china, width=400, height=400, bg="white")
df41frame.place(x=400, y=0)

df41img = PhotoImage(file="df41.png")
df41button = Button(df41frame, image=df41img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=df41)
df41button.place(x=24, y=25)

fc31frame = Frame(china, width=400, height=400, bg="white")
fc31frame.place(x=0, y=400)

fc31img = PhotoImage(file="fc31.png")
fc31button = Button(fc31frame, image=fc31img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=fc31)
fc31button.place(x=24, y=24)

qi17frame = Frame(china, width=400, height=400, bg="white")
qi17frame.place(x=400, y=400)

qi17img = PhotoImage(file="qi17.png")
qi17button = Button(qi17frame, image=qi17img, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=qi17)
qi17button.place(x=24, y=24)

china.mainloop()
