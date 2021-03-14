def body_mass_index():
    def bmi(w, h):
        return w / (h ** 2)

    def child(hei, wei):
        index = bmi(wei, hei)
        index = int(index * 10)
        val="indeterminate"
        category = {range(0, 5): 'Underweight', range(5, 85): 'Healthy weight', range(85, 95): 'At risk of overweight',
                    range(95, 7000): 'overweight'}
        for i in category.keys():
            if index in i:
                val= category[i]
        return  index,val
    def adult(heigh, weigh):
        index = bmi(weigh, heigh)
        index = int(index * 10)
        val="indeterminate"
        category = {range(0, 16): 'Severe Thinness', range(16, 17): 'Moderate thinness',
                    range(17, 19): 'Mild Thinness',
                    range(19, 25): 'normal', range(25, 30): 'overweight', range(30, 35): 'Obese Class 1 ',
                    range(35, 40): 'Obese Class 2', range(40, 1000): "Obese Class 3"}
        for i in category.keys():
            if index in i:
                val= category[i]
        return index,val

    with open("data.txt","r") as data:
        lis=list()
        for line in data:
            lis.append((line).split("\n"))
    age =int(lis[2][0])
    weight =int(lis[4][0])
    height = int(lis[3][0])/30.48
    if age in range(1, 18):
        bmi = child(height, weight)
    else:
        bmi = adult(height, weight)
    return bmi