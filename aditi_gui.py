import proj
from tkinter import *

r=Tk()
l=Label(r, text='Hello! Enter following details to check your pulse rate:')
l.grid(row=0, column=7)

ln=Label(r, text='Age')
ln.place(x=540,y=20)

ln2=Label(r, text='Resting heart rate')
ln2.place(x=470,y=35)

ln3=Label(r, text='Low end heart rate')
ln3.place(x=460,y=55)

ln4=Label(r, text='High end heart rate zone')
ln4.place(x=470,y=75)

ln5=Label(r, text='Gender: 1-female; 2-male')
ln5.place(x=520,y=95)


e1=Entry(r)
e1.grid(row=2, column=20)

e2=Entry(r)
e2.grid(row=3, column=20)

e3=Entry(r)
e3.grid(row=4, column=20)

e4=Entry(r)
e4.grid(row=5, column=20)

e5=Entry(r)
e5.grid(row=6, column=20)


def getinput():
    age = e1.get()
    rhr = e2.get()
    lhr = e3.get()
    hhr = e4.get()
    gen = e5.get()
    proj.calc(age, rhr, lhr, hhr, gen)

mb=Button(r, text="submit",command = getinput)
mb.grid()

r.mainloop()
