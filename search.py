from pydoc import doc
import crawler
import searchdata
import matmult as mat
import os
from math import log

def search(phrase:str, boost):
    #Step 1: Find vectors:
        #a) Find tf-idf of every unique word in the phrase
        #b) Retrieve the tf-idfs of the unique words in the phrase for every document
    #Step 2: Find cosine similarity of the phrase and every page
        #a) For each document:
                #- For each term in the query vector, multiply it's query tfidf with the document tfidf of that term
                #- Add these values up from all the terms
            #- Divide the summed up value by the product of the euclidean norm of the query multiplied by the euclidean norm of the document
    #Step 3: Multiply by pageRank is boost is True
    # crawler.crawl("http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html")

    phraseWords = phrase.split()
    
    
    cosineSimilarities = []
    documentVectors = []
    
    urlSimMap = {}

    
    phraseVector,phraseUniques = getPhraseVector(phraseWords)

    #NOTE: CARE ABOUT DOCUMENTVECTOR VS DOCUMENTVECTORS
    files = os.listdir("pages")
    for url in files:
        documentVector = []
        for word in phraseUniques:
            documentVector.append(searchdata.get_tf_idf(url + ".html",word))
        # print(documentVector)
        sim = cosineSim(phraseVector,documentVector)
        if boost:
            sim = sim*searchdata.get_page_rank(url+".html")
        
        if sim in urlSimMap:
            urlSimMap[sim].append(url)
        else:
            urlSimMap[sim] = [url]

        #Insert the doasort
        insert = 0
        if (length:=len(cosineSimilarities))>=1:
            for i in range(10):
                print("length",length,"i",i)
                if i == length:
                    cosineSimilarities.insert(insert,sim)
                    break
                elif sim<cosineSimilarities[i]:
                    insert+=1
                elif insert == 10:
                    break
                else:
                    cosineSimilarities.insert(insert,sim)
                    print(cosineSimilarities)
                    break
        else:
            cosineSimilarities.append(sim)
        documentVectors.append(documentVector)
    
    results = []
    for i in cosineSimilarities:
        result = {}
        URL = urlSimMap[i].pop(0)
        new_url = URL.replace('{','/').replace('}',':') + ".html"
        result["url"] = new_url
        result["title"] = searchdata.get_title(new_url)
        result["score"] = i
        results.append(result)
    return results

# Still reading
def cosineSim(a, b):
    if (en_a:=euclidean_norm(a)) == 0 or (en_b:=euclidean_norm(b)) == 0:
        return 0
    return (float(crawler.dotProduct(a, b))/(en_a*en_b))

def euclidean_norm(a):
    sum = 0
    for i in range(len(a)):
        sum += a[i]**2
    return sum**0.5

def getPhraseVector(phraseWords):
    phraseUniques = {}
    phraseIdfs = {}
    phraseVector = []
    for word in phraseWords:
        if (idf:=searchdata.get_idf(word)) == 0:
            phraseWords = list(filter((word).__ne__,phraseWords))
        else:
            if word in phraseUniques:
                phraseUniques[word] += 1
            else:
                phraseUniques[word] = 1
            phraseIdfs[word] = idf

    for word in phraseUniques:
        tf = phraseUniques[word]/len(phraseWords)
        print(tf)
        phraseVector.append( log(1+tf, 2) * phraseIdfs[word])
    return phraseVector,phraseUniques

# crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
# print(search('coconut coconut orange blueberry lime lime lime tomato',True))
# search("I want an apple", False)

