import math
def count(list, value):
    if (startVal:= findstart(list,value))!=-1: #using walrus operator to not call findstart again in the return statement
        return (findend(list,value) - startVal + 1)
    return 0

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
searchlistX = []
searchlistY = []

for i in range(int(repeat/20)):
	searchlistX.append(random.randint(0,maxval))

for i in range(repeat):		
	searchlistY.append(random.randint(0,1*maxval))

searchlistX.sort()
searchlistY.sort()

for i in searchlistY:
    if (linearBool:=searchlistX.count(i)) != (hashBool:=count(searchlistX,i)):
        print(hashBool);exit()

start = time.time()
for i in searchlistY:
	searchlistX.count(i)
end = time.time()
print("Linear time: ", (lintime:=end-start))

start = time.time()
for i in searchlistY:
	count(searchlistX,i)
end = time.time()
print("binary search ", (bintime:=end-start))
print("Linear search is", round(lintime/bintime), "times slower than binary search")

#The larger the range is, the slower linear search is compared to binary search
#When there's a larger proportion of numbers that don't exist in X, linear search is even more slow compared to binary search
#The larger the size of Y and X, the slower linear search is compared to binary search