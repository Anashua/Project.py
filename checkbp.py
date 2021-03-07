
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
