from tkinter import *

f35 = Tk()

f35.title("F-35A Lightning II - Classified")
f35.geometry('1280x720+100+65')
f35.configure(bg="#fff")
f35.resizable(False, False)

f35frame = Frame(f35, width=495, height=720, bg="white")
f35frame.place(x=0, y=0)

f35img = PhotoImage(file="f35img.png")
f35pic = Label(f35frame, image=f35img, bg="#fff")
f35pic.place(x=0, y=0)

f35info = Frame(f35, width=766, height=720, bg="white")
f35info.place(x=515, y=0)

heading = Label(f35info, text='Multi-Role Fighter', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthf35 = Label(f35info, text='Length:15.7 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthf35.place(x=115, y=100)

areaf35 = Label(f35info, text='Wing area: 42.7 sq.m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
areaf35.place(x=367, y=100)

payloadf35 = Label(f35info, text='Payload : 8160 kg', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
payloadf35.place(x=115, y=180)

speedf35 = Label(f35info, text='Max Speed: Mach 1.6', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
speedf35.place(x=115, y=260)

rangef35 = Label(f35info, text='Range:2,200 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangef35.place(x=115, y=340)

ceilingf35 = Label(f35info, text='Service ceiling:15.24km', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingf35.place(x=115, y=420)

weightf35 = Label(f35info, text='Weight : 29,900 kg', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
weightf35.place(x=115, y=500)

pointsf35 = Label(f35info, text='Hardpoints: 7 hardpoints', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
pointsf35.place(x=115, y=580)

manufacturerf35 = Label(f35info, text='Manufacturer : Lockheed Martin', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
manufacturerf35.place(x=115, y=660)

f35.mainloop()
