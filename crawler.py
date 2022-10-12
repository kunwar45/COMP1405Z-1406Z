import webdev

urlDict = {}
# I don't know if relativeLink should be defined as a hardcoded variable, lemme know if you think of a better way
relativeLink = 'http://people.scs.carleton.ca/~davidmckenney/fruits/'

def crawl(seed):
    global urlDict
    
    totalPages = 0
    return totalPages

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
            urlList.append(createSubString(index, '=', '>').strip('"'))
    return urlList

# Returns non inclusive substring from in between two characters of a string
def createSubString(str, start, end):
    return str[(str.index(start)+1):str.index(end)]

print(parse('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html'))