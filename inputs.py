age = input("Enter your age :")
    while not age.isnumeric():
        age = input("Enter your age : ")
        age = int(age)
    while age <= 0 or age >= 120:
        age = int(input("Enter your age : "))

weight = input("Enter your body weight in kg")
    while not weight.isnumeric():
        weight = input("Enter your body weight in kg : ")
    weight = int(weight)
    while weight <= 0:
        weight = int(input("Enter your body weight in kg"))

    height = input("Enter your body height in kg")
    while not height.isnumeric():
        height = input("Enter your body height in kg : ")
    height = int(height)
    while height <= 0:
        height = int(input("Enter your body height in kg"))
