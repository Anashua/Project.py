def body_mass_index():
    def bmi(w, h):
        return w / (h ** 2)

    def child(hei, wei):
        index = bmi(wei, hei)
        index = index * 100
        category = {range(0, 5): 'Underweight', range(5, 85): 'Healthy weight', range(85, 95): 'At risk of overweight',
                    range(95, 7000): 'overweight'}
        for i in category.keys():
            if index in i:
                return category[i], index

    def adult(heigh, weigh):
        index = bmi(weigh, heigh)
        index = index * 100
        category = {range(0, 16): 'Severe Thinness', range(16, 17): 'Moderate thinness',
                    range(17, 19): 'Mild Thinness',
                    range(19, 25): 'normal', range(25, 30): 'overweight', range(30, 35): 'Obese Class 1 ',
                    range(35, 40): 'Obese Class 2', range(40, 1000): "Obese Class 3"}
        for i in category.keys():
            if index in i:
                return category[i], index

    print("Hi ! Welcome to BMI Calculator")
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

    if age in range(1, 18):
        bmi = child(height, weight)
    else:
        bmi = adult(height, weight)
    return bmi
