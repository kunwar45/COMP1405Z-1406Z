#Puts the new added value to the end of the stack given
def push(stack, value):
    stack.append(value)

#Returns the value that was most recently added and deletes it from the stack
def pop(stack):
    if(not isempty(stack)):
        return stack.pop(len(stack)-1)
    return None

#Returns true if the stack is emtpy, otherwise returns False
def isempty(stack):
    if len(stack) == 0:
        return True
    return False

#Returns the value that was most recently added
def peek(stack):
    if (not isempty(stack)):
        return stack[len(stack)-1]
    return None
