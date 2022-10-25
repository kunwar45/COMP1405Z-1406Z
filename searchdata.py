import os

#Reads a file, O(n) if the file does not have a bound
def readFile(path):
    file = open(path,"r")
    content = file.readlines()
    file.close()
    return content

#Returns outgoing links, O(n) as the file gets larger as there are more links
def get_outgoing_links(URL): 
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(os.path.join("pages",new_url)):
        return readFile(os.path.join("pages",new_url,"outgoinglinks.txt"))[0].split()
    return None

#Returns incoming links, O(n) as the file gets larger as there are more links
def get_incoming_links(URL):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(os.path.join("pages",new_url)):
        return readFile(os.path.join("pages",new_url,"incominglinks.txt"))[0].split()
    return None

#Returns the pageRank of a page, O(1) since the file doesn't get larger as there are more urls
def get_page_rank(URL):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(os.path.join("pages",new_url)):
        return float(readFile(os.path.join("pages",new_url,"pageRank.txt"))[0])
    return -1

#Returns the title of a page, O(1) since the file doesn't get larger as there are more urls
def get_title(URL):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(os.path.join("pages",new_url)):
        return str(readFile(os.path.join("pages",new_url,"title.txt"))[0])
    return None

#Returns the idf of a page, O(1) since the file doesn't get larger as there are more urls
def get_idf(word):
    if os.path.exists(path:=os.path.join("Idfs",f"{word}.txt")):
        return float(readFile(path)[0])
    return 0

#Returns the tf of a page, O(1) since the file doesn't get larger as there are more urls
def get_tf(URL,word):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(urlPath:=os.path.join("pages",new_url)):
        if os.path.exists(path:=os.path.join(urlPath,"countAll",f"{word}.txt")):
            return float(readFile(path)[0].split()[2])
    return 0

#Returns the tf-idf of a page, O(1) since the file doesn't get larger as there are more urls
def get_tf_idf(URL, word):
    new_url = URL.replace('/','{')[:-5].replace(':','}')
    if os.path.exists(urlPath:=os.path.join("pages",new_url)):
        if os.path.exists(path:=os.path.join(urlPath,"countAll",f"{word}.txt")):
            return float(readFile(path)[0].split()[1])
    return 0