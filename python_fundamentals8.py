##Assignment: Fun with Functions

#Odd Even
def odd_even():
	for i in range(1, 2001):
		oddeven = 'odd'
		if i % 2 == 0:
			oddeven = 'even'
		print "Number is " + str(i) + ". This is an " + oddeven + " number."

#odd_even()

#Multiply
def multiply(someList, times):
	newList = []
	for i in someList:
		newList += [i * times]
	return newList

a = [2,4,10,16]
b = multiply(a, 5)
print b

#Hacker Challenge
def layered_multiples(arr):
	new_array = []
	for i in arr:
		new_array += [[1] * i]

	return new_array

x = layered_multiples(multiply([2,4,5],3))
print x