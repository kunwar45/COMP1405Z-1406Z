import search
import crawler

prompt = str(input("What link would you like to crawl? "))
crawler.crawl(prompt)

while(True):
    prompt = str(input("What is your search query? (Type n to end)"))
    if prompt.lower() == 'n':
        break
    boost = bool(input("Would you like to boost (True or False)? "))
    search.search(prompt, boost)
