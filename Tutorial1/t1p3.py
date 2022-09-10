import random

# generate random number 1 -100

randomNumber = random.randint(1, 100)

# user guesses the number
userNumber = int(input("Enter your guess: "))

# calculate distance
distance = abs(randomNumber-userNumber)

# tell user distance from actual

print("The actual number was: ", randomNumber)
print("The distance from the actual number and your guess was: ", distance)