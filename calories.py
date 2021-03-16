from tkinter import *
def func():
    root=Tk()
    root.title("Calorie")
    root.geometry("800x500")
    root['background'] = '#856ff8'
    def cardio():
        message = "Calories burnt is 557 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message,bg="purple",fg="white")
        label2.grid(row=6,column=6)
    def rest():
        message = "Calories burnt is 10 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message,bg="purple",fg="white")
        label2.grid(row=7,column=6)
    def sleep():
        message = "Calories burnt is 50 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message,bg="purple",fg="white")
        label2.grid(row=8,column=6)
    def wt():
        message = "Calories burnt is 590 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message,bg="purple",fg="white")
        label2.grid(row=9,column=6)
    def cycle():
        message = "Calories burnt is 604 per hour"  # GET RETURNS THE CURRENT STRING THE USER ENTERS
        label2 = Label(root, text=message,bg="purple",fg="white")
        label2.grid(row=10,column=6)
    mylabel=Label(root,text="Welcome to Calorie predictor",bg="red",fg="green")
    mylabel.grid(row=1,column=1000)
    welcome=Label(root,text="Please click on the following buttons to check calories burned per hour",bg="blue")
    welcome.grid(row=5,column=2)
    button1=Button(root,text="Cardio",command=cardio,bg="pink")
    button1.grid(row=6,column=0)
    button2=Button(root,text="Rest",command=rest,bg="pink")
    button2.grid(row=7,column=0)
    button3=Button(root,text="Sleep",command=sleep,bg="pink")
    button3.grid(row=8,column=0)
    button4=Button(root,text="Weight Training",command=wt,bg="pink")
    button4.grid(row=9,column=0)
    button5=Button(root,text="Cycling",command=cycle,bg="pink")
    button5.grid(row=10,column=0)
    root.mainloop()

func()