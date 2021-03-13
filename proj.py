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
	def BP():
		sys=0
		dia=0
		sys=(msys+asys)/2
		dia=(mdia+adia)/2
		return sys, dia
	
	index1, index2=BP()
		
	cat={range(0,90): 'Your systolic pressure is in the LOW region', range(90,120): 'Your systolic pressure is in the IDEAL region', range(120, 140):'Your systolic pressure is in the PRE-HYPERTENSION region', range(140, 160):'Your systolic pressure is in the HIGH(STAGE 1 HYPERTENSION) region', range(160, 300):'Your systolic pressure is in the HIGH(STAGE 2 HYPERTENSION) region'}	
	for i in cat.keys():
		if index1 in i:
        	print(i)
	     
	   
	cat2={range(0,60):'Your diastolic pressure is in the LOW region', range(60,80):'Your diastolic pressure is in the IDEAL region', range(80,90):'Your diastolic pressure is in the PRE-HYPERTENSION region', range(90,100):'Your diastolic pressure is in the HIGH(STAGE 1 HYPERTENSION) region', range(100, 500):'Your diastolic pressure is in the HIGH(STAGE 2 HYPERTENSION) region'}
	for i in cat2.keys():
	     if index2 in i:
            print(i)   
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


