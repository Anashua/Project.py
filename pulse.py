def pulse():
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



	with open("pulse.txt","r") as data:
		ls1=list()
		for line in data:
			ls1.append((line).split("\n"))
	age =int(ls1[2][0])
	rhr =int(ls1[3][0])
	lhr =int(ls1[4][0])
	hhr =int(ls1[5][0])
	gen =int(ls1[6][0])
	m1,m2=calc(age, rhr, lhr, hhr, gen)
	return m1, m2
