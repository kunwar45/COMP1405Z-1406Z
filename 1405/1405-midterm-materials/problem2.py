def analyze(filename):
    fhand = open(filename).readlines()
    listCounts = [0]
    maxCount = 0
    for i in fhand:
        if int(i.strip())%2 == 1:
            maxCount+=1
        else:
            listCounts.append(maxCount)
            maxCount = 0
    listCounts.append(maxCount)
    return max(listCounts)