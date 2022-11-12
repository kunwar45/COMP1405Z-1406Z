'''
Pseudocode: 
Take the first score afrom the user and store it in a variable (scoreOne)
Take the first weight afrom the user and store it in a variable (weightOne)
Take the second score afrom the user and store it in a variable (scoreTwo)
Take the second weight afrom the user and store it in a variable (weightTwo)
Take the third score afrom the user and store it in a variable (scoreThree)
Take the third weight afrom the user and store it in a variable (weightThree)
Take the fourth score afrom the user and store it in a variable (scoreFour)
Take the fourth weight afrom the user and store it in a variable (weightFour)

Multiply the scores and their respective weights, then take the sum of those products and divide that sum by the sum of all the weights
then store it in a variable (weightedAverage)

Output the weightedAverage
'''

scoreOne = float(input("What is your first score: "))
weightOne = float(input("What is the weight of your first item: "))
scoreTwo = float(input("What is your second score: "))
weightTwo = float(input("What is the weight of your second item: "))
scoreThree = float(input("What is your third score: "))
weightThree = float(input("What is the weight of your third item: "))
scoreFour = float(input("What is your four score: "))
weightFour = float(input("What is the weight of your four item: "))

weightedAverage = ( (scoreOne * weightOne) + (scoreTwo * weightTwo) + (scoreThree * weightThree) + (scoreFour * weightFour) )/ (weightOne + weightTwo + weightThree+ weightFour)
print("Your weighted average is",weightedAverage)