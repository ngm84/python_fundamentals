#Optional Assignment: Multiplication Table
import pprint

#I got this to work, but I don't completely understand multidimensional lists/arrays...
def multTable():
	#got this "comprehension" from stack overflow...
	table = [[i for i in range(0, 13)] for i in range(0, 13)]
	for k in range(0, 13):
		table[k][0] = k
	table[0][0] = 'x'
	#this was an intuitive leap.
	for x in range(1, 13):
		for z in range(1, 13):
			table[x][z] = x * z

	pprint.pprint(table)

multTable()
