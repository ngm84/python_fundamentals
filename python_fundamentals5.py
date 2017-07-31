# Assignment: Compare Arrays

def compareArrays(arr1, arr2):
	equal = True
	if len(arr1) != len(arr2):
		equal = False
	else:
		for i in range(len(arr1)):
			if arr1[i] != arr2[i]:
				equal = False

	if equal == False:
		print "They are not the same."
	else:
		print "They are the same."
