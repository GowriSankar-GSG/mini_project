from tkinter import *

b2 = Tk()

b2.title("NORTHROP GRUMMAN B-2 SPIRIT - Classified")
b2.geometry('1280x720+100+65')
b2.configure(bg="#fff")
b2.resizable(False, False)

b2frame = Frame(b2, width=495, height=720, bg="white")
b2frame.place(x=0, y=0)

b2img = PhotoImage(file="b2img.png")
b2pic = Label(b2frame, image=b2img, bg="#fff")
b2pic.place(x=0, y=0)

b2info = Frame(b2, width=766, height=720, bg="white")
b2info.place(x=515, y=0)

heading = Label(b2info, text='Strategic Heavy Bomber', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthb2 = Label(b2info, text='Length:21.0 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthb2.place(x=115, y=100)

weightb2 = Label(b2info, text='Gross weight:152,200 kg', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
weightb2.place(x=367, y=100)

fuelb2 = Label(b2info, text='Fuel capacity:75,750 kg', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
fuelb2.place(x=115, y=180)

speedb2 = Label(b2info, text='Maximum speed: 1,010 km/h', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
speedb2.place(x=115, y=260)

rangeb2 = Label(b2info, text='Range:11,000 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangeb2.place(x=115, y=340)

ceilingb2 = Label(b2info, text='Service ceiling:15,200 m', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingb2.place(x=115, y=420)

heightb2 = Label(b2info, text='Height: 5.18 m', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
heightb2.place(x=115, y=500)

areasb2 = Label(b2info, text='Wing area:  478 sq.m.', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
areasb2.place(x=115, y=580)

designb2 = Label(b2info, text='Design: Northrop Grumman', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
designb2.place(x=115, y=660)

b2.mainloop()
