##Assignment: Dictionary in, tuples out

def makeTuples(dict):
	tupleList = []
	for key,val in dict.iteritems():
		tup = (key, val)
		tupleList += [tup]
	print tupleList


my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

makeTuples(my_dict)