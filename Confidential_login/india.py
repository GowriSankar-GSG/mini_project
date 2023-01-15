from tkinter import *

india = Tk()


def rafale():
    india.destroy()
    import rafale

def tejas():
    india.destroy()
    import tejas

def brahmos():
    india.destroy()
    import brahmos

def prithvi():
    india.destroy()
    import prithvi

india.title("INDIA - Classified")
india.geometry('800x800+350+15')
india.configure(bg="white")
india.resizable(False, False)

rafaleframe = Frame(india, width=400, height=400, bg="white")
rafaleframe.place(x=0, y=0)

rafaleimg = PhotoImage(file="rafale.png")
rafalebutton = Button(rafaleframe, image=rafaleimg, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=rafale)
rafalebutton.place(x=24, y=25)

tejasframe = Frame(india, width=400, height=400, bg="white")
tejasframe.place(x=400, y=0)

tejasimg = PhotoImage(file="tejas.png")
tejasbutton = Button(tejasframe, image=tejasimg, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=tejas)
tejasbutton.place(x=24, y=25)

brahmosframe = Frame(india, width=400, height=400, bg="white")
brahmosframe.place(x=0, y=400)

brahmosimg = PhotoImage(file="brahmos.png")
brahmosbutton = Button(brahmosframe, image=brahmosimg, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=brahmos)
brahmosbutton.place(x=24, y=24)

prithviframe = Frame(india, width=400, height=400, bg="white")
prithviframe.place(x=400, y=400)

prithviimg = PhotoImage(file="prithvi.png")
prithvibutton = Button(prithviframe, image=prithviimg, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=prithvi)
prithvibutton.place(x=24, y=24)

india.mainloop()
