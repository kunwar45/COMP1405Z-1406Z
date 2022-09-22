maxQueue = 10

#Adds one item parameter to the queue (list) given if it's less than the maxQueue
def enqueue(queue, value):
    if(len(queue)<maxQueue):
        queue.append(value)
        return True
    return False

#Deletes one item from the queue (list) given and returns it if the queue is not empty
def dequeue(queue):
    if (not isempty(queue)):
        return queue.pop(0)
    return None

#Check the first item in the queue (list) given if it's not empty
def peek(queue):
    if (not isempty(queue)):
        return queue[0]
    return None

def isempty(queue):
    if(len(queue)>0):
        return False
    return True

#Queue multiple items in the queue until t
def multienqueue(queue, items):
    count = 0
    for item in items:
        if enqueue(queue,item):
            count+=1
    return count

def multidequeue(queue,number):
    dequeued = []
    for num in range(0,number):
        if(not isempty(queue)):
            dequeued.append(dequeue(queue))
        else:
            break
    return dequeued
