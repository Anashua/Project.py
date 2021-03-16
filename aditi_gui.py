from tkinter import *
def checkbp():
    m=Tk()
    m.title('bp')
    m.geometry('500x500')
    m.configure(bg='red')


    la1=Label(m, text='welcome to BP calculator')
    la1.grid(row=1,column=2)

    la=Label(m, text='pressure=').grid(row=3,column=2)
    e1=Entry(m,width=20)
    e1.grid(row=3,column=3)

    def click():
        p=int(e1.get())
        if p<=90:
            mes='Your pressure is in the LOW region'
        elif p>90 and p<=120:
            mes='Your pressure is in the IDEAL region'
        elif p>120 and p<=140:
            mes='Your pressure is in the PRE-HYPERTENSION region'
        elif p>140 and p<=160:
            mes='Your systolic pressure is in the HIGH(STAGE 1 HYPERTENSION) region'
        elif p>160 and p<=7000:
            mes='Your systolic pressure is in the HIGH(STAGE 2 HYPERTENSION) region'
        ll=Label(m,text=mes)
        ll.grid(row=9,column=1)

    but=Button(m,text='click for result',command=click).grid(row=5,column=1)

    m.mainloop()