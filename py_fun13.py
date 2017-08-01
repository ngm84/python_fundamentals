##Assignment: Names

# Part I

def printNames(roster):
	for i in roster:
		print i["first_name"], i["last_name"]


students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

printNames(students)

# Part II

def printFormat(newRoster):
	for key in newRoster:
		print key
		for val in newRoster[key]:
			print str(newRoster[key].index(val) + 1) + " - " + val["first_name"] + " " + val["last_name"] + " - " + str(len(val["first_name"] + val["last_name"]))


users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }
printFormat(users)