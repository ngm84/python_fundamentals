## Assignment: Type List

def typeList(myList):
	listType = ''
	strBucket = []
	intSum = 0
	strIntCount = 0
	strIntSum = 0
	listList = []

	for i in myList:
		if isinstance(i, str):
			if listType == '':
				listType = 'string'
			else:
				listType = 'mixed'
			strBucket.append(i)
			if i.replace(' ', '').isalpha() == False:
				strIntSum += int(i)
		elif isinstance(i, int):
			if listType == 'string' or listType == 'list':
				listType = 'mixed'
			else:
				listType = 'integer'
			intSum += i
		elif isinstance(i, list):
			if listType == '' and listType != 'string' and listType != 'integer' and listType != 'mixed':
				listType = 'list'
			listList.extend(i)

	print "The list you entered is of " + listType + " type."
	if listType == 'mixed':
		if len(strBucket) > 0:
			print "String:", " ".join(strBucket)
			if strIntSum > 0:
				print "You had some numeric strings: Sum:", strIntSum
		if intSum > 0:
			print "Sum:", intSum
		if len(listList) > 0:
			print "You even had some lists!", listList
	elif listType == "string":
			print "String:", " ".join(strBucket)
			if strIntSum > 0:
				print "You had some numeric strings: Sum:", strIntSum
	elif listType == 'integer':
			print "Sum:", intSum
	elif listType == 'list':
		print "Wow! Lists!", listList

x = input("Type something > ")

typeList(x)

