from cgi import test
import webdev
import improvedqueue
import json
import os
from matmult import euclidean_dist, mult_scalar

ALPHA = 0.1
DISTANCE_THRESHOLD = 0.0001


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
    newDict = {}
    queueDict,queueList = {seed:1},[seed]
    
    url = improvedqueue.removestart(queueList,queueDict)
    # os.makedirs("0")
    count = 1

    while True: #Keeps crawling until there are no more links to take
        newDict = parse(url,newDict)
        
        for outgoingLink in newDict[url]["outgoinglinks"]:
            if not improvedqueue.containshash(queueDict,outgoingLink) and "outgoinglinks" not in newDict[outgoingLink]:
                improvedqueue.addend(queueList,queueDict,outgoingLink)
                
        if len(queueList) == 0:
            break
        url = improvedqueue.removestart(queueList,queueDict)
        count+=1

    pageRanks,mapping = createPageRanks(newDict)
    for rank in range(len(pageRanks)):
        newDict[mapping[rank]]["pageRank"] = pageRanks[rank]
    
    createFiles(newDict,mapping)
    # print(mapping)
    with open('output.json', 'w+') as file:
        json.dump(newDict, file)
    # print(newDict)
    return count

# Returns list of urls present in a given webpage --- could rename to getUrls(seed) for clarity
def parse(url, newDict):
    if url not in newDict:
        newDict[url] = {}
    if "incominglinks" not in newDict[url]:
        newDict[url]["incominglinks"] = []
    newDict[url]["outgoinglinks"] = []
    newDict[url]["countAll"] = {}
    newDict[url]["wordCount"] = 0
    newDict[url]["wordVectors"] = []
    newDict[url]["pageRank"] = 0

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
    return newDict

# Returns non inclusive substring from in between two characters of a string
def createSubString(str, start, end):
    return str[(str.index(start)+1):str.index(end)]

def createPageRanks(newDict):
    mapping = []
    # print("Mapping from matrix index to URL:")

    for url in newDict:
        mapping.append(url)
        # print(str(mapping.index(url)) + " -> " + url)
    
    matrix = []

    length = len(mapping)
    for i in range(length):
        matrix.append([])
        for j in range(length):
            # print(len(newDict[mapping[i]]["outgoinglinks"]))
            if len(ogIndexes:=newDict[mapping[i]]["outgoinglinks"]) == 0:
                matrix[i].append(1/length)
            else:
                matrix[i].append(1/len(ogIndexes) if mapping[j] in ogIndexes else 0)
    
    # print("Adjacency matrix \n",matrix)
    
    matrix = mult_scalar(matrix, 1-ALPHA) #Multiply matrix by 1-alpha

    # print("Scaled Adjacency matrix \n",matrix)

    # Add alpha/N to each of the elements in the matrix
    for i in range(length):
        for j in range(length):
            matrix[i][j]+= (ALPHA/length)
    
    # print("Adjacency Matrix after adding alpha/N to each entry \n\n",matrix)

    pi = []
    for i in range(length):
        pi.append(1/length)
    euclid_dist = 1
    
    #Finding Stable State
    # print ("Creating Pi")
    count = 0
    while(euclid_dist>=DISTANCE_THRESHOLD):
        count+=1
        new_pi = []
        for i in range (length):
            new_pi.append(dotProduct(pi, [x[i] for x in matrix]))
        euclid_dist = euclidean_dist([pi],[new_pi])
        pi = new_pi
    return pi,mapping

def dotProduct(pi,b):
    sum = 0
    for i in range(len(pi)):
        sum+=pi[i]*b[i]
    return sum

def createFiles(newDict,mapping):

    #Delete previous pages
    if os.path.exists("pages"):
        deleteFolder("pages")
    os.makedirs("pages")

    #Create file for the mapping of all the URLs
    file = open("mapping.txt","w")
    file.write(" ".join(mapping))
    file.close()
    
    for urlNum in range(len(mapping)):
        #Create a directory for the URL
        url_path = os.path.join("pages",str(urlNum))
        os.makedirs(url_path)
        
        #Create file for incominglinks
        file = open(os.path.join(url_path,"incominglinks.txt"),"w")
        file.write(" ".join(newDict[mapping[urlNum]]["incominglinks"]))
        file.close()
        
        #Create file for outgoinglinks
        file = open(os.path.join(url_path,"outgoinglinks.txt"),"w")
        file.write(" ".join(newDict[mapping[urlNum]]["outgoinglinks"]))
        file.close()

        #Create file for the frequency of each word in the url
        os.makedirs( wordsPath:= os.path.join(url_path,"countAll") )
        for word in newDict[mapping[urlNum]]["countAll"]:
            file = open(os.path.join(wordsPath,word + ".txt"),"w")
            file.write(str(newDict[mapping[urlNum]]["countAll"][word]))
            file.close()
        
        #Create file for the total word count of the page
        file = open(os.path.join(url_path,"wordCount.txt"),"w")
        file.write(str(newDict[mapping[urlNum]]["wordCount"]))
        file.close()

        #For wordVectors
        # os.makedirs( vectorsPath:= os.path.join(url_path,"wordVectors") )
        # for word in newDict[mapping[urlNum]]["wordVectors"]:
        #     file = open(os.path.join(vectorsPath,word + ".txt"),"w")
        #     file.write(str(newDict[mapping[urlNum]]["wordVectors"][word]))
        #     file.close()

        #Create file for the page rank
        file = open(os.path.join(url_path,"pageRank.txt"),"w")
        file.write(str(newDict[mapping[urlNum]]["pageRank"]))
        file.close()

#Recursive function that goes through everything inside a folder and deletes it all
def deleteFolder(folder):
    files = os.listdir(folder)
    for file in files:
        file_path = os.path.join(folder,file)
        if file.endswith(".txt"):
            os.remove(file_path)
        else:
            deleteFolder(file_path)
    os.rmdir(folder)

file = open("mapping.txt","r")
print()
print(crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html"))
# print(webdev.read_url("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/"))

