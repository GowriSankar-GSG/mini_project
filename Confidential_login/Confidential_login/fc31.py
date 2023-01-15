from tkinter import *

fc31 = Tk()

fc31.title("SHENYANG FC-31 GRYFALCON - Classified")
fc31.geometry('1280x720+100+65')
fc31.configure(bg="#fff")
fc31.resizable(False, False)

fc31frame = Frame(fc31, width=495, height=720, bg="white")
fc31frame.place(x=0, y=0)

fc31img = PhotoImage(file="fc31img.png")
fc31pic = Label(fc31frame, image=fc31img, bg="#fff")
fc31pic.place(x=0, y=0)

fc31info = Frame(fc31, width=766, height=720, bg="white")
fc31info.place(x=515, y=0)

heading = Label(fc31info, text='5th-generation fighter', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthfc31 = Label(fc31info, text='Length: 17.3 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthfc31.place(x=115, y=100)

wingfc31 = Label(fc31info, text='Wing area: 50 sq.m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
wingfc31.place(x=367, y=100)

payloadfc31 = Label(fc31info, text='Payload: 8000 kg', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
payloadfc31.place(x=115, y=180)

speedfc31 = Label(fc31info, text='Maximum speed: Mach 1.8', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
speedfc31.place(x=115, y=260)

rangefc31 = Label(fc31info, text='Combat Range: 1,200 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangefc31.place(x=115, y=340)

ceilingfc31 = Label(fc31info, text='Service ceiling: 16 km', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingfc31.place(x=115, y=420)

weightfc31 = Label(fc31info, text='Weight : 28,000 kg', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
weightfc31.place(x=115, y=500)

pointsfc31 = Label(fc31info, text='Hardpoints: 12 hardpoints', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
pointsfc31.place(x=115, y=580)

designfc31 = Label(fc31info, text='Design: Shenyang Aircraft Design Institute', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
designfc31.place(x=115, y=660)

fc31.mainloop()
