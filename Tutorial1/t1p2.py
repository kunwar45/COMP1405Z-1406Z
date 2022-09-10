# user input 3 midterms (20%)
# user input 1 final (40%)

grade1 = int(input("whats the grade for the first midterm?: "))
weight1 = int(input("enter the weight for the first midterm (%): "))

grade2 = int(input("whats the grade for the second midterm?: "))
weight2 = int(input("enter the weight for the second midterm (%): "))

grade3 = int(input("whats the grade for the third midterm?: "))
weight3 = int(input("enter the weight for the third midterm (%): "))

grade4 = int(input("whats the grade for the final?: "))
weight4 = int(input("enter the weight for the final (%): "))

average = (grade1*(weight1/100))+(grade2*(weight2/100))+(grade3*(weight3/100))+(grade4*(weight4/100))

print(average)