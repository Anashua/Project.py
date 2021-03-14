from tkinter import *
from tkinter import messagebox
def func_main():
    #GETTING THE DATA
    with open("data.txt","r") as data:
        lis=list()
        for line in data:
            lis.append((line).split("\n"))

    height = int(lis[3][0])
    gender=lis[1][0]

    def onClick():
        steps=dist.get()//stride()
        messagebox.showinfo("Steps walked are",steps)
        exit_button=Button(root,text="EXIT",command=root.destroy).grid(row=3,column=0)

    def stride():
        if gender=="Female":
            return 12*height*0.413
        else:
            return 12*height*0.415
    root=Tk()
    root.geometry("600x300")
    dist=IntVar()
    entry=Label(root,text="Enter distance walked in m").grid(row=0,column=0)
    entry_label=Entry(root,text="Enter distance walked in m",textvariable=dist).grid(row=1,column=0)
    entry_button=Button(root,text="Click here",command=onClick).grid(row=2,column=0)
    root.mainloop()
func_main()