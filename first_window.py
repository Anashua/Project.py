import second_window
from tkinter import *


def write_file():
    with open("data.txt", "w") as data_file:
        print(name_var.get(), file=data_file,flush=True)
        print(gender.get(), file=data_file,flush=True)
        print(age_var.get(), file=data_file,flush=True)
        print(height_var.get(), file=data_file,flush=True)
        print(weight_var.get(), file=data_file,flush=True)
        second_window.func()

main = Tk()
main.geometry("600x600")
main.title("Your Fitness Module")
main["padx"] = 10
# ADDING WELCOME LABEL
# messagebox.showinfo("Fitness Module","HI! , Welcome to your fitness module \n Please Enter the following details: ")
welcomeLabel = Label(main, text="HI! , Welcome to your fitness module \n Please Enter the following details: ")
welcomeLabel.grid(row=0, column=0, columnspan=3, sticky="n")
# CONFIGURING COLUMNS
main.columnconfigure(0, weight=10)
main.columnconfigure(1, weight=100)
main.columnconfigure(2, weight=10)
main.columnconfigure(3, weight=100)
main.columnconfigure(4, weight=1)
# CONFIGURING ROWS
main.rowconfigure(0, weight=10)
main.rowconfigure(1, weight=50)
main.rowconfigure(2, weight=50)
main.rowconfigure(3, weight=50)
main.rowconfigure(4, weight=50)
main.rowconfigure(5, weight=50)

# 2ND ROW
name_entryFrame = Frame(main).grid(column=0, row=1, columnspan=3)
nameLabel = Label(name_entryFrame, text="NAME :", width=10).grid(column=0, row=1, sticky="w")
name_var = StringVar()
nameEntry = Entry(name_entryFrame, width=20, textvariable=name_var).grid(column=1, row=1, columnspan=3, sticky="w")

# 3rd ROW
age_label = Label(main, text="AGE: ").grid(column=0, row=2, sticky="w")
age_var = StringVar()
age_var.set("18")
age_Entry = Entry(main, textvariable=age_var).grid(column=1, row=2, sticky="w")

gender_frame = Frame(main).grid(column=0, row=3)
gender = StringVar()
gender.set("Male")
gender_label = Label(gender_frame, text="Enter your gender").grid(row=2, column=2, sticky="w")
f_radio = Radiobutton(gender_frame, text="Female", value="Female", variable=gender).grid(row=3, column=2, sticky="nw")
m_radio = Radiobutton(gender_frame, text="Male", value="Male", variable=gender).grid(row=4, column=2, sticky="nw")

# height

height_label = Label(main, text="HEIGHT in cm: ").grid(column=0, row=3, sticky="w")
height_var = IntVar()
height_var.set(6)
height_Spinner = Spinbox(main, width=2, from_=60, to=300,textvariable=height_var).grid(column=1, row=3, sticky="w")

# weight

weight_label = Label(main, text="WEIGHT: ").grid(column=0, row=4, sticky="w")
weight_var = IntVar()
weight_var.set(60)
weight_Spinner = Spinbox(main, width=2, from_=1, to=400,textvariable=weight_var).grid(column=1, row=4, sticky="w")

okButton = Button(main, text=" NEXT ", command=write_file).grid(row=5, column=3, sticky="e")  #####
# #change destroy to quit or vice versa for errors
cancelButton = Button(main, text="Cancel", command=main.destroy).grid(row=5, column=3, sticky="se")

main.mainloop()
