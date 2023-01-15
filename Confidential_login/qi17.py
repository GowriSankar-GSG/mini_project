from tkinter import *

qi17 = Tk()

qi17.title("HONG QI-17 - Classified")
qi17.geometry('1280x720+100+65')
qi17.configure(bg="#fff")
qi17.resizable(False, False)

qi17frame = Frame(qi17, width=556, height=720, bg="white")
qi17frame.place(x=0, y=0)

qi17img = PhotoImage(file="qi17img.png")
qi17pic = Label(qi17frame, image=qi17img, bg="#fff")
qi17pic.place(x=0, y=0)

qi17info = Frame(qi17, width=766, height=720, bg="white")
qi17info.place(x=556, y=0)

heading = Label(qi17info, text='Surface-to-Air Missile System', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=80, y=10)

lengthqi17 = Label(qi17info, text='Length:2.9 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthqi17.place(x=80, y=100)

massqi17 = Label(qi17info, text='Mass:165 kg', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
massqi17.place(x=367, y=100)

warheadqi17 = Label(qi17info, text='Warhead:15 kg HE-FRAG', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
warheadqi17.place(x=80, y=180)

rangeqi17 = Label(qi17info, text='Operational range: 1.5 km to 15 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangeqi17.place(x=80, y=260)

platformqi17 = Label(qi17info, text='Launch platform:TEL', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
platformqi17.place(x=80, y=340)

ceilingqi17 = Label(qi17info, text='Flight altitude:10 m to 10 km', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingqi17.place(x=80, y=420)

speedqi17 = Label(qi17info, text='Maximum speed:Mach 3', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
speedqi17.place(x=80, y=500)

propellantqi17 = Label(qi17info, text='Propellant: Solid fuel', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
propellantqi17.place(x=80, y=580)

manufacturerqi17 = Label(qi17info, text='Manufacturer:China Precision Machinery Corp.', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
manufacturerqi17.place(x=80, y=660)

qi17.mainloop()
