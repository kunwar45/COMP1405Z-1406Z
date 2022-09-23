import mystack

#Algorithm
'''
Define function isvalid that takes in string
Create an empty list stack
Create an empty list bracket

Fill brackets with the characters in string that are brackets

set stackIndex to 0
while the both brackets and stack aren't empty
    if stack is empty
        Pop the last element from brackets into stack
        restart the loop
    
    if brackets is not empty:
        Pop the last element from brackets into stack
    if the stackIndex is equal to the length of stack:
        break the loop, since this means that stack wasn't able to become empty because the string is invalid

    if the last 2 elements of stack are matching brackets:
        Pop both of those elements out
        Reduce stackIndex by 2 as those elements are now gone
    Increment stackIndex
return True if stack is empty, otherwise return False

Demonstration:
string = "({})"

Step 0:
brackets = ['(', '{', '}', ')']
stack = []
stackIndex = 0
forced continue

Step 1 (of loop):
brackets = ['(', '{', '}']
stack = [')']

stackIndex += 1 (now 1)
Forced continue

Step 2 (of loop):
brackets = ['(', '{']
stack = [')', '}']
stackIndex = 1

Last two elements of stack aren't matching
stackIndex +=1 (now 2)

Step 3 (of loop):
brackets = ['(']
stack = [')', '}','{']
stackIndex = 2

Last two elements of stack are matching
pop '}' and '{'
stackIndex -=2 (now 0)
stackIndex +=1 (now 1)

Step 4 (of loop):
brackets = []
stack = [')', '(']
stackIndex = 1

Last two elements of stack are matching
pop ')' and '('
stackIndex -=2 (now -1)
stackIndex +=1 (now 0)

Step 5 (of loop) :
brackets = []
stack = []
loop ends as brackets and stack are both empty

Step 6:
Stack is empty, therefore string is valid

'''


def isvalid(string):
    stack = []
    brackets = []
    for i in string:
        if i == '(' or i == ')' or i == '[' or i == ']' or i == '{' or i == '}':
            mystack.push(brackets,i)
    
    stackIndex = 0
    while len(brackets)!=0 or len(stack) !=0:
        if len(stack) == 0: #For when the stack gets empty, need to get at least 1 bracket before comparing
            mystack.push(stack,mystack.pop(brackets))
            stackIndex+=1
            continue
        
        if len(brackets) != 0: #If brackets is empty, there's nothing to pop
            mystack.push(stack,mystack.pop(brackets))
        if stackIndex == len(stack): #If the brackets don't match, the loop will go until stackindex is larger than the stack length
            break
        
        if(
        (stack[stackIndex] == '(' and stack[stackIndex-1] == ')') or 
        (stack[stackIndex] == '[' and stack[stackIndex-1] == ']') or
        (stack[stackIndex] == '{' and stack[stackIndex-1] == '}') ):
            
            #Deletes the pair of brackets
            mystack.pop(stack)
            mystack.pop(stack)
            stackIndex-=2 #-2 since the two brackets have been taken out
        
        stackIndex+=1
    return mystack.isempty(stack)   