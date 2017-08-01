##Assignment: Coin Tosses

def coinToss():
	import random
	heads_count = 0
	tails_count = 0
	for i in range(1, 5001):
		result = "head"
		attempt = round(random.random())
		if attempt == 0:
			result = "tail"
			tails_count += 1
		else:
			heads_count += 1
		print "Attempt #" + str(i) + ": Throwing a coin... It's a " + result + "! ... Got " + str(heads_count) + " head(s) so far and " + str(tails_count) + " tail(s) so far"
	print "Ending the program, thank you!"

coinToss()