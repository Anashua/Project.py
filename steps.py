from tkinter import*
import math
from tkinter import messagebox

def func_main():
    #GETTING THE DATA
    with open(r"C:\Users\HP\Desktop\Project.py\data.txt","r") as data:
        lis=list()
        for line in data:
            lis.append((line).split("\n"))
    height = int(lis[3][0])/30.48
    def stride():
        stride_len=30
        hei=int(height*10)
        dict={range(50,52):25,range(52,54):26,range(54,56):27,range(56,58):28,range(58,60):29,range(60,62):30,range(62,64):32,range(64,66):34,range(66,80):35}
        for i in dict:
            if hei in i :
                stride_len=dict[i]
        return stride_len
    def onClick():
        steps=str(math.floor(dist.get()**1.31125))
        val=Label(root,text="Steps walked are "+steps).grid(row=3,column=0)
        exit_button=Button(root,text="EXIT",command=root.destroy).grid(row=4,column=0)

    root=Tk()
    root.geometry("600x300")
    dist=IntVar()
    entry=Label(root,text="Enter distance walked in m").grid(row=0,column=0)
    entry_label=Entry(root,text="Enter distance walked in m",textvariable=dist).grid(row=1,column=0)
    entry_button=Button(root,text="Click here",command=onClick).grid(row=2,column=0)
    root.mainloop()