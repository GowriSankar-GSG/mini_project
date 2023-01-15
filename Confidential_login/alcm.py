from tkinter import *

alcm = Tk()

alcm.title("AGM-86 ALCM - Classified")
alcm.geometry('1280x720+100+65')
alcm.configure(bg="#fff")
alcm.resizable(False, False)

alcmframe = Frame(alcm, width=664, height=720, bg="white")
alcmframe.place(x=0, y=0)

alcmimg = PhotoImage(file="alcmimg.png")
alcmpic = Label(alcmframe, image=alcmimg, bg="#fff")
alcmpic.place(x=0, y=0)

alcminfo = Frame(alcm, width=616, height=720, bg="white")
alcminfo.place(x=664, y=0)

heading = Label(alcminfo, text='Air-to-Ground cruise missile', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 30, 'bold'))
heading.place(x=30, y=10)

tspeedalcm = Label(alcminfo, text='Maximum speed:890 km/h', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
tspeedalcm.place(x=30, y=100)

massalcm = Label(alcminfo, text='Mass : 1,430 kg', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 20, 'bold'))
massalcm.place(x=30, y=180)

lengthalcm = Label(alcminfo, text='Length:6.3 m', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
lengthalcm.place(x=30, y=260)

warheadalcm = Label(alcminfo, text='Warhead:W80 thermonuclear weapon', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
warheadalcm.place(x=30, y=340)

rangealcm = Label(alcminfo, text='Operational range : 2,400+ km', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 20, 'bold'))
rangealcm.place(x=30, y=420)

payloadalcm = Label(alcminfo, text='Warhead weight : 1362kg', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 20, 'bold'))
payloadalcm.place(x=30, y=500)

platformalcm = Label(alcminfo, text='Launch platform: B-52H Stratofortress', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 20, 'bold'))
platformalcm.place(x=30, y=580)

designalcm = Label(alcminfo, text='Design:Boeing Integrated Defence Systems', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 20, 'bold'))
designalcm.place(x=30, y=660)

alcm.mainloop()
