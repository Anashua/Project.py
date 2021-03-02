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


def steps():
    state = input("True if walking , False if not ").capitalize()
    move = False
    if state == 'True' or 'T' or 'Yes' or 'Y' or 'TRUE' or 'YES':
        move = True
    elif state == 'False' or 'F' or 'No' or 'N' or 'FALSE' or 'NO':
        move = False
    count = 0
    res = 0
    while move:
        count += 1
        res += 1
        state = input("True if walking , False if not ").capitalize()
        if state == 'False' or 'F' or 'No' or 'N' or 'FALSE' or 'NO':
            move = False
        if res == 10:
            res = 0
            print(count * 50, " STEPS TAKEN !!!")
    print("Steps take are ", count * 50)

    return count * 50
steps()
body_mass_index()





from math import trunc

def checkbp():
	print('HELLO! Welcome to BP check!')

	msys=input('Enter systolic pressure (morning):')
	while not msys.isnumeric():
		msys=input('Enter systolic pressure (morning):')
	msys=int(msys)

	mdia=input('Enter diastolic pressure (morning):')
	while not mdia.isnumeric():
		mdia=input('Enter systolic pressure (morning):')
	mdia=int(mdia)
	
	asys=input('Enter systolic pressure (afternoon):')
	while not asys.isnumeric():
		asys=input('Enter systolic pressure (morning):')
	asys=int(asys)

	adia=input('Enter diastolic pressure (afternoon):')
	while not adia.isnumeric():
		adia=input('Enter systolic pressure (morning):')
	adia=int(adia)
	
	sys=0
	dia=0
	sys=(msys+asys)/2
	dia=(mdia+adia)/2

	if(sys>=70 and sys<=90):
		print('Your systolic pressure is in the LOW region')
	elif(sys>=91 and sys<=120):
		print('Your systolic pressure is in the IDEAL region')
	elif(sys>=121 and sys<=140):
		print('Your systolic pressure is in the PRE-HYPERTENSION region')
	elif (sys >= 141 and sys <= 160):
		print('Your systolic pressure is in the HIGH(STAGE 1 HYPERTENSION) region')
	elif (sys >= 161):
		print('Your systolic pressure is in the HIGH(STAGE 2 HYPERTENSION) region')

	if (dia>=40 and dia<=60):
		print('Your diastolic pressure is in the LOW region')
	elif (dia>=61 and dia<=80):
		print('Your diastolic pressure is in the IDEAL region')
	elif (dia>=81 and dia<=90):
		print('Your diastolic pressure is in the PRE-HYPERTENSION region')
	elif (dia >= 91 and dia <= 100):
		print('Your diastolic pressure is in the HIGH(STAGE 1 HYPERTENSION) region')
	elif (dia >= 101):
		print('Your diastolic pressure is in the HIGH(STAGE 2 HYPERTENSION) region')

checkbp()



def calc(age, rhr, lhr, hhr, gen):
	if gen == 1:
		maxhr = 206.9-(0.67*age)
		H = maxhr-rhr
		mn = (H*(lhr/100))+rhr	
		mx = (H*(hhr/100))+rhr
		return mn, mx
	elif gen == 2:
		maxhr = 206.9-(0.88*age)
		H = maxhr-rhr
		mn = (H*(lhr/100))+rhr
		mx = (H*(hhr/100))+rhr
		return mn, mx
	   

age=input('enter your age:')
while not age.isnumeric():
	age=input('enter your age:')
age=int(age)

rhr=input('enter your resting heart rate:')
while not rhr.isnumeric():
	rhr=input('enter your resting heart rate:')
rhr=int(rhr)

lhr=input('enter lower limit of heart rate:')
while not lhr.isnumeric():
	lhr=input('enter lower limit of heart rate:')
lhr=int(lhr)

hhr=input('enter upper limit of heart hate:')
while not hhr.isnumeric():
	hhr=input('enter upper limit of heart hate:')
hhr=int(hhr)

gen=input('enter your gender[1-male; 2-female] :')
while not gen.isnumeric():
	gen=input('enter your gender[1-male; 2-female] :')
gen=int(gen)

mn, mx=calc(age, rhr, lhr, hhr, gen)

print('Ideal pulse rate is between', trunc(mn), 'and', trunc(mx))

















