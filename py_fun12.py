##Assignment: Making and Reading from Dictionaries

def printDict(dict):
	for key, value in dict.iteritems():
		print "My",key,"is",value

about_me = {"name":"Nate", "age":"111", "country of birth":"USA", "favorite language":"Python"}

printDict(about_me)