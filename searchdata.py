from types import NoneType
from matmult import euclidean_dist, mult_scalar
from math import log
import json

ALPHA = 0.1
DISTANCE_THRESHOLD = 0.0001

def grabNewDict():
    with open('output.json') as output:
        return json.load(output)


newDict = {0:{ "outgoinglinks": [1], "incominglinks": [0,1], "countAll": {"word": 0}, "wordCount": 0, "wordVectors":{"word": 0}}, 
               1:{ "outgoinglinks": [0,2], "incominglinks": [0,1], "countAll": {"word": 0}, "wordCount": 0, "wordVectors":{"word": 0}},
              2:{ "outgoinglinks": [1], "incominglinks": [0,1], "countAll": {"word": 0}, "wordCount": 0, "wordVectors":{"word": 0}},}

def get_outgoing_links(URL):
    newDict = grabNewDict()
    if newDict !=NoneType and URL!=NoneType and URL in newDict:
        return newDict[URL]["outgoinglinks"]
    return None
    

def get_incoming_links(URL):
    newDict = grabNewDict()
    if URL in newDict:
        return newDict[URL]["incominglinks"]
    return None

def get_page_rank(URL):
    newDict = grabNewDict()

    print("Mapping from matrix index to URL:")
    mapping = []
    for url in newDict:
        mapping.append(url)
        print(str(mapping.index(url)) + " -> " + url)
    
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
    
    print("Adjacency matrix \n",matrix)
    
    matrix = mult_scalar(matrix, 1-ALPHA) #Multiply matrix by 1-alpha

    print("Scaled Adjacency matrix \n",matrix)

    # Add alpha/N to each of the elements in the matrix
    for i in range(length):
        for j in range(length):
            matrix[i][j]+= (ALPHA/length)
    
    print("Adjacency Matrix after adding alpha/N to each entry \n\n",matrix)

    pi = [1]
    for i in range(length-1):
        pi.append(0)
    euclid_dist = 1
    
    #Finding Stable State
    print ("")
    count = 0
    while(euclid_dist>=DISTANCE_THRESHOLD):
        count+=1
        new_pi = []
        for i in range (length):
            new_pi.append(dotProduct(pi, [x[i] for x in matrix]))
        euclid_dist = euclidean_dist([pi],[new_pi])
        pi = new_pi
        # print(pi,euclid_dist, count)
        print(count)
    return pi

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

get_page_rank('1')