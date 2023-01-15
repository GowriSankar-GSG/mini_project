from tkinter import *

df41 = Tk()

df41.title("DONGFENG-41 - Classified")
df41.geometry('1280x720+100+65')
df41.configure(bg="#fff")
df41.resizable(False, False)

df41frame = Frame(df41, width=576, height=720, bg="white")
df41frame.place(x=0, y=0)

df41img = PhotoImage(file="df41img.png")
df41pic = Label(df41frame, image=df41img, bg="#fff")
df41pic.place(x=0, y=0)

df41info = Frame(df41, width=766, height=720, bg="white")
df41info.place(x=576, y=0)

heading = Label(df41info, text='Intercontinental Ballistic Missile', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=60, y=10)

lengthdf41 = Label(df41info, text='Length: 21 metres', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthdf41.place(x=60, y=100)

massdf41 = Label(df41info, text='Mass: 80,000 kg', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
massdf41.place(x=367, y=100)

payloaddf41 = Label(df41info, text='Payload: 2,500 kg', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
payloaddf41.place(x=60, y=180)

diamdf41 = Label(df41info, text='Diameter:2.25 m', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
diamdf41.place(x=60, y=260)

rangedf41 = Label(df41info, text='Range :13,000 kilometres', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangedf41.place(x=60, y=340)

speeddf41 = Label(df41info, text='Maximum speed: Mach 25', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
speeddf41.place(x=60, y=420)

propdf41 = Label(df41info, text='Propellant Config. : 3 stages', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
propdf41.place(x=60, y=500)

payheaddf41 = Label(df41info, text='Warhead:Thermonuclear weapon', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
payheaddf41.place(x=60, y=580)

manufacturerdf41 = Label(df41info, text='Manufacturer:China Academy of Launch Vehicle', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
manufacturerdf41.place(x=60, y=660)

df41.mainloop()
