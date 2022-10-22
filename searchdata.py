from math import log
import json
import os

def grabNewDict():
    with open('output.json') as output:
        return json.load(output)

def readFile(path):
    file = open(path,"r")
    content = file.readlines()
    file.close()
    return content

#Make getting to the correct URL folder O(1)
reversedMap = readFile("mapping.txt")[0].split()
mapping = {}
for urlNum in range(len(reversedMap)):
    mapping[reversedMap[urlNum]] = urlNum

def get_outgoing_links(URL):
    # newDict = grabNewDict()
    if URL in reversedMap:
        return readFile(os.path.join("pages",str(mapping[URL]),"outgoinglinks.txt"))[0].split()
    return None
    

def get_incoming_links(URL):
    # newDict = grabNewDict()
    if URL in reversedMap:
        return readFile(os.path.join("pages",str(mapping[URL]),"incominglinks.txt"))[0].split()
    return None

def get_page_rank(URL):
    # newDict = grabNewDict()
    if URL in reversedMap:
        return float(readFile(os.path.join("pages",str(mapping[URL]),"pageRank.txt"))[0])
    return -1

def get_idf(word):
    newDict = grabNewDict()
    counter = 0
    for url in newDict:
        if word in newDict[url]["countAll"]:
            counter +=1
    
    if counter == 0: return 0
    idf = log( len(newDict)/(1 + counter), 2)

    return idf

def get_tf(URL, word):
    newDict = grabNewDict()
    if URL not in newDict:
        return 0
    if word in newDict[URL]["countAll"]:
        return newDict[URL]["countAll"][word]/(newDict[URL])["wordCount"]
    return 0

def get_tf_idf(URL, word):
    tfidf = log(1+ get_tf(URL,word), 2)* get_idf(word)
    return tfidf

def dotProduct(pi,b):
    print(pi,b)
    sum = 0
    for i in range(len(pi)):
        sum+=pi[i]*b[i]
    return sum

# print(get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html'))