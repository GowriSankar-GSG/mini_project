from tkinter import *
from tkinter import messagebox
import pymysql


def signuppage():
    loginwin.destroy()
    import signup

loginwin = Tk()

loginwin.title("login")
loginwin.geometry('1280x720+100+65')
loginwin.configure(bg="#fff")
loginwin.resizable(False, False)


def hide():
    openeye.config(file='closeeye.png')
    enpass.config(show='*')
    eyebutton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    enpass.config(show='')
    eyebutton.config(command=hide)


def signin():
    username = user.get()
    password = enpass.get()
    if username == '' or password == '' or username == 'Username':
        messagebox.showerror('Error', 'All fields are required')
    else:
        try:
            connectdb = pymysql.connect(host='localhost', user='root', password='root')
            mycursor = connectdb.cursor()

        except:
            messagebox.showerror('Error', 'Database connectivity issue')
            return

        query = 'use userdata'
        mycursor.execute(query)
        query = 'select * from data where username = %s and password = %s'
        mycursor.execute(query,(username, password))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Invalid username or password')
        else:
            messagebox.showinfo('Welcome', 'login is successful')
            loginwin.destroy()
            import agreement


img = PhotoImage(file="login.png")
Label(loginwin, image=img, bg="#fff").place(x=30, y=100)

frame = Frame(loginwin, width=700, height=600, bg="white")
frame.place(x=550, y=50)

heading = Label(frame, text='Sign in', fg='#62B6B7', bg='white', font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=300, y=50)


def on_enter(event):
    user.delete(0, 'end')


def on_leave(event):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=30, fg='black', bg='white', border=0, font=('Microsoft YaHei UI Light', 20))
user.place(x=140, y=130)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

line1 = Frame(frame, width=485, height=2, bg="black")
line1.place(x=140, y=170)


def on_enter(e):
    enpass.delete(0, 'end')


def on_leave(e):
    encode = enpass.get()
    if encode == '':
        enpass.insert(0, 'Password')


enpass = Entry(frame, width=30, fg='black', bg='white', border=0, font=('Microsoft YaHei UI Light', 20))
enpass.place(x=140, y=250)
enpass.insert(0, 'Password')
enpass.bind('<FocusIn>', on_enter)
enpass.bind('<FocusOut>', on_leave)

openeye = PhotoImage(file="openeye.png")
eyebutton = Button(frame, image=openeye, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=hide)
eyebutton.place(x=570, y=238)

line2 = Frame(frame, width=485, height=2, bg="black")
line2.place(x=140, y=290)

button1 = Button(frame, text='sign in', width=44, pady=16, bg='#0099a8', activebackground='#a7dde8', fg='white',
                 border=0, command=signin, font=30,
                 cursor='hand2')
button1.place(x=140, y=320)

label = Label(frame, text='Don\'t have an account?', fg='#1a1a1a', bg='white', font=('Microsoft YaHei UI Light', 15))
label.place(x=210, y=410)

button2 = Button(frame, text='Sign up', width=6, bg='white', fg='#0099a8', border=0, font=30, cursor='hand2',
                 activeforeground='#1a1a1a',command=signuppage)
button2.place(x=437, y=409)

loginwin.mainloop()
