def search(keyword):
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

    maxCount = fileList[frequencyList.index(max(frequencyList))]
    maxRatio = fileList[ratioList.index(max(ratioList))]
   
    print(f"max page (count): {maxCount}")
    print(f"max page (ratio): {maxRatio}")

# def main():
#     search("pear")

# if __name__ == "__main__":
#     main()