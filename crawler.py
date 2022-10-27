from math import log
import webdev
import improvedqueue
import os
from matmult import euclidean_dist, mult_scalar

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
    data = {} #holds all the parsed values
    IDFs = {}
    queueDict,queueList = {seed:1},[seed] #Improved queue variables used to make checking the queue O(1)

    url = improvedqueue.removestart(queueList,queueDict)
    count = 1

    while True: #Keeps crawling until there are no more links to take
        data = parse(url,data)
        
        for outgoingLink in data[url]["outgoinglinks"]:
            if not improvedqueue.containshash(queueDict,outgoingLink) and "outgoinglinks" not in data[outgoingLink]:
                improvedqueue.addend(queueList,queueDict,outgoingLink)

        #Adds to the frequency of urls that have a word
        for word in data[url]["countAll"]:
            if word in IDFs:
                IDFs[word] += 1
            else:
                IDFs[word] = 1

        if len(queueList) == 0:
            break
        url = improvedqueue.removestart(queueList,queueDict)
        count+=1

    #Gets the mapping of the urls to the numbers as well as the pageranks, O(n^3)
    pageRanks,mapping = createPageRanks(data)

    #Adds the pageranks to the dictionary
    for rank in range(len(pageRanks)):
        data[mapping[rank]]["pageRank"] = pageRanks[rank]
    
    #Creates all the files for searchdata.py to use
    createFiles(data,IDFs)
    return count

# Returns the updated dictionary that has all the parsed information of the url
def parse(url, data):
    #Creating the dictionary keys
    if url not in data:
        data[url] = {}
    if "incominglinks" not in data[url]:
        data[url]["incominglinks"] = []
    data[url]["title"] = ""
    data[url]["outgoinglinks"] = []
    data[url]["countAll"] = {}
    data[url]["wordCount"] = 0
    data[url]["pageRank"] = 0

    parsed = webdev.read_url(url)
    if parsed == "":
        return -1
    for index in parsed.split():
        if "title" in index:
            data[url]["title"] = createSubString(index, "<title>", "</title>")
        elif "href" in index:
            if ("http" in index):
                outgoingLink = createSubString(index, 'href="', '"')
            else:
                lastSlash = len(url) - url[::-1].find('/') # last slash of initial url to append relative link to
                outgoingLink = url[:lastSlash] + createSubString(index, 'href="./', '"')
                data[url]["outgoinglinks"].append(outgoingLink) # add the outgoing link
                
            #Put the current url in the outgoing link's incoming links
            if outgoingLink in data:
                if "incominglinks" in data[outgoingLink]:
                    data[outgoingLink]["incominglinks"].append(url)
            else:
                data[outgoingLink]= {}
                data[outgoingLink]["incominglinks"] = [] 
                data[outgoingLink]["incominglinks"].append(url)
        elif (">" in index) and ("<" not in index):
            data[url]["wordCount"]+=1

            index = index[index.index('>')+1:]

            if index in data[url]["countAll"]:
                data[url]["countAll"][index] += 1
            else:
                data[url]["countAll"][index] = 1 
        elif ("<" in index) and (not index.startswith("<")):
            data[url]["wordCount"]+=1

            index = index[:index.index('<')]
            
            if index in data[url]["countAll"]:
                data[url]["countAll"][index] += 1
            else:
                data[url]["countAll"][index] = 1 
        #If it's just text from the paragraph
        elif ("<" not in index) and (">" not in index):
            data[url]["wordCount"]+=1

            if index in data[url]["countAll"]:
                data[url]["countAll"][index] += 1
            else:
                data[url]["countAll"][index] = 1   
    return data


# Returns non inclusive substring from in between two characters of a string
def createSubString(str, start, end):
    if ((start not in str) or (end not in str[str.index(start)+len(start):])):
        return 0
    return str[(str.index(start)+len(start)):str.index(end, (str.index(start)+len(start)))]

#Returns the inverse term frequency of a word from a URL, O(1) as it uses the IDFs dictionary
def get_idf(word, totalUrls, IDFs):
    if word in IDFs:
        counter = IDFs[word]
    else:
        return 0
    return log( totalUrls/(1 + counter), 2)

#Returns the term frequency of a word from a URL, O(1) as the 'in' keyword is constant when dealing with dictionaries
def get_tf(URL, word, data):
    if URL not in data:
        return 0
    if word in data[URL]["countAll"]:
        return data[URL]["countAll"][word]/(data[URL])["wordCount"]
    return 0

#Returns the tf-idf of a word from a URL, O(1) as both get_tf and get_df are O(1)
def get_tf_idf(URL, word, data, IDFs):
    tfidf = log(1+ get_tf(URL, word, data), 2)* get_idf(word, len(data), IDFs)
    return tfidf

#Returns the dotProduct between two vectors, O(n)
def dotProduct(pi,b):
    sum = 0
    for i in range(len(pi)):
        sum+=pi[i]*b[i]
    return sum

