from tkinter import *

mig31 = Tk()

mig31.title("MIKOYAN MIG-31 - Classified")
mig31.geometry('1280x720+100+65')
mig31.configure(bg="#fff")
mig31.resizable(False, False)

mig31frame = Frame(mig31, width=495, height=720, bg="white")
mig31frame.place(x=0, y=0)

mig31img = PhotoImage(file="mig.png")
mig31pic = Label(mig31frame, image=mig31img, bg="#fff")
mig31pic.place(x=0, y=0)

mig31info = Frame(mig31, width=766, height=720, bg="white")
mig31info.place(x=515, y=0)

heading = Label(mig31info, text='Interceptor Aircraft', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthmig31 = Label(mig31info, text='Length: 22.62 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthmig31.place(x=115, y=100)

weightmig31 = Label(mig31info, text='Gross weight: 41,000 kg', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
weightmig31.place(x=367, y=100)

fuelmig31 = Label(mig31info, text='Fuel capacity:16,130 kg', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
fuelmig31.place(x=115, y=180)

speedmig31 = Label(mig31info, text='Maximum speed: Mach 2.4', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
speedmig31.place(x=115, y=260)

rangemig31 = Label(mig31info, text='Range: 3,000 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangemig31.place(x=115, y=340)

ceilingmig31 = Label(mig31info, text='Service ceiling: 25,000 m', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingmig31.place(x=115, y=420)

gunmig31 = Label(mig31info, text='Guns: 1 × 30 mm Gryazev-Shipunov', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
gunmig31.place(x=115, y=500)

pointsmig31 = Label(mig31info, text='Hardpoints: 9 hardpoints', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
pointsmig31.place(x=115, y=580)

designmig31 = Label(mig31info, text='Design: Mikoyan and Gurevich Design Bureau', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
designmig31.place(x=115, y=660)

mig31.mainloop()
