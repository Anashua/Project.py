from tkinter import *


def pulse():
    m = Tk()
    m.title('bp')
    m.geometry('500x500')
    m.configure(bg='purple')

    la = Label(m, text='welcome to pulse calculator')
    la.grid(row=1, column=2)

    l1 = Label(m, text='age=').grid(row=3, column=2)
    e1 = Entry(m, width=20)
    e1.grid(row=3, column=3)

    l2 = Label(m, text='resting heart rate=').grid(row=4, column=2)
    e2 = Entry(m, width=20)
    e2.grid(row=4, column=3)

    l3 = Label(m, text='lower limit of heart rate=').grid(row=5, column=2)
    e3 = Entry(m, width=20)
    e3.grid(row=5, column=3)

    l4 = Label(m, text='upper limit of heart rate=').grid(row=6, column=2)
    e4 = Entry(m, width=20)
    e4.grid(row=6, column=3)

    def onclick():
        # mn,mx=0
        age = int(e1.get())
        rhr = int(e2.get())
        lhr = int(e3.get())
        hhr = int(e4.get())
        maxhr = 206.9 - (0.67 * age)
        H = maxhr - rhr
        mn = (H * (lhr / 100)) + rhr
        mx = (H * (hhr / 100)) + rhr
        mes = 'your ideal pulse range is between' + str(mn) + 'and' + str(mx)
        lab = Label(m, text=mes)
        lab.grid(row=9, column=1)

    bu = Button(m, text='click for result', command=onclick).grid(row=5, column=1)
    m.mainloop()
