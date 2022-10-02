from operator import truediv
from xml.dom.minidom import Element


maxSize = 10

def enqueue(queue, value):
    if (len(queue) < maxSize):
        queue.append(value)
        return True
    else:
        return False

def dequeue(queue):
    if (len(queue) > 0):
        ele = queue[0]
        del queue[0]
        return ele
    else:
        return None

def peek(queue):
    if (len(queue) > 0):
        return queue[0]
    else:
        return None

def isEmpty(queue):
    if (len(queue) > 0):
        return False
    else:
        return True

def multienqueue(queue, items):
    numAdded = 0

    while (len(queue) < maxSize):
        queue.append(items[numAdded])
        numAdded += 1
    
    return numAdded

def multidequeue(queue, number):

    for i in range(number):
        del queue[i]
    
    return queue
