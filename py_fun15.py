#Assignment: Making Dictionaries

def make_dict(arr1, arr2):
	if len(arr2) > len(arr1):
		new_dict = dict(zip(arr2, arr1))
	else:
		new_dict = dict(zip(arr1, arr2))
	return new_dict

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

a = make_dict(name, favorite_animal)
print a

country = ["UK", "USA", "France", "Japan"]
capital = ["London", "Washington", "Paris", "Tokyo", "King's Landing"]

b = make_dict(country, capital)
print b