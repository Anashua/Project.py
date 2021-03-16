from tkinter import *
def func():
    root = Tk()
    root.title("Hrmax")
    root.geometry("500x500")
    root['background'] = '#856ff8'


    label1 = Label(root, text="Welcome to HRmax calculator", bg="green")
    label1.grid(row=1, column=5)
    label2 = Label(root, text="Name:", bg="red").grid(row=3, column=2)
    entry1 = Entry(root, width=20)
    entry1.grid(row=3,column=3)
    label3 = Label(root, text="Age:", bg="red").grid(row=4, column=2)
    e=Entry(root, width=20)
    e.grid(row=4,column=3)
    def myclick1():
        message1="Your Hrmax is="
        message=220-int(e.get())
        lb4 = Label(root, text=message,bg="purple",fg="white")
        lb4.grid(row=11,column=3)
        lb3=Label(root,text=message1,bg="orange")
        lb3.grid(row=11,column=1)
    def myclick2():
        message=220-int(e.get())-10
        lb3=Label(root,text="Max heart rate=",bg="orange")
        lb3.grid(row=12,column=1)
        lb4=Label(root,text=message,bg="purple",fg="white")
        lb4.grid(row=12,column=3)
        message1=220-int(e.get())-30
        lb1=Label(root,text="Min heart rate=",bg="orange")
        lb1.grid(row=13,column=1)
        lb2=Label(root,text=message1,bg="purple",fg="white")
        lb2.grid(row=13,column=3)
    button4= Button(root,text="Click for HRmax Results",command=myclick1,bg="pink").grid(row=5,column=3)
    button5=Button(root,text="Click for Target heart rates during intervals",command=myclick2,bg="pink").grid(row=6,column=3)

    root.mainloop()
func()
"""label1=Label(root,text="Welcome to HRmax calculator",bg="green")
    label1.grid(row=1, column=2)
    label2=Label(root,text="Name:",bg="red").grid(row=3,column=2)
    entry1=Entry(root,width=20).grid(row=3,column=3)
    label3=Label(root,text="Age:",bg="red").grid(row=4,column=2)
    entry2 = Entry(root, width=20).grid(row=3, column=3)"""






'''from tkinter import *
#creating buttons
root = Tk() #creates a window

lb1 = Label(root, text = "Form")
lb1.pack()
#text box
e = Entry(root, width = 50)
e.pack()
e.insert(0, "Enter your name") #Default text to be displayed as a prompt
def myClick():
     message = "hello "+e.get()
     lb4 = Label(root, text = message)
     lb4.pack()

bt1 = Button(root, text = "Click Me!", command = myClick,bg = "blue",fg = "white")#callback
bt1.pack()

root.mainloop()'''







