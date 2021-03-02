def hrmax():
    print("Welcome to HRmax calculator")
    print("1.Male\n2.Female")
    cho=int(input("Enter your option:"))
    age=int(input("Enter your age:"))
    hgh=int(input("Enter your height(cm):"))
    wgt=int(input("Enter your weight(kgs):"))
    def male(age,hgh,wgt):
        Hrmax=220-age
        upperi= Hrmax-10
        loweri= Hrmax-30
        upperar= Hrmax-50
        lowerar=Hrmax-70
        ##""c=bmi(age,hgh,wgt)""
        print("Your HRmax is calculated to be ",Hrmax)
        ##print("Your BMI is calculated to be ",c)
        print("Your target heart rates for interval training are:\nDuring intervals :")
        print(upperi,"-",loweri)
        print("During active rest:\n")
        print(upperar,"-",lowerar)


    def female(age, hgh, wgt):
        Hrmax = 220 - age
        upperi = Hrmax - 10
        loweri = Hrmax - 30
        upperar = Hrmax - 50
        lowerar = Hrmax - 70
        ##""c=bmi(age,hgh,wgt)""
        print("Your HRmax is calculated to be ", Hrmax)
        ##print("Your BMI is calculated to be ",c)
        print("Your target heart rates for interval training are:\nDuring intervals :")
        print(upperi, "-", loweri)
        print("During active rest:")
        print(upperar, "-", lowerar)


    if cho==1:
        male(age,hgh,wgt)
    elif cho==2:
        female(age,hgh,wgt)
    else:
        print("Entered wrong option")




