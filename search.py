import crawler
import searchdata
import matmult as mat
import os
from math import log, sqrt

def search(phrase:str, boost):
    phraseWords = phrase.split()
    cosineSimilarities = []
    documentVectors = []
    urlSort = []
    
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
        
        insert = 0
        if (length:=len(cosineSimilarities))>=1:
            for i in range(10):
                # print("length",length,"i",i)
                if i == length:
                    cosineSimilarities.insert(insert,sim)
                    urlSort.insert(insert,url)
                    break
                elif sim<cosineSimilarities[i]:
                    insert+=1
                elif insert == 9:
                    # print("at max")
                    break
                else:
                    cosineSimilarities.insert(insert,sim)
                    urlSort.insert(insert,url)
                    # print(cosineSimilarities)
                    break
        else:
            cosineSimilarities.append(sim)
            urlSort.append(url)
        if length>10:
            cosineSimilarities.pop(10)
            urlSort.pop(10)
        documentVectors.append(documentVector)
    
    results = []
    for i in range(len(cosineSimilarities)):
        result = {}
        URL = urlSort[i]
        new_url = URL.replace('{','/').replace('}',':') + ".html"
        result["url"] = new_url
        result["title"] = searchdata.get_title(new_url)
        result["score"] = cosineSimilarities[i]
        results.append(result)
    # print(urlSort)
    return results

# Still reading
def cosineSim(a, b):
    if (en_a:=euclidean_norm(a)) == 0 or (en_b:=euclidean_norm(b)) == 0:
        return 0
    return (float(crawler.dotProduct(a, b))/(en_a*en_b))

def euclidean_norm(a):
    sum = 0.0
    for i in range(len(a)):
        sum += a[i]**2
    return sqrt(sum)

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
        # print(tf)
        phraseVector.append( log(1+tf, 2) * phraseIdfs[word])
    return phraseVector,phraseUniques

# crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')
# print(len(search('banana peach tomato tomato pear peach peach',False)))
# search("I want an apple", False)

