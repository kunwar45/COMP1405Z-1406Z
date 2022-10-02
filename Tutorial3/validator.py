import mystack

def isvalid(str):
    strList = list(str)
    stack = []
    brackets = ['(', '{', '[', ')', '}', ']']
    bracketsForward = ['(', '{', '[']
    bracketsBackward = [ ')', '}', ']']

    strList = list(filter(lambda character: character in brackets, strList))

    for character in strList:
        if (character in bracketsForward):
            mystack.push(stack, character)
        elif (character in bracketsBackward):
            if (mystack.peek(stack) == bracketsForward[bracketsBackward.index(character)]):
                mystack.pop(stack)
            else:
                return False
        
    return mystack.isEmpty(stack)
