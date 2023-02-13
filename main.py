from tkinter import *
from playsound import playsound
import time
# first
class Timer:
    def __init__(self):
        self.root = Tk()
        self.root.title('Timer')
        self.root.config(bg='white')
        self.root.geometry('380x300+100+100')
        self.title = Label(
            self.root,
            text='Timer',
            font=('Arial 16 bold'),
            bg='brown',
            fg='#FF0')
        self.title.place(x = 150, y = 10)

        self.hrs = StringVar()
        self.hours_inp = Entry(self.root, textvariable=self.hrs, width=10, font='arial 50', bg='white', fg='black', bd=0)
        self.hrs.set('00')
        self.mins = StringVar()
        self.minutes_inp = Entry(self.root, textvariable=self.mins, width=10, font='arial 50', bg='white', fg='black', bd=0)
        self.mins.set('00')
        self.scs = StringVar()
        self.seconds_inp = Entry(self.root, textvariable=self.scs, width=50, font='arial 50', bg='white', fg='black', bd=0)
        self.scs.set('00')
        self.hours_inp.place(x = 30, y = 100)
        self.title = Label(
            self.root,
            text=':',
            font=('Arial 50 bold'),
            bg='white',
            fg='black')
        self.title.place(x=115, y=90)
        self.minutes_inp.place(x=150, y=100)
        self.title = Label(
            self.root,
            text=':',
            font=('Arial 50 bold'),
            bg='white',
            fg='black')
        self.title.place(x=235, y=90)
        self.seconds_inp.place(x=270, y=100)

        self.start = Button(self.root, text='start', font=('Arial', 12), bg='white', command = self.timer)
        self.stop = Button(self.root, text='stop', font=('Arial', 12), bg='white')

        self.start.place(x = 100, y = 200)
        self.stop.place(x = 200, y = 200)

        self.root.mainloop()
    def timer(self):
        times = int(self.hrs.get())*3600 + int(self.mins.get())*60 + int(self.scs.get())
        while times > -1:
            minutes, seconds = (times//60, times%60)
            hours = 0
            if minutes > 60:
                hours, minutes = (minutes // 60, minutes % 60)

            self.hrs.set(hours)
            self.mins.set(minutes)
            self.scs.set(seconds)

            self.root.update()
            time.sleep(1)

            if (times==0):
                self.scs.set('00')
                self.mins.set('00')
                self.hrs.set('00')

            times -= 1
n = Timer()
