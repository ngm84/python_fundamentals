
## Assignment: Multiples, Sum, Average

#Multiples Part I
def multiplesI():
	for num in range(1, 1000):
		if num % 2 != 0:
			print num

#Multiples Part II
multiplesI()

def multiplesII():
	for num in range(5, 1000000):
		if num % 5 == 0:
			print num

multiplesII()

#Sum List
def sumList(listy):
	sum = 0;
	# looping over the list, getting a *COPY* of each element --
	# can't use this syntax to actually change values in a list
	for i in listy:
		# Testing to make sure i is an int and can be math'd
		if type(i) == int:
			sum += i
	print sum

x = [1, 2, 5, 10, 255, 3]
sumList(x)

#Average List
def averageList(listo):
	sum = 0;
	for i in listo:
		if type(i) == int:
			sum += i
	print sum / len(listo)

a = [1, 2, 5, 10, 255, 3]
averageList(a)