def push(stack, value):
    stack.append(value)

def pop(stack):
    if (len(stack) > 0):
        ele = stack[-1]
        del stack[-1]
        return ele
    else:
        return None

def isEmpty(stack):
    if (len(stack) > 0):
        return False
    else: 
        return True

def peek(stack):
    if (len(stack) > 0):
        return stack[-1]
    else: 
        return None