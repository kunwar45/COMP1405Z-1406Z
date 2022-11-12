print("Welcome to the Trivia Game!")

fhand = open("triviaquestions.txt")
userGuess = ''
for line in fhand:
    print(line)
    if line[0] != ' ':
        userGuess = str(input(line))
    elif userGuess.lower() == line[1:]:
        print("You are correct")
    else:
        print("Incorrect Answer, the right answer is", line[1:])