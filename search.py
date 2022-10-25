import crawler
import searchdata
import os
import time
from math import log, sqrt

#Search function, returns the top 10 search results for a phrase, O(n^2) as cosineSim is O(n) and it's being looped for each url
#We can never make this O(n), with cosineSim as O(1) because even if the euclidean_norms were stored elsewhere for O(1) lookup,
#We would have to do the dotproduct (O(n)) of EACH URL in search() as we won't have the query vector from before search()
def search(phrase:str, boost):
    phraseWords = phrase.split()
    cosineSimilarities = []
    urlSort = []
    
    phraseVector,phraseUniques = getPhraseVector(phraseWords)

    #Creates top 10 list of urls ordered by cosine similarity, O(n^2) due to looping cosineSim() n times
    files = os.listdir("pages")
    for url in files:
        documentVector = []
        for word in phraseUniques:
            documentVector.append(searchdata.get_tf_idf(url,word))
        sim = cosineSim(phraseVector,documentVector)
        if boost:
            sim = sim*searchdata.get_page_rank(url)
        
        #Inserts new cosine similarity into the top 10 which makes it worst case O(11) which is O(1)
        list_cap = 11
        insert = 0
        if (length:=len(cosineSimilarities))>=1:
            for i in range(list_cap):
                if i == length:
                    cosineSimilarities.insert(insert,sim)
                    urlSort.insert(insert,url)
                    break
                elif sim<cosineSimilarities[i]:
                    insert+=1
                elif insert == list_cap-1:
                    break
                else:
                    cosineSimilarities.insert(insert,sim)
                    urlSort.insert(insert,url)
                    break
        else:
            cosineSimilarities.append(sim)
            urlSort.append(url)
        if length>10:
            cosineSimilarities.pop(10)
            urlSort.pop(10)
    
    results = []
    #Formats the top 10 cosine similarities into results
    if len(cosineSimilarities)>10:
        length = 10
    else:
        length = len(cosineSimilarities)

    for i in range(length):
        result = {}
        URL = urlSort[i]
        new_url = URL.replace('{','/').replace('}',':').replace('(','.')
        result["url"] = new_url
        result["title"] = searchdata.get_title(new_url)
        result["score"] = cosineSimilarities[i]
        results.append(result)

        print(f"{i+1}. { searchdata.get_title(new_url)} with a score of {cosineSimilarities[i]}")
    return results

#Returns the cosine similarity of two vectors, O(n) as both crawler.dotProduct and euclidean_norm are O(n) with n being the length of the vector
def cosineSim(a, b):
    if (en_a:=euclidean_norm(a)) == 0 or (en_b:=euclidean_norm(b)) == 0:
        return 0
    return (float(crawler.dotProduct(a, b))/(en_a*en_b))

#Returns the euclidean norm of a vector, O(n) with n being the length of the vector
def euclidean_norm(a):
    sum = 0.0
    for i in range(len(a)):
        sum += a[i]**2
    return sqrt(sum)

#Returns the phraseVector and the dictionary of unique words in phraseWords
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
        phraseVector.append( log(1+tf, 2) * phraseIdfs[word])
    return phraseVector,phraseUniques

start = time.time()
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')
end = time.time()
print(f"Crawl time is {end-start}")

start = time.time()
search('pear apple banana banana tomato tomato',True)
end = time.time()
print(f"Search time is {end-start}")