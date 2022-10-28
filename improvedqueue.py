def addend(list, dict, value):
	list.append(value)
	dict[value] = (dict[value] + 1) if value in dict else 1

def removestart(list, dict):
	if len(list) == 0 or len(dict) == 0:
		return None
	dict[(removed_val:= list.pop(0))]-=1
	return removed_val
	
def containslinear(list, value):
	return value in list

def containshash(dict,value):
	if value in dict:
		return not (dict[value] == 0)
	return False