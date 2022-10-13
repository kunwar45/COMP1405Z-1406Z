
def addend(list, dict, value):
	list.append(value)
	dict[value] = value
	
def removestart(list, dict):
	if len(list) == 0:
		return None

	last = list.pop(0)
	del dict[last]
		
	return last
	
def containslinear(list, value):
	return value in list

def containshash(dict, value):
	return value in dict.values()
	
