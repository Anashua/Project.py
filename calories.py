def calorie1():
    inp=1
    calorie={1:557,2:10,3:50,4:590,5:604}
    while inp==1:
        print("1.Cardio\n 2.Rest\n 3.Sleep\n4.Weight Training\n5.Cycling")
        ch = int(input("Enter your choice:\n"))
        if ch in calorie:
            print("Average calories burned during",end="")
            print(calorie[ch])
        else:
            print("Wrong input")
            inp=int(input("Do you want to continue?\n 1.Yes 2.No"))



