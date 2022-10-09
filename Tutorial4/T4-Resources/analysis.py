lines = []
words = []
uniqueWords = []
wordFrequencies = {}
followingWordFrequencies = {}

def load(str):

    global words
    global uniqueWords

    file = open(str, "r")

    lines = file.readlines()
    
    words = []

    for line in lines:
        for word in line.split():
            words.append(word)

    uniqueWords = []
    for word in words:
        if (word not in uniqueWords):
            uniqueWords.append(word)

def commonword(list):
    global wordFrequencies
    if ((len(list) == 0) or (not(bool(set(list) & set(words))))):
        return None
    else:
        wordFrequencies = {word : words.count(word) for word in list}
    
    return max(wordFrequencies, key=wordFrequencies.get)
        

def commonpair(str):
    global followingWordFrequencies
    followingWordFrequencies = {}
    if ((str not in words)):
        return None
    for i in range(len(words)-1):
        if words[i] == str:
            if words[i+1] in followingWordFrequencies:
                    followingWordFrequencies[words[i+1]] += 1
            else:
                followingWordFrequencies[words[i+1]] = 1
    if (followingWordFrequencies):
        return max(followingWordFrequencies, key=followingWordFrequencies.get)
    else:
        return None

def countall():
    return len(words)

def countunique():
    return len(uniqueWords)
