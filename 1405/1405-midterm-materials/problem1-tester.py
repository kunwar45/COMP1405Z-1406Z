
import copy
import importlib

modname = "problem1"
funcname = "largest_prime_factor"
information = [[[390], 13], [[350], 7], [[263], 263], [[9], 3], [[419], 419], [[104], 13], [[319], 29], [[116], 29], [[457], 457], [[470], 47], [[287], 41], [[372], 31], [[34], 17], [[435], 29], [[415], 83], [[358], 179], [[364], 13], [[86], 43], [[83], 83], [[355], 71], [[246], 41], [[245], 7], [[426], 71], [[180], 5], [[212], 53], [[100], 5], [[287], 41], [[32], 2], [[196], 7], [[150], 5], [[28], 7], [[356], 89], [[306], 17], [[54], 3], [[94], 47], [[176], 11], [[249], 83], [[263], 263], [[451], 41], [[61], 61], [[45], 5], [[89], 89], [[427], 61], [[239], 239], [[207], 23], [[489], 163], [[324], 3], [[275], 11], [[343], 7], [[432], 3], [[165], 11], [[133], 19], [[77], 11], [[4], 2], [[248], 31], [[269], 269], [[282], 47], [[75], 5], [[397], 397], [[479], 479], [[391], 23], [[273], 13], [[74], 37], [[176], 11], [[150], 5], [[439], 439], [[159], 53], [[419], 419], [[209], 19], [[246], 41], [[43], 43], [[29], 29], [[262], 131], [[28], 7], [[494], 19], [[298], 149], [[350], 7], [[84], 7], [[196], 7], [[98], 7], [[53], 53], [[482], 241], [[354], 59], [[71], 71], [[350], 7], [[494], 19], [[439], 439], [[50], 5], [[385], 11], [[308], 11], [[367], 367], [[470], 47], [[64], 2], [[102], 17], [[452], 113], [[424], 53], [[165], 11], [[493], 29], [[121], 11], [[361], 19]]
resulttype = "int"

try:
    module = importlib.import_module(modname)
    func = getattr(module,funcname)
except Exception as e:
    print("Error loading module and/or function - check the names?")
    print("Error description: " + str(e))
    quit()

correct = 0
incorrect = []
print("Checking function with test inputs...")
print()
for info in information:
    inputs = copy.deepcopy(info[0])
    goal = info[1]
    print("Inputs:", str(inputs)[1:-1])
    print("Goal:",goal)
    result = func(*inputs)
    print("Your Result:", result)
    success = False
    if resulttype == "int" and isinstance(result, int):
        success = goal == result
    elif resulttype == "float" and isinstance(result, (int,float)):
        success = abs(goal - result) < 0.001
    elif resulttype == "string" and isinstance(result, str):
        success = goal.lower() == result.lower()
    elif resulttype == "orderedlist" and isinstance(result, list):
        success = False
        if len(goal) == len(result):
            success = True
            for i in range(len(goal)):
                if goal[i] != result[i]:
                    success = False

    if success:
        correct += 1
        print("Good!")
    else:
        incorrect.append([inputs,goal,result])
        print("Incorrect!")
    print()

print()
print("Your code produced",correct,"out of", len(information),"correct results.")
print()

if len(incorrect) > 0:
    input("Hit enter to see the incorrect cases...")
    print("The inputs for which your program failed were:")
    print()
    for info in incorrect:
        print("Inputs:", str(info[0])[1:-1])
        print("Goal:", info[1])
        print("Your Result:", info[2])
        print()
