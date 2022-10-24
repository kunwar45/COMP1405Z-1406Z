# from math import log
# import json
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

def get_idf(word):
    if os.path.exists(path:=os.path.join("Idfs",f"{word}.txt")):
        return float(readFile(path)[0])
    return 0

def get_tf(URL,word):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(urlPath:=os.path.join("pages",new_url)):
        if os.path.exists(path:=os.path.join(urlPath,"countAll",f"{word}.txt")):
            return float(readFile(path)[0].split()[2])
    return 0

def get_tf_idf(URL, word):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(urlPath:=os.path.join("pages",new_url)):
        if os.path.exists(path:=os.path.join(urlPath,"countAll",f"{word}.txt")):
            return float(readFile(path)[0].split()[1])
    return 0

# print(get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html'))