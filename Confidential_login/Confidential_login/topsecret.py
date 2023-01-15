from tkinter import *

topsecret = Tk()

def rusecret():
    topsecret.destroy()
    import russia

def usasecret():
    topsecret.destroy()
    import usa

def cnsecret():
    topsecret.destroy()
    import china

def indsecret():
    topsecret.destroy()
    import india

topsecret.title("Confidential-Air Supremacy")
topsecret.geometry('1280x720+100+65')
topsecret.configure(bg="white")
topsecret.resizable(False, False)

russia = Frame(topsecret, width=320, height=720, bg="white")
russia.place(x=0, y=0)

russiaimg = PhotoImage(file="russia.png")
russiabutton = Button(russia, image=russiaimg, bg="#fff", bd=0, activebackground='white', cursor="hand2", command=rusecret)
russiabutton.place(x=9, y=10)

headingru = Label(russia, text='Country:\nRussian Federation', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 15, 'bold'))
headingru.place(x=63, y=325)
govermentru = Label(russia, text='Government:\nAuthoritarian Dictatorship', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 15, 'bold'))
govermentru.place(x=27, y=390)
arearu = Label(russia, text='Area:\n17,098,246+ Sq.Km.', fg='#1a1a1a', bg='white',
               font=('Microsoft YaHei UI Light', 15, 'bold'))
arearu.place(x=58, y=455)
forceru = Label(russia, text='Air Force:\nVVS Russian Aerospace Forces', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 15, 'bold'))
forceru.place(x=5, y=520)
yearru = Label(russia, text='Established on:\n25 December 1991', fg='#1a1a1a', bg='white',
               font=('Microsoft YaHei UI Light', 15, 'bold'))
yearru.place(x=65, y=585)
continentru = Label(russia, text='Continent:\nAsia', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 15, 'bold'))
continentru.place(x=105, y=650)

usa = Frame(topsecret, width=320, height=720, bg="white")
usa.place(x=320, y=0)

usaimg = PhotoImage(file="usa.png")
usabutton = Button(usa, image=usaimg, bg="#fff", bd=0, activebackground='white', cursor="hand2",command=usasecret)
usabutton.place(x=9, y=10)

headingusa = Label(usa, text='Country:\nUnited States of America', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 15, 'bold'))
headingusa.place(x=34, y=325)
govermentusa = Label(usa, text='Government:\nRepresentative Democracy', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 15, 'bold'))
govermentusa.place(x=24, y=390)
areausa = Label(usa, text='Area:\n9,833,520+ Sq.Km.', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 15, 'bold'))
areausa.place(x=64, y=455)
forceusa = Label(usa, text='Air Force:\nUnited States Air Force USAF', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 15, 'bold'))
forceusa.place(x=13, y=520)
yearusa = Label(usa, text='Established on:\n4 July 1776', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 15, 'bold'))
yearusa.place(x=82, y=585)
continentusa = Label(usa, text='Continent:\nNorth America', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 15, 'bold'))
continentusa.place(x=84, y=650)

china = Frame(topsecret, width=320, height=720, bg="white")
china.place(x=640, y=0)

chinaimg = PhotoImage(file="china.png")
chinabutton = Button(china, image=chinaimg, bg="#fff", bd=0, activebackground='white', cursor="hand2",command=cnsecret)
chinabutton.place(x=9, y=10)

headingcn = Label(china, text='Country:\nPeople\'s Republic of China', fg='#1a1a1a', bg='white',
                  font=('Microsoft YaHei UI Light', 15, 'bold'))
headingcn.place(x=24, y=325)
govermentcn = Label(china, text='Government:\nCommunist Dictatorship', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 15, 'bold'))
govermentcn.place(x=38, y=390)
areacn = Label(china, text='Area:\n9,596,961+ Sq.Km.', fg='#1a1a1a', bg='white',
               font=('Microsoft YaHei UI Light', 15, 'bold'))
areacn.place(x=66, y=455)
forcecn = Label(china, text='Air Force:\nPLA Air Force', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 15, 'bold'))
forcecn.place(x=89, y=520)
yearcn = Label(china, text='Established on:\n1 October 1949', fg='#1a1a1a', bg='white',
               font=('Microsoft YaHei UI Light', 15, 'bold'))
yearcn.place(x=82, y=585)
continentcn = Label(china, text='Continent:\nAsia', fg='#1a1a1a', bg='white',
                    font=('Microsoft YaHei UI Light', 15, 'bold'))
continentcn.place(x=105, y=650)

india = Frame(topsecret, width=320, height=720, bg="white")
india.place(x=960, y=0)

indiaimg = PhotoImage(file="india.png")
indiabutton = Button(india, image=indiaimg, bg="#fff", bd=0, activebackground='white', cursor="hand2",command=indsecret)
indiabutton.place(x=9, y=10)

headingind = Label(india, text='Country:\nRepublic of India', fg='#1a1a1a', bg='white',
                   font=('Microsoft YaHei UI Light', 15, 'bold'))
headingind.place(x=70, y=325)
govermentind = Label(india, text='Government:\nIndirect Democracy', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 15, 'bold'))
govermentind.place(x=57, y=390)
areaind = Label(india, text='Area:\n3,287,263+ Sq.Km.', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 15, 'bold'))
areaind.place(x=62, y=455)
forceind = Label(india, text='Air Force:\nIndian Air Force', fg='#1a1a1a', bg='white',
                 font=('Microsoft YaHei UI Light', 15, 'bold'))
forceind.place(x=75, y=520)
yearind = Label(india, text='Established on:\n15 August 1947', fg='#1a1a1a', bg='white',
                font=('Microsoft YaHei UI Light', 15, 'bold'))
yearind.place(x=80, y=585)
continentind = Label(india, text='Continent:\nAsia', fg='#1a1a1a', bg='white',
                     font=('Microsoft YaHei UI Light', 15, 'bold'))
continentind.place(x=105, y=650)

topsecret.mainloop()
