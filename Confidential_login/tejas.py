from tkinter import *

tejas = Tk()

tejas.title("HAL TEJAS - Classified")
tejas.geometry('1280x720+100+65')
tejas.configure(bg="#fff")
tejas.resizable(False, False)

tejasframe = Frame(tejas, width=528, height=720, bg="white")
tejasframe.place(x=0, y=0)

tejasimg = PhotoImage(file="tejasimg.png")
tejaspic = Label(tejasframe, image=tejasimg, bg="#fff")
tejaspic.place(x=0, y=0)

tejasinfo = Frame(tejas, width=766, height=720, bg="white")
tejasinfo.place(x=528, y=0)

heading = Label(tejasinfo, text='Multi-Role Fighter', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=60, y=10)

lengthtejas = Label(tejasinfo, text='Length: 13.2 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthtejas.place(x=60, y=100)

areatejas = Label(tejasinfo, text='Wing area: 38.4 sq.m.', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
areatejas.place(x=300, y=100)

payloadtejas = Label(tejasinfo, text='Payload : 5,300 kg', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
payloadtejas.place(x=60, y=180)

speedtejas = Label(tejasinfo, text='Max Speed: Mach 1.6', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
speedtejas.place(x=60, y=260)

rangetejas = Label(tejasinfo, text='Range: 1,850 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangetejas.place(x=60, y=340)

ceilingtejas = Label(tejasinfo, text='Service ceiling: 16 km', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingtejas.place(x=60, y=420)

weighttejas = Label(tejasinfo, text='Weight : 9,800 kg', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
weighttejas.place(x=60, y=500)

pointstejas = Label(tejasinfo, text='Hardpoints: 8 hardpoints', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
pointstejas.place(x=60, y=580)

manufacturertejas = Label(tejasinfo, text='Manufacturer: Aeronautical Development Agency', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
manufacturertejas.place(x=60, y=660)

tejas.mainloop()
