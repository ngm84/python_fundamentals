##Assignment: Scores and Grades

def scoresAndGrades():
	import random
	print "Scores and Grades"
	grade = ""
	for i in range(1, 11):
		#N.B. randint() is inclusive...
		score = random.randint(60, 100)
		if score >= 60 and score < 70:
			grade = "D"
		elif score >= 70 and score < 80:
			grade = "C"
		elif score >= 80 and score < 90:
			grade = "B"
		else:
			grade = "A"
		print "Score: " + str(score) + "; Your grade is " + grade
	print "End of the program. Bye!"

scoresAndGrades()