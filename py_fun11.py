##Assignment: Stars

# v. 1
# def draw_stars(someList):
# 	for i in someList:
# 		print "*" * i

# x=[4,6,1,3,5,7,25]
# draw_stars(x)

# v. 2
def draw_stars(someList):
	for i in someList:
		if isinstance(i, str):
			print i[0].lower() * len(i)
		else:
			print "*" * i

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars(y)


