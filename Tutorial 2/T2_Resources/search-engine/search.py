searchWord = str(input("Enter a word to search for: "))
pageCounts = [] #List to hold the searchWordCounts for each of the pages
pageRatios = [] #List to hold the ratios of the searchWordCounts to the totalWordCounts for each of the pages
for page in range(0,6):
    searchWordCount, totalWordCount = 0,0
    fhand = open(f"N-{page}.txt") #Fstring, puts a variable in a string (in this case, the page number)
    for line in fhand:
        totalWordCount+=1
        if searchWord in line:
            searchWordCount+=1
    fhand.close() #Closes the page
    pageCounts.append(searchWordCount)
    pageRatios.append((searchWordCount/totalWordCount))
print("Max Page (Count):", f"N-{pageCounts.index(max(pageCounts))}.txt") #Finds the page number with the max amount of searchWords
print("Max Count:", max(pageCounts))
print("Max Page (Ratio):", f"N-{pageRatios.index(max(pageRatios))}.txt") #Finds the page number with the max ratio of searchWords
print("Max Ratio:", max(pageRatios))