from tkinter import *

rafale = Tk()

rafale.title("DASSAULT RAFALE - Classified")
rafale.geometry('1280x720+100+65')
rafale.configure(bg="#fff")
rafale.resizable(False, False)

rafaleframe = Frame(rafale, width=555, height=720, bg="white")
rafaleframe.place(x=0, y=0)

rafaleimg = PhotoImage(file="rafaleimg.png")
rafalepic = Label(rafaleframe, image=rafaleimg, bg="#fff")
rafalepic.place(x=0, y=0)

rafaleinfo = Frame(rafale, width=766, height=720, bg="white")
rafaleinfo.place(x=555, y=0)

heading = Label(rafaleinfo, text='Multi-Role Fighter', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthrafale = Label(rafaleinfo, text='Length: 15.27 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthrafale.place(x=115, y=100)

arearafale = Label(rafaleinfo, text='Wing area: 45.7 sq.m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
arearafale.place(x=367, y=100)

speedrafale = Label(rafaleinfo, text='Maximum speed: 1,912 km/h', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
speedrafale.place(x=115, y=180)

rangerafale = Label(rafaleinfo, text='Combat range: 1,850 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangerafale.place(x=115, y=260)

ceilingrafale = Label(rafaleinfo, text='Service ceiling: 16 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingrafale.place(x=115, y=340)

payloadrafale = Label(rafaleinfo, text='Payload: 9,500 kg', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
payloadrafale.place(x=115, y=420)

weightrafale = Label(rafaleinfo, text='Max takeoff weight: 24,500 kg', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
weightrafale.place(x=115, y=500)

pointsrafale = Label(rafaleinfo, text='Hardpoints: 14 hardpoints', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
pointsrafale.place(x=115, y=580)

manufacturerrafale = Label(rafaleinfo, text='Manufacturer: Dassault Aviation', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
manufacturerrafale.place(x=115, y=660)

rafale.mainloop()
