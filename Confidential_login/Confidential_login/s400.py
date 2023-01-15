from tkinter import *

s400 = Tk()

s400.title("S-400 Triumf - Classified")
s400.geometry('1280x720+100+65')
s400.configure(bg="#fff")
s400.resizable(False, False)

s400frame = Frame(s400, width=664, height=720, bg="white")
s400frame.place(x=0, y=0)

s400img = PhotoImage(file="s400plan.png")
s400pic = Label(s400frame, image=s400img, bg="#fff")
s400pic.place(x=0, y=0)

s400info = Frame(s400, width=616, height=720, bg="white")
s400info.place(x=664, y=0)

heading = Label(s400info, text='Surface-to-Air missile system', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=30, y=10)

tspeed400 = Label(s400info, text='Maximum target speed: Mach 14', fg='#1a1a1a', bg='white',
                       font=('Microsoft YaHei UI Light', 20, 'bold'))
tspeed400.place(x=30, y=100)

ddistance400 = Label(s400info, text='Target detection distance: 600 km', fg='#1a1a1a', bg='white',
                      font=('Microsoft YaHei UI Light', 20, 'bold'))
ddistance400.place(x=30, y=180)

starget400 = Label(s400info, text='No. of simultaneously engaged targets: 80', fg='#1a1a1a', bg='white',
                      font=('Microsoft YaHei UI Light', 20, 'bold'))
starget400.place(x=30, y=260)

sgtargets400 = Label(s400info, text='No. of simultaneously guided missiles : 160', fg='#1a1a1a', bg='white',
                        font=('Microsoft YaHei UI Light', 20, 'bold'))
sgtargets400.place(x=30, y=340)

payloads400 = Label(s400info, text='Ready for operation on a signal: 5 min', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
payloads400.place(x=30, y=420)

yields400 = Label(s400info, text='Ready for operation from standby : 35 sec', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
yields400.place(x=30, y=500)

designs400 = Label(s400info, text='Design:Almaz-Antey Corporation', fg='#1a1a1a', bg='white',
                       font=('Microsoft YaHei UI Light', 20, 'bold'))
designs400.place(x=30, y=580)

s400.mainloop()
