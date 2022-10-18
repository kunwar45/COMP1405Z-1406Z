import webdev

urlDict = {}
# I don't know if relativeLink should be defined as a hardcoded variable, lemme know if you think of a better way
relativeLink = 'http://people.scs.carleton.ca/~davidmckenney/fruits/'

def crawl(seed):
    global urlDict
    parse

    # Most likely we should store this differently, perhaps a nested dictionary
    urlDict[seed.strip(relativeLink)] = parse(seed)

    for url in urlDict[seed.strip(relativeLink)]:
        urlDict[url] = parse(relativeLink + url)

    """
    This code gets every URl in the in the seed file. Now my thought process was to make a function which essentially returns in the list without duplicates
    This might not be the best way but its where my mind went so lemme know if there is a better way to do this. Like for example, checking if duplicate already exists before appending etc.
    """
    urlsWithoutDuplicates = removeDuplicates(urlDict)

    return len(urlsWithoutDuplicates)

# Returns list of urls present in a given webpage --- could rename to getUrls(seed) for clarity
def parse(url):
    urlList = []
    for index in webdev.read_url(url).split():
        if "href" in index:
            """
            Here I tried the line:
            urlList.append(createSubString(index, '"', '"')
            But it was returning empty strings so I had to take the characters before and after the double quotes, respectively and then strip the double quotes.
            Lemme know if you think of a better way.
            """
            urlList.append(createSubString(index, '/', '>').strip('"'))
            # urlList.append(index)
        elif "<" not in index:

    return urlList

# Returns non inclusive substring from in between two characters of a string
def createSubString(str, start, end):
    return str[(str.index(start)+1):str.index(end)]

# Remove the duplicates, this is not the cleanest way of doing this I suppose
def removeDuplicates(dict):
    newList = []
    for urlList in dict.values():
        for item in urlList:
            if item not in newList:
                newList.append(item)
    return newList

print(crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html'), urlDict)
print(webdev.read_url("http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html"))

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