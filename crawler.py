import webdev
import improvedqueue
import json
newDict = {}

'''
Pseudocode:

crawl(seed)
    create improvedqueue of urls (empty)
    loop:
        Take url and parse it
        for each url in dict[url][outgoinglinks]:
            Add it to improvedqueue if it isn't are already in the queue #should be o(1) because we're using improvedqueue

parse(url)
    Search through url
        if it is a word
            increment dict[url][countAll][<word>] if it isn't there already
            increment dict[url][wordCount]
            find tf of the word and add it to dict[url][wordVectors][<word>][0]
        if it is a link
            add it to dict[url][outgoinglinks]
            add url to dict[link][incominglinks]
'''

def crawl(seed):
    global newDict
    queueDict,queueList = {seed:1},[seed]
    
    url = improvedqueue.removestart(queueList,queueDict)
    count = 1

    while True: #Keeps crawling until there are no more links to take
        parse(url)
        
        for outgoingLink in newDict[url]["outgoinglinks"]:
            if not improvedqueue.containshash(queueDict,outgoingLink) and "outgoinglinks" not in newDict[outgoingLink]:
                improvedqueue.addend(queueList,queueDict,outgoingLink)
        if len(queueList) == 0:
            break
        url = improvedqueue.removestart(queueList,queueDict)
        count+=1

    with open('output.json', 'w+') as file:
        json.dump(newDict, file)
    # print(newDict)
    return count

# Returns list of urls present in a given webpage --- could rename to getUrls(seed) for clarity
def parse(url):
    global newDict
    
    if url not in newDict:
        newDict[url] = {}
    if "incominglinks" not in newDict[url]:
        newDict[url]["incominglinks"] = []
    newDict[url]["outgoinglinks"] = []
    newDict[url]["countAll"] = {}
    newDict[url]["wordCount"] = 0
    newDict[url]["wordVectors"] = []

    parsed = webdev.read_url(url)
    if parsed == "":
        return -1
    for index in parsed.split():
        if "href" in index:

            lastSlash = len(url) - url[::-1].find('/')
            outgoingLink = url[:lastSlash] + createSubString(index, '/', '>').strip('"')
            newDict[url]["outgoinglinks"].append(outgoingLink) # add the outgoing link
            # add the current url to the outgoing link's incoming links
            
            if outgoingLink in newDict:
                if "incominglinks" in newDict[outgoingLink]:
                    newDict[outgoingLink]["incominglinks"].append(url)
            else:
                newDict[outgoingLink]= {}
                newDict[outgoingLink]["incominglinks"] = [] 
                newDict[outgoingLink]["incominglinks"].append(url)
            
        elif "<" not in index:
            newDict[url]["wordCount"]+=1

            if index in newDict[url]["countAll"]:
                newDict[url]["countAll"][index] += 1
            else:
                newDict[url]["countAll"][index] = 1

    return 0

# Returns non inclusive substring from in between two characters of a string
def createSubString(str, start, end):
    return str[(str.index(start)+1):str.index(end)]

print(crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html"))
# print(webdev.read_url("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/"))

# <a > " "