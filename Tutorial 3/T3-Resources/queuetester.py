import myqueue

thequeue = []


print("Printing the initial queue, should be: []")
print("Your queue is:", thequeue)
print("Adding 10 values to queue")

for i in range(10):
    myqueue.enqueue(thequeue, i)

print("The queue should now be: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
print("Your queue is:", thequeue)

print("Trying to add 'cow' to queue")
result = myqueue.enqueue(thequeue, 'cow')
print("The return value of that call to enqueue should be False")
print("The returned value from your queue was", result)
print("Printing the queue, should be: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]")
print("Your queue is:", thequeue)

print("Removing and printing 4 values from queue")
print("Should be 0:", myqueue.dequeue(thequeue))
print("Should be 1:", myqueue.dequeue(thequeue))
print("Should be 2:", myqueue.dequeue(thequeue))
print("Should be 3:", myqueue.dequeue(thequeue))

print("Looking at the first value, but not removing")
print("Should be 4:", myqueue.peek(thequeue))

print("Trying to add 'cow' to queue")
myqueue.enqueue(thequeue, 'cow')
print("The queue should now be: [4, 5, 6, 7, 8, 9, 'cow']")
print("Your queue is:", thequeue)

print("Trying to enqueue the list ['a', 'b', 'c', 'd', 'e']")
added = myqueue.multienqueue(thequeue, ['a', 'b', 'c', 'd', 'e'])
print("The number added should be 3.")
print("The number added was", added)

print("The queue should now be: [4, 5, 6, 7, 8, 9, 'cow', 'a', 'b', 'c']")
print("Your queue is:", thequeue)

print("Trying to dequeue a list of 5 items")
removed = myqueue.multidequeue(thequeue, 5)
print("The dequeued list should be: [4, 5, 6, 7, 8]")
print("The dequeued list was: ", removed)

print("The queue should now be: [9, 'cow', 'a', 'b', 'c']")
print("Your queue is:", thequeue)

print("Trying to dequeue a list of 7 items")
removed = myqueue.multidequeue(thequeue, 7)
print("The dequeued list should be: [9, 'cow', 'a', 'b', 'c']")
print("The dequeued list was: ", removed)

print("The queue should now be: []")
print("Your queue is:", thequeue)

print("Dequeing from empty queue, should be None")
print("Your queue produced: ", myqueue.dequeue(thequeue))

print("Peeking at empty queue, should be None")
print("Your queue produced: ", myqueue.peek(thequeue))
