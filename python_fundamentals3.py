## Assignment: Filter by Type

def typeFilter(testThis):
	if isinstance(testThis, int):
		if testThis >= 100:
			print "That's a big number!"
		else:
			print "That's a small number"
	elif isinstance(testThis, str):
		if len(testThis) >= 50:
			print "Long sentence."
		else:
			print "Short sentence."
	elif isinstance(testThis, list):
		if len(testThis) >= 10:
			print "Big list!"
		else:
			print "Short list."

x = input("Type something > ")
typeFilter(x)