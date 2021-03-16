import bmi
import steps
from tkinter import *
from tkinter import messagebox
import heartRate
import  calories
import aditi_gui
def bmi_func():
    disp=bmi.body_mass_index()
    messagebox.showinfo("BMI is :",disp)

def func():
    main = Tk()
    main.geometry("500x500")
    main.title("Function window")
    main["padx"] = 15
    main.columnconfigure(0, weight=500)
    main.columnconfigure(1, weight=500)
    main.columnconfigure(2, weight=5)
    main.rowconfigure(0, weight=500)
    main.rowconfigure(1, weight=500)
    main.rowconfigure(2, weight=300)
    main.rowconfigure(3, weight=5)
    # HR MAX FRAME
    hrm_button=Button(main,text="Calculate \n HR Max",width=8).grid(column=0,row=0,sticky="nsew")

    # CALORIES FRAME
    cal_button=Button(main,text="Calculate \n Calories",width=8,command=calories.func).grid(column=1,row=0,sticky="nsew")#
    # Heart Rate FRAME
    hr_button=Button(main,text="Check Pulse",width=8,command=heartRate.pulse).grid(column=0,row=1,sticky="nsew")#

    # BMI FRAME
    bmi_button=Button(main,text="Calculate \n BMI",width=8,command=bmi_func).grid(column=1,row=1,sticky="nsew")#

    # CHECK_BP
    cbp_button=Button(main,text="Check \n BP",width=8,command=aditi_gui.checkbp).grid(column=0,row=2,sticky="nsew")

    # STEP_COUNTER
    sc_button=Button(main,text="Step \n Counter",width=8,command=steps.func_main).grid(column=1,row=2,sticky="nsew")

    #EXIT FUNCTION
    cancelButton = Button(main, text="EXIT", command=main.destroy).grid(row=3, column=0,columnspan=2, sticky="nsew")

    main.mainloop()
