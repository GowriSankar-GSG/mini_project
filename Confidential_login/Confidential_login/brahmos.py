from tkinter import *

brahmos = Tk()

brahmos.title("BrahMos - Classified")
brahmos.geometry('1280x720+100+65')
brahmos.configure(bg="#fff")
brahmos.resizable(False, False)

brahmosframe = Frame(brahmos, width=405, height=720, bg="white")
brahmosframe.place(x=0, y=0)

brahmosimg = PhotoImage(file="brahmosimg.png")
brahmospic = Label(brahmosframe, image=brahmosimg, bg="#fff")
brahmospic.place(x=0, y=0)

brahmosinfo = Frame(brahmos, width=875, height=720, bg="white")
brahmosinfo.place(x=405, y=0)

heading = Label(brahmosinfo, text='Ramjet Supersonic Cruise Missile', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=115, y=10)

lengthbrahmos = Label(brahmosinfo, text='Length: 8.4 m', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthbrahmos.place(x=115, y=100)

massbrahmos = Label(brahmosinfo, text='Mass: 3,000 kg', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
massbrahmos.place(x=367, y=100)

payloadbrahmos = Label(brahmosinfo, text='Warhead: 300 kg', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
payloadbrahmos.place(x=115, y=180)

speedbrahmos = Label(brahmosinfo, text='Maximum speed:Mach 3+', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
speedbrahmos.place(x=115, y=260)

rangebrahmos = Label(brahmosinfo, text='Operational range : 500 km', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
rangebrahmos.place(x=115, y=340)

ceilingbrahmos = Label(brahmosinfo, text='Service ceiling: 15 km', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
ceilingbrahmos.place(x=115, y=420)

propellantbrahmos = Label(brahmosinfo, text='Propellant: 2 Stage', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
propellantbrahmos.place(x=115, y=500)

accuracybrahmos = Label(brahmosinfo, text='Accuracy:1 m', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
accuracybrahmos.place(x=115, y=580)

manufacturerbrahmos = Label(brahmosinfo, text='Manufacturer : DRDO of India, NPO Mashinostroyeniya', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
manufacturerbrahmos.place(x=115, y=660)

brahmos.mainloop()
