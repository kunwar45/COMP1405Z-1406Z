import webdev

urlDict = {}
# I don't know if relativeLink should be defined as a hardcoded variable, lemme know if you think of a better way
relativeLink = 'http://people.scs.carleton.ca/~davidmckenney/fruits/'

def crawl(seed):
    global urlDict

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

print(crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html'))