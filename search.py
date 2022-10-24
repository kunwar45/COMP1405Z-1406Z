import crawler
import searchdata
import matmult as mat

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

    phraseWords = phrase.split()
    phraseIdfs = []
    for word in phraseWords:
        if idf:=searchdata.get_idf(word) == 0:
            phraseWords = list(filter((word).__ne__,phraseWords))
        
    print(phraseWords)
    return []

# Still reading
def cosineSim(a, b):
    return (crawler.dotProduct(a, b))/(mat.euclidean_dist(a, b))

search("Gang",False)
# search("I want an apple", False)