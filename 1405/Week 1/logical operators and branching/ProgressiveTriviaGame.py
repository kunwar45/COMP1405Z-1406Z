print("Welcome to the Trivia Game!")
userGuess = str(input("Your question is: What is the capital of Canada? "))
print("You are correct!") if userGuess.lower() == "ottawa" else print("Incorrect, the right answer is Ottawa")