from tkinter import *

avangard = Tk()

avangard.title("AVANGARD - Classified")
avangard.geometry('1280x720+100+65')
avangard.configure(bg="#fff")
avangard.resizable(False, False)

avangardframe = Frame(avangard, width=600, height=720, bg="white")
avangardframe.place(x=0, y=0)

avangardimg = PhotoImage(file="avangardplan.png")
avangardpic = Label(avangardframe, image=avangardimg, bg="#fff")
avangardpic.place(x=0, y=0)

avangardinfo = Frame(avangard, width=680, height=720, bg="white")
avangardinfo.place(x=600, y=0)

heading = Label(avangardinfo, text='Hypersonic Glide Vehicle', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthavangard = Label(avangardinfo, text='Length: 5.4 m', fg='#1a1a1a', bg='white',
                       font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthavangard.place(x=115, y=100)

weightavangard = Label(avangardinfo, text='Gross weight: 2,000 kg', fg='#1a1a1a', bg='white',
                       font=('Microsoft YaHei UI Light', 20, 'bold'))
weightavangard.place(x=367, y=100)

speedavangard = Label(avangardinfo, text='Maximum speed: Mach 27', fg='#1a1a1a', bg='white',
                      font=('Microsoft YaHei UI Light', 20, 'bold'))
speedavangard.place(x=115, y=180)

rangeavangard = Label(avangardinfo, text='Range: 6,000', fg='#1a1a1a', bg='white',
                      font=('Microsoft YaHei UI Light', 20, 'bold'))
rangeavangard.place(x=115, y=260)

classavangard = Label(avangardinfo, text='Class: Hypersonic Glide Vehicle (HGV)', fg='#1a1a1a', bg='white',
                        font=('Microsoft YaHei UI Light', 20, 'bold'))
classavangard.place(x=115, y=340)

payloadavangard = Label(avangardinfo, text='Payload: Conventional and Nuclear', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
payloadavangard.place(x=115, y=420)

yieldavangard = Label(avangardinfo, text='Blast yield: 0.8–2 Mt', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
yieldavangard.place(x=115, y=500)

designavangard = Label(avangardinfo, text='Design:Moscow Institute of Thermal Tech.', fg='#1a1a1a', bg='white',
                       font=('Microsoft YaHei UI Light', 20, 'bold'))
designavangard.place(x=115, y=580)

avangard.mainloop()
