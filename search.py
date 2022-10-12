def search(phrase, boost):
    #Step 1: Find phrase's vector:
        #a) Find tf-idf of every unique word in the phrase
    #Step 2: Find cosine similarity of the phrase and every page
        #a) For each document:
                #- For each term in the query vector, multiply it's query tfidf with the document tfidf of that term
                #- Add these values up from all the terms
            #- Divide the summed up value by the product of the euclidean norm of the query multiplied by the euclidean norm of the document
    return []