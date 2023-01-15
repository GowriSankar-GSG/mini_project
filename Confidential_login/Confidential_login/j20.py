from tkinter import *

j20 = Tk()

j20.title("CHENGDU J-20 - Classified")
j20.geometry('1280x720+100+65')
j20.configure(bg="#fff")
j20.resizable(False, False)

j20frame = Frame(j20, width=631, height=720, bg="white")
j20frame.place(x=0, y=0)

j20img = PhotoImage(file="j20img.png")
j20pic = Label(j20frame, image=j20img, bg="#fff")
j20pic.place(x=0, y=0)

j20info = Frame(j20, width=649, height=720, bg="white")
j20info.place(x=631, y=0)

heading = Label(j20info, text='Air Superiority Fighter', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthj20 = Label(j20info, text='Length: 21.2 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthj20.place(x=115, y=100)

spanj20 = Label(j20info, text='Wingspan: 13.01 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
spanj20.place(x=367, y=100)

weightj20 = Label(j20info, text='Gross weight: 25,000 kg', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
weightj20.place(x=115, y=180)

speedj20 = Label(j20info, text='Maximum speed: Mach 2.0', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
speedj20.place(x=115, y=260)

rangej20 = Label(j20info, text='Range: 5,500 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangej20.place(x=115, y=340)

ceilingj20 = Label(j20info, text='Service ceiling: 20,000 m', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingj20.place(x=115, y=420)

payloadj20 = Label(j20info, text='Maximum weapon capacity: 11,000 kg', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
payloadj20.place(x=115, y=500)

fuelj20 = Label(j20info, text='Fuel capacity: 12,000 kg', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
fuelj20.place(x=115, y=580)

designj20 = Label(j20info, text='Design:Chengdu Aircraft Industry Group', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
designj20.place(x=115, y=660)

j20.mainloop()
