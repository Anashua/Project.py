def bp():
	def blood(sys):	
		val="indeterminate"
		category = {range(0,90): 'Your systolic pressure is in the LOW region', 
                    range(90,120): 'Your systolic pressure is in the IDEAL region', 
                    range(120, 140):'Your systolic pressure is in the PRE-HYPERTENSION region', 
                    range(140, 160):'Your systolic pressure is in the HIGH(STAGE 1 HYPERTENSION) region',
                    range(160, 5000):'Your systolic pressure is in the HIGH(STAGE 2 HYPERTENSION) region'}
		for i in category.keys():
			if sys in i:
				val= category[i]
		return  sys,val
	def blo(dia):
		val="indeterminate"
		category={range(0,60):'Your diastolic pressure is in the LOW region', 
                  range(60,80):'Your diastolic pressure is in the IDEAL region', 
                  range(80,90):'Your diastolic pressure is in the PRE-HYPERTENSION region', 
                  range(90,100):'Your diastolic pressure is in the HIGH(STAGE 1 HYPERTENSION) region', 
                  range(100, 5000):'Your diastolic pressure is in the HIGH(STAGE 2 HYPERTENSION) region'}
		for i in category.keys():
			if dia in i:
				val= category[i]
		return dia,val

	with open("bp.txt","r") as data:
		lis=list()
		for line in data:
			lis.append((line).split("\n"))
	sys =int(lis[2][0])	
	dia =int(lis[4][0])
	s = blood(sys)
	d = blo(dia)
	return s,d
