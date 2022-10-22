from math import log
import json
import os

def readFile(path):
    file = open(path,"r")
    content = file.readlines()
    file.close()
    return content

def get_outgoing_links(URL):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(os.path.join("pages",new_url)):
        return readFile(os.path.join("pages",new_url,"outgoinglinks.txt"))[0].split()
    return None
    

def get_incoming_links(URL):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(os.path.join("pages",new_url)):
        return readFile(os.path.join("pages",new_url,"incominglinks.txt"))[0].split()
    return None

def get_page_rank(URL):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(os.path.join("pages",new_url)):
        return float(readFile(os.path.join("pages",new_url,"pageRank.txt"))[0])
    return -1

# def get_idf(word):
#     newDict = grabNewDict()
#     counter = 0
#     for url in newDict:
#         if word in newDict[url]["countAll"]:
#             counter +=1
    
#     if counter == 0: return 0
#     idf = log( len(newDict)/(1 + counter), 2)

#     return idf

# def get_tf(URL, word):
#     newDict = grabNewDict()
#     if URL not in newDict:
#         return 0
#     if word in newDict[URL]["countAll"]:
#         return newDict[URL]["countAll"][word]/(newDict[URL])["wordCount"]
#     return 0

# def get_tf_idf(URL, word):
#     tfidf = log(1+ get_tf(URL,word), 2)* get_idf(word)
#     return tfidf

# print(get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html'))