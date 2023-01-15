from tkinter import *

prithvi = Tk()

prithvi.title("PRITHVI DEFENCE VEHICLE MARK 2 - Classified")
prithvi.geometry('1280x720+100+65')
prithvi.configure(bg="#fff")
prithvi.resizable(False, False)

prithviframe = Frame(prithvi, width=529, height=720, bg="white")
prithviframe.place(x=0, y=0)

prithviimg = PhotoImage(file="prithviimg.png")
prithvipic = Label(prithviframe, image=prithviimg, bg="#fff")
prithvipic.place(x=0, y=0)

prithviinfo = Frame(prithvi, width=766, height=720, bg="white")
prithviinfo.place(x=529, y=0)

heading = Label(prithviinfo, text='Interceptor Missile ', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthprithvi = Label(prithviinfo, text='Length: 13.2 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthprithvi.place(x=115, y=100)

massprithvi = Label(prithviinfo, text='Mass: 18.87 t', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
massprithvi.place(x=367, y=100)

rangeprithvi = Label(prithviinfo, text='Operational range : 2,000 km', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
rangeprithvi.place(x=115, y=180)

engineprithvi = Label(prithviinfo, text='Engine: Three stage rocket motor', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
engineprithvi.place(x=115, y=260)

detonationprithvi = Label(prithviinfo, text='Detonation mechanism: Hit-to-kill interception', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
detonationprithvi.place(x=115, y=340)

ceilingprithvi = Label(prithviinfo, text='Flight altitude: 180 km', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingprithvi.place(x=115, y=420)

accuracyprithvi = Label(prithviinfo, text='Accuracy: <10 cm', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
accuracyprithvi.place(x=115, y=500)

engineprithvi = Label(prithviinfo, text='Engine: Two stage', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
engineprithvi.place(x=115, y=580)

designprithvi = Label(prithviinfo, text='Design: DRDO of India', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
designprithvi.place(x=115, y=660)

prithvi.mainloop()
