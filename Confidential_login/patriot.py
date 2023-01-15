from tkinter import *

patriot = Tk()

patriot.title("MIM-104 PATRIOT - Classified")
patriot.geometry('1280x720+100+65')
patriot.configure(bg="#fff")
patriot.resizable(False, False)

patriotframe = Frame(patriot, width=664, height=720, bg="white")
patriotframe.place(x=0, y=0)

patriotimg = PhotoImage(file="mimimg.png")
patriotpic = Label(patriotframe, image=patriotimg, bg="#fff")
patriotpic.place(x=0, y=0)

patriotinfo = Frame(patriot, width=616, height=720, bg="white")
patriotinfo.place(x=664, y=0)

heading = Label(patriotinfo, text='Anti-Ballistic Missile System', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=30, y=10)

lengthpatriot = Label(patriotinfo, text='Length: 5.34m', fg='#1a1a1a', bg='white',
                      font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthpatriot.place(x=30, y=100)

payloadmpatriot = Label(patriotinfo, text='Warhead weight: 90 kg', fg='#1a1a1a', bg='white',
                        font=('Microsoft YaHei UI Light', 20, 'bold'))
payloadmpatriot.place(x=30, y=180)

detonationpatriot = Label(patriotinfo, text='Detonation mechanism: Proximity fuse', fg='#1a1a1a', bg='white',
                          font=('Microsoft YaHei UI Light', 20, 'bold'))
detonationpatriot.place(x=30, y=260)

propellantpatriot = Label(patriotinfo, text='Propellant: Solid-fuel rocket', fg='#1a1a1a', bg='white',
                          font=('Microsoft YaHei UI Light', 20, 'bold'))
propellantpatriot.place(x=30, y=340)

altpatriot = Label(patriotinfo, text='Flight altitude: 24,200 m', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
altpatriot.place(x=30, y=420)

speedpatriot = Label(patriotinfo, text='Maximum speed : Mach 4.1', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
speedpatriot.place(x=30, y=500)

platformpatriot = Label(patriotinfo, text='Launch platform: 4 or 16 round semi-trailer', fg='#1a1a1a', bg='white',
                        font=('Microsoft YaHei UI Light', 20, 'bold'))
platformpatriot.place(x=30, y=580)

designpatriot = Label(patriotinfo, text='Design : Raytheon, Hughes, and RCA', fg='#1a1a1a', bg='white',
                      font=('Microsoft YaHei UI Light', 20, 'bold'))
designpatriot.place(x=30, y=660)

patriot.mainloop()
