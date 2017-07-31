## Assignment: String and List Practice

#Find and Replace
def findAndReplace():
	words = "It's thanksgiving day. It's my birthday, too!"
	print "First occurence of 'day' begins at index", words.find('day')
	more_words = words.replace('day','month')
	print more_words

#Min and Max
def minAndMax(someList):
	print "Min:", min(someList)
	print "Max:", max(someList)

x = [2,54,-2,7,12,98]
minAndMax(x)

#First and Last
def firstAndLast(myList):
	first = myList[0]
	print first
	last = myList[len(myList) - 1]
	print last
	newList = [first, last]
	print newList

y = ["hello",2,54,-2,7,12,98,"world"]
firstAndLast(y)

#New List
def newList(thisList):
	thisList.sort()
	half = len(thisList) / 2
	firstHalf = thisList[:half]
	lastHalf = thisList[half:]
	lastHalf.insert(0, firstHalf)
	print lastHalf


z = [19,2,54,-2,7,12,98,32,10,-3,6]
newList(z)

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