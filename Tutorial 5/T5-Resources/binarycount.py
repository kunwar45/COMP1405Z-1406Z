import math
def count(list, value):
    if (startVal:= findstart(list,value))!=-1: #using walrus operator to not call findstart again in the return statement
        return (findend(list,value) - startVal + 1)
    return -1

def findstart(list,value):
    start,end = 0,len(list)-1
    while start<=end:
        mid = int((start+end)/2)
        if (midVal := list[mid]) == value and (mid == start or list[mid-1]!= value): 
            return mid
        elif midVal >= value:
            end = mid-1
        elif midVal < value:
            start = mid+1
    return -1

def findend(list,value):
    start,end = 0,len(list)-1
    while start<=end:
        mid = math.ceil(((start+end)/2))
        if (midVal := list[mid]) == value and (mid == end or list[mid+1]!= value):
            return mid
        elif midVal > value:
            end = mid-1
        elif midVal <= value:
            start = mid+1
    return -1

import random
import time
repeat = 50000
maxval = 500
searchlist = []

for i in range(repeat):		
	searchlist.append(random.randint(0,maxval))
	
	searchnum = random.randint(0,maxval)
searchlist.sort()

print("Checking if equal")
if searchlist.count(searchnum) != count(searchlist, searchnum):
    
    print(searchlist.count(searchnum), count(searchlist, searchnum))
    exit()
else:
    print("Equal")

start = time.time()
for i in searchlist:
	searchlist.count(i)
end = time.time()
print("Linear time: ", (end-start))

start = time.time()
for i in searchlist:
	count(searchlist,i)
end = time.time()
print("binary search ", (end-start))
