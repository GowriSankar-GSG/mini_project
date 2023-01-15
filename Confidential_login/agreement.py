from tkinter import *


def decline():
    agreementwin.destroy()


def accept():
    agreementwin.destroy()
    import topsecret


agreementwin = Tk()

agreementwin.title("NDA-Confidential")
agreementwin.geometry('1280x720+100+65')
agreementwin.configure(bg="#f7f7f7")
agreementwin.resizable(False, False)

img = PhotoImage(file="classified1.png")
Label(agreementwin, image=img, bg="#fff").place(x=3, y=0)

frame = Frame(agreementwin, width=565, height=600, bg="#f7f7f7")
frame.place(x=690, y=50)

heading = Label(frame, text='NDA - Confidential', fg='#b30000', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=105, y=50)

agreementterm = Label(frame, text='By Accepting you agree to the Non-disclosure \n agreement terms and conditions',
                      fg='#b30000', bg='white', font=('Microsoft YaHei UI Light', 15, 'bold'))
agreementterm.place(x=55, y=200)

button1 = Button(frame, text='Accept', width=44, pady=16, bg='#b30000', activebackground='#e94235', fg='white',
                 border=0, font=40,
                 cursor='hand2', command=accept)
button1.place(x=50, y=320)

button2 = Button(frame, text='Decline', width=44, pady=16, bg='#b30000', activebackground='#e94235', fg='white',
                 border=0, font=40,
                 cursor='hand2', command=decline)

button2.place(x=50, y=409)

agreementwin.mainloop()
