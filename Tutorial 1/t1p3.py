'''
Pseudocode:
Generate a random number from 1 to 100 and store it in a variable (randomNum)
Take an integer input from the user that is from 1 to 100 and store it into a variable (userGuess)
If userGuess and randomNum are the same:
    Output to the user that they guessed the random number correctly
Else
    Output the absolute value of the difference between userGuess and randomNum to the user

'''
import random

randomNum = random.randint(1,100)
print(randomNum)
userGuess = int(input("Guess a number between 1 and 100 (inclusive): "))
if userGuess == randomNum:
    print("You guessed correctly!")
else:
    print("You were", abs(randomNum - userGuess), "off from the random number")