keyword = str(input("Enter a word to search for: "))

fileList = open("pages.txt", "r").readlines()

frequencyList = []
ratioList = []

wordCount = 0

for index in fileList:
    file = open(index.strip('\n'), "r")
    frequency = 0
    for line in file:
        wordCount += 1
        if (line.strip('\n') == keyword):
            frequency += 1

    frequencyList.append(frequency)
    ratioList.append(frequency/wordCount)
    wordCount = 0

maxCount = fileList[frequencyList.index(max(frequencyList))].strip('\n')
maxRatio = fileList[ratioList.index(max(ratioList))].strip('\n')

print("max page (count): ", maxCount)
print("Max Count:", max(frequencyList))
print("max page (ratio): ", maxRatio) 
print("Max Ratio:", max(ratioList))