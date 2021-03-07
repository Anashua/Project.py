from math import trunc
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
