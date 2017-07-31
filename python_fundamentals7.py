## Assignment: Checkerboard

def Checkerboard():
	odd = "* * * * "
	even = " * * * *"
	for i in range(1, 9):
		if i % 2 == 0:
			print even
		else:
			print odd

Checkerboard()