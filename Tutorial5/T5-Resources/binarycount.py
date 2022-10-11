def count(list, value):
    if (findstart(list, value) != -1):
        return ((findend(list, value) - findstart(list, value)) + 1)
    return -1
def findstart(list, value):
    start, end = 0, len(list)-1

    while (start <= end):
        middle = int((start+end)/2)
        if ((list[middle] == value) and ((list[middle-1] != value) or (middle == start))):
            return list[middle]
        elif (list[middle] < value):
            start = middle + 1
        elif (list[middle] >= value):    
            end = middle -1
    
    return -1

def findend(list, value):
    start, end = 0, len(list)-1

    while (start <= end):
        middle = int((start+end)/2)
        if ((list[middle] == value) and ((list[middle+1] != value) or (middle == end))):
            return list[middle]
        elif (list[middle] <= value):
            start = middle + 1
        elif (list[middle] > value):    
            end = middle -1
    
    return -1