from tkinter import *

su57 = Tk()

su57.title("SUKHOI SU-57 - Classified")
su57.geometry('1280x720+100+65')
su57.configure(bg="#fff")
su57.resizable(False, False)

su57frame = Frame(su57, width=514, height=720, bg="white")
su57frame.place(x=0, y=0)

su57img = PhotoImage(file="su.png")
su57pic = Label(su57frame, image=su57img, bg="#fff")
su57pic.place(x=0, y=0)

su57info = Frame(su57, width=766, height=720, bg="white")
su57info.place(x=515, y=0)

heading = Label(su57info, text='Twin engine multi-role fighter', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthsu57 = Label(su57info, text='Length: 20.1 m', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthsu57.place(x=115, y=100)

weightsu57 = Label(su57info, text='Gross weight: 25,000 kg', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
weightsu57.place(x=367, y=100)

fuelsu57 = Label(su57info, text='Fuel capacity: 10,300 kg', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
fuelsu57.place(x=115, y=180)

speedsu57 = Label(su57info, text='Maximum speed: Mach 2', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
speedsu57.place(x=115, y=260)

rangesu57 = Label(su57info, text='Range: 3,500 km', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
rangesu57.place(x=115, y=340)

ceilingsu57 = Label(su57info, text='Service ceiling: 20,000 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingsu57.place(x=115, y=420)

gunsu57 = Label(su57info, text='Guns: 1 × 30 mm Gryazev-Shipunov', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 20, 'bold'))
gunsu57.place(x=115, y=500)

pointsu57 = Label(su57info, text='Hardpoints: 12 hardpoints', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 20, 'bold'))
pointsu57.place(x=115, y=580)

designsu57 = Label(su57info, text='Design: JSC Sukhoi Company', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
designsu57.place(x=115, y=660)

su57.mainloop()
