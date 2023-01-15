from tkinter import *
from tkinter import Checkbutton
from tkinter import messagebox

import pymysql


def clear():
    user.delete(0, END)
    usermail.delete(0, END)
    enpass.delete(0, END)
    conpass.delete(0, END)
    agree.set(0)


def loginpage():
    signupwin.destroy()
    import login


signupwin = Tk()

signupwin.title("Sign up")
signupwin.geometry('1280x720+100+65')
signupwin.configure(bg="#fff")
signupwin.resizable(False, False)


def signup():
    username = user.get()
    mail = usermail.get()
    password = enpass.get()
    conpassword = conpass.get()
    term = agree.get()

    if username == 'username' or mail == 'Email Address' or password == 'Password' or conpassword == 'Confirm Password':
        messagebox.showerror('Invalid', 'All fields are required')

    elif password != conpassword:
        messagebox.showerror('Error', 'Password mismatch')

    elif term == 0:
        messagebox.showerror('Error', 'Please read and accept the terms & conditions to proceed')

    else:
        try:
            connectdb = pymysql.connect(host='localhost', user='root', password='root')
            mycursor = connectdb.cursor()
        except:
            messagebox.showerror('Error', 'Database connectivity issue')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table data(id int auto_increment primary key not null,username varchar(50),mail varchar(50),password varchar(50))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')

        query = 'select * from data where username = %s'
        mycursor.execute(query, (username))
        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error', 'Username already exist')
        else:
            query = 'insert into data(username,mail,password) values(%s,%s,%s)'
            mycursor.execute(query, (username, mail, password))
            connectdb.commit()
            connectdb.close()
            messagebox.showinfo('Success', 'Your account has been successfully')
            clear()
            signupwin.destroy()
            import login


img = PhotoImage(file="signup.png")
Label(signupwin, image=img, bg="#fff").place(x=30, y=100)

frame = Frame(signupwin, width=700, height=680, bg="white")
frame.place(x=550, y=30)

heading = Label(frame, text='Sign up', fg='#62B6B7', bg='white', font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=300, y=10)


def on_enter(event):
    user.delete(0, 'end')


def on_leave(event):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')


user = Entry(frame, width=30, fg='#1a1a1a', bg='white', border=0, font=('Microsoft YaHei UI Light', 20))
user.place(x=140, y=100)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

line1 = Frame(frame, width=485, height=2, bg="#1a1a1a")
line1.place(x=140, y=140)


def on_enter(event):
    usermail.delete(0, 'end')


def on_leave(event):
    mail = usermail.get()
    if mail == '':
        usermail.insert(0, 'Email Address')


usermail = Entry(frame, width=30, fg='#1a1a1a', bg='white', border=0, font=('Microsoft YaHei UI Light', 20))
usermail.place(x=140, y=190)
usermail.insert(0, 'Email Address')
usermail.bind('<FocusIn>', on_enter)
usermail.bind('<FocusOut>', on_leave)

line2 = Frame(frame, width=485, height=2, bg="#1a1a1a")
line2.place(x=140, y=230)


def on_enter(e):
    enpass.delete(0, 'end')


def on_leave(e):
    encode = enpass.get()
    if encode == '':
        enpass.insert(0, 'Password')


enpass = Entry(frame, width=30, fg='#1a1a1a', bg='white', border=0, font=('Microsoft YaHei UI Light', 20))
enpass.place(x=140, y=280)
enpass.insert(0, 'Password')
enpass.bind('<FocusIn>', on_enter)
enpass.bind('<FocusOut>', on_leave)

line3 = Frame(frame, width=485, height=2, bg="#1a1a1a")
line3.place(x=140, y=320)


def on_enter(e):
    conpass.delete(0, 'end')


def on_leave(e):
    concode = conpass.get()
    if concode == '':
        conpass.insert(0, 'Confirm Password')


conpass = Entry(frame, width=30, fg='#1a1a1a', bg='white', border=0, font=('Microsoft YaHei UI Light', 20))
conpass.place(x=140, y=370)
conpass.insert(0, 'Confirm Password')
conpass.bind('<FocusIn>', on_enter)
conpass.bind('<FocusOut>', on_leave)

line4 = Frame(frame, width=485, height=2, bg="#1a1a1a")
line4.place(x=140, y=410)

agree = IntVar()
termbutton = Checkbutton(frame, text='Agree to the terms and conditions and privacy policy', cursor='hand2', bd=1,
                         variable=agree, font=('Microsoft YaHei UI Light', 14), height=1, bg='white', onvalue=1,
                         offvalue=0, activebackground='white')
termbutton.place(x=140, y=450)

button1 = Button(frame, text='Sign up', width=44, pady=16, bg='#0099a8', command=signup,
                 activebackground='#a7dde8', fg='white', border=0, font=30, cursor='hand2')
button1.place(x=140, y=520)

label = Label(frame, text='Already have an account?', fg='#1a1a1a', bg='white', font=('Microsoft YaHei UI Light', 16))
label.place(x=210, y=610)

button2 = Button(frame, text='Sign in', width=6, bg='white', fg='#0099a8', border=0, font=30, cursor='hand2',
                 activeforeground='#1a1a1a', command=loginpage)
button2.place(x=455, y=610)

signupwin.mainloop()