#Creates files for all the values in the dictionary so that searchData can be O(1), Requires the data dictionary and the IDFs dictionary
#O(n*m) time complexity where m is the number of words in data[url]["countAll"] and it is being looped over (hence the n)
def createFiles(data, IDFs):

    #Delete previous pages
    if os.path.exists("pages"):
        deleteFolder("pages")
    if os.path.exists("Idfs"):
        deleteFolder("Idfs")
    os.makedirs("pages")
    os.makedirs("Idfs")
    
    for url in data:
        #Create a directory for the URL
        new_url = url.replace('/','{').replace(':','}').replace('.','(')
        url_path = os.path.join("pages",new_url)
        os.makedirs(url_path)
        
        #Create file for incominglinks
        file = open(os.path.join(url_path,"incominglinks.txt"),"w")
        file.write(" ".join(data[url]["incominglinks"]))
        file.close()
        
        #Create file for outgoinglinks
        file = open(os.path.join(url_path,"outgoinglinks.txt"),"w")
        file.write(" ".join(data[url]["outgoinglinks"]))
        file.close()

        #Create file for the frequency of each word in the url
        os.makedirs( wordsPath:= os.path.join(url_path,"countAll") )
        for word in data[url]["countAll"]:
            file = open(os.path.join(wordsPath,word + ".txt"),"w")
            file.write(str(data[url]["countAll"][word]))
            file.close()
        
        #Create file for the total word count of the page
        file = open(os.path.join(url_path,"wordCount.txt"),"w")
        file.write(str(data[url]["wordCount"]))
        file.close()

        #Adding IDFs and tf-idfs
        for word in data[url]["countAll"]:
            idfspath = os.path.join("Idfs",f"{word}.txt")
            if not os.path.exists(idfspath):
                file = open(idfspath,"w")
                file.write(str(get_idf(word,len(data),IDFs)))
                file.close()
            file = open(os.path.join(url_path,"countAll",f"{word}.txt"),"a")
            file.write(" " + str(get_tf_idf(url, word, data, IDFs)) + " " + str(get_tf(url, word, data)))
            file.close()
        
        #Creating a file for the pageRanks
        file = open(os.path.join(url_path,"pageRank.txt"),"w")
        file.write(str(data[url]["pageRank"]))
        file.close()

        #Creating a file for the title of each page
        file = open(os.path.join(url_path,"title.txt"),"w")
        file.write(str(data[url]["title"]))
        file.close()

#Recursive function that goes through everything inside a folder and deletes it all, O(n) with n being the number of files to delete
#Requires the folder name
def deleteFolder(folder):
    files = os.listdir(folder)
    for file in files:
        file_path = os.path.join(folder,file)
        if file.endswith(".txt"):
            os.remove(file_path)
        else:
            deleteFolder(file_path)
    os.rmdir(folder)

#Creates all the pageRanks, O(n^2*m) as looping dot product is O(n^2), n being the number of links, and the while loop on top of it is
#makes it O(n^2*m), m being the number of convergence iterations. It returns the pageRank vector and needs the data dictionary as a parameter
def createPageRanks(data):
    ALPHA = 0.1
    DISTANCE_THRESHOLD = 0.0001
    mapping = []

    for url in data:
        mapping.append(url)
      
    #Creating Probability Matrix
    matrix = []
    length = len(mapping)
    for i in range(length):
        matrix.append([])
        for j in range(length):
            if len(ogIndexes:=data[mapping[i]]["outgoinglinks"]) == 0:
                matrix[i].append( ((1/length) * (1-ALPHA)) + (ALPHA/length))
            else:
                matrix[i].append( ((1/len(ogIndexes)) * (1-ALPHA)) + (ALPHA/length) if mapping[j] in ogIndexes else (ALPHA/length))

    pi = []
    for i in range(length):
        pi.append(1/length)
    euclid_dist = 1
    
    #Finding Stable State, O(n^2 * m) where n is the number of urls and m is the number of convergence iterations
    count = 0
    while(euclid_dist>=DISTANCE_THRESHOLD):
        count+=1
        new_pi = []
        for i in range (length):
            new_pi.append(dotProduct(pi, [x[i] for x in matrix]))
        euclid_dist = euclidean_dist([pi],[new_pi])
        pi = new_pi

    return pi,mapping

#This is used to test a theory I had. I reference this in the course project analysis. It simply returns the pageRank
def createWorsePageRanks(data):
    ALPHA = 0.1
    DISTANCE_THRESHOLD = 0.0001
    mapping = []

    for url in data:
        mapping.append(url)
    
    #Creating Adjacency matrix
    matrix = []
    length = len(mapping)
    for i in range(length):
        matrix.append([])
        for j in range(length):
            if len(ogIndexes:=data[mapping[i]]["outgoinglinks"]) == 0:
                matrix[i].append(1/length)
            else:
                matrix[i].append(1/len(ogIndexes) if mapping[j] in ogIndexes else 0)
    
    matrix = mult_scalar(matrix, 1-ALPHA) #Multiply matrix by 1-alpha

    # Add alpha/N to each of the elements in the matrix
    for i in range(length):
        for j in range(length):
            matrix[i][j]+= (ALPHA/length)

    pi = []
    for i in range(length):
        pi.append(1/length)
    euclid_dist = 1
    
    #Finding Stable State, O(n^2 * m) where n is the number of urls and m is the number of convergence iterations
    count = 0
    while(euclid_dist>=DISTANCE_THRESHOLD):
        count+=1
        new_pi = []
        for i in range (length):
            new_pi.append(dotProduct(pi, [x[i] for x in matrix]))
        euclid_dist = euclidean_dist([pi],[new_pi])
        pi = new_pi

    return pi,mapping

    