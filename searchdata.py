from matmult import mult_scalar


dictionary = {"0":{ "outgoinglinks": [1], "incominglinks": [0,1], "countAll": {"word": 0}, "wordCount": 0, "wordVectors":{"word": 0}}, 
              "1":{ "outgoinglinks": [0,2], "incominglinks": [0,1], "countAll": {"word": 0}, "wordCount": 0, "wordVectors":{"word": 0}},
              "2":{ "outgoinglinks": [1], "incominglinks": [0,1], "countAll": {"word": 0}, "wordCount": 0, "wordVectors":{"word": 0}},}

def get_outgoing_links(URL):
    return []

def get_incoming_links(URL):
    return []

def get_page_rank(URL):
    matrix = []
    for i in range(len(dictionary)):
        matrix.append([])
        for j in range(len(dictionary)):
            if len(ogIndexes:=dictionary[str(i)]["outgoinglinks"]) == 0:
                matrix[i].append(1/len(dictionary))
            else:
                matrix[i].append(1/len(ogIndexes) if int(j) in ogIndexes else 0)
    

    matrix = mult_scalar(matrix, 0.5) #Multiply matrix by 1-alpha

    # Add alpha/N to each of the elements in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix[i][j]+= (0.5/len(dictionary))
    
    print(matrix)

    pi = [1]
    for i in range(len(matrix)-1):
        pi.append(0)
    
    while(True):
        for i in range(len(pi)):
            pi[i] = sum(row[i] for row in matrix)

    pageRank = 0
    return pageRank

def get_idf(word):
    # counter = 0
    # for url in dictionary:
    #     if word in url[countAll]:
    #         counter +=1
    #idf = math.log( len(dictionary)/(1 + counter), 2)
    return 0

def get_tf(URL, word):
    # return dictionary[URL][countAll][word]/(dictionary[URL])[wordCount]
    return 0

def get_tf_idf(URL, word):
    #tfidf = math.log( 1+ get_tf(URL,word) , 2)* get_idf(word)
    tfidf = 0 
    return tfidf

get_page_rank('1')