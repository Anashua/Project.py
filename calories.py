from tkinter import *
def func():
    root=Tk()
    root.title("Calorie")
    root.geometry("500x500")
    root.configure(bg='red')
    def cardio():
        message = "Calories burnt is 557 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message)
        label2.grid(row=2,column=1)
    def rest():
        message = "Calories burnt is 10 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message)
        label2.grid(row=3,column=1)
    def sleep():
        message = "Calories burnt is 50 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message)
        label2.grid(row=4,column=1)
    def wt():
        message = "Calories burnt is 590 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message)
        label2.grid(row=5,column=1)
    def cycle():
        message = "Calories burnt is 604 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message)
        label2.grid(row=6,column=1)
    mylabel=Label(root,text="Welcome to Calorie predictor",bg="red",fg="white")
    mylabel.grid(row=0,column=1000)
    button1=Button(root,text="Cardio",command=cardio,bg="blue",fg="white")
    button1.grid(row=2,column=0)
    button2=Button(root,text="Rest",command=rest,bg="blue",fg="white")
    button2.grid(row=3,column=0)
    button3=Button(root,text="Sleep",command=sleep,bg="blue",fg="white")
    button3.grid(row=4,column=0)
    button4=Button(root,text="Weight Training",command=wt,bg="blue",fg="white")
    button4.grid(row=5,column=0)
    button5=Button(root,text="Cycling",command=cycle,bg="blue",fg="white")
    button5.grid(row=6,column=0)
    root.mainloop()

#