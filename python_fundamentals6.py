## Assignment: Find Chars

def findChars(wordList, char):
	new_list = []
	for i in wordList:
		if char in i:
			new_list.append(i)
	print new_list

x = ['hello','world','my','name','is','Anna']
findChars(x, 'o')
