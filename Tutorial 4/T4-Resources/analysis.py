wordlist,wordCount,wordCounts,commonpairs = [],0,{},{}

def load(filename):
    global wordlist
    global wordCount
    global wordCounts
    wordlist,wordCount,wordCounts = [],0,{}
    wordlist = open(filename).readlines()[0].split()
    wordCount = len(wordlist)
    for word in wordlist:
        if word in wordCounts:
            wordCounts[word]+=1
        else:
            wordCounts[word] = 1

def commonword(list):
    if len(list) == 0 : return None

    flag,maxCount = 0,0
    #if the new wordCount of the word given is more than maxCount, set that to maxCount. If none of the words in the list are in
    #the wordCounts dictionary, return None
    for word in list:
        if word in wordCounts:
            flag = 1
            maxCount = wordCounts[word] if wordCounts[word] > maxCount else maxCount        
    if flag == 0: return None

    return ([word for word in wordCounts if (wordCounts[word] == maxCount and word in list)][0]) #list comprehension to find the key that has the maxCount

def commonpair(string):
    global commonpairs
    commonpairs = {}
    if string not in wordCounts or (wordCounts[string]==1 and wordlist[len(wordlist)-1] == string):
        return None

    for word in range(len(wordlist)-2):
        if wordlist[word] == string:
            if wordlist[word+1] in commonpairs:
                commonpairs[wordlist[word+1]]+=1
            else:
                commonpairs[wordlist[word+1]]=1
    return max(commonpairs,key=commonpairs.get) #Max can use a key for iterables like dictionaries according to the documentation

def countall():
    return wordCount

def countunique():
    return len(wordCounts)