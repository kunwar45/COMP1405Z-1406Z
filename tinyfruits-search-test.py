
import testingtools
import crawler
import searchdata
import search
output = open('tinyfruits-search-failed.txt', 'w')
success_output = open('tinyfruits-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
#Test #0 checking search results for 'coconut coconut orange blueberry lime lime lime tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29114699312854103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0773023258458759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07491464806478916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06552765463688297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04269051023692432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.034865703393258916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03473830270000377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03026764776674082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.026364400306154893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026364400306154893}]
result = search.search('coconut coconut orange blueberry lime lime lime tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'coconut coconut orange blueberry lime lime lime tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'coconut coconut orange blueberry lime lime lime tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'coconut coconut orange blueberry lime lime lime tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9029831796862584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.899927800610306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7995513215997765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7536309452206319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6542428167522454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6474598285394256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6297155349056148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.569873141487924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.569873141487924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2784293793188435}]
result = search.search('coconut coconut orange blueberry lime lime lime tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'coconut coconut orange blueberry lime lime lime tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'coconut coconut orange blueberry lime lime lime tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'coconut fig cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.28932580545468994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1005684438398008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09596876141664096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04515319497421663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03571072686011265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.029776428491938168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029412029356386267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.028030888547907855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut fig cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'coconut fig cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'coconut fig cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'coconut fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9759976623540498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.897334823785796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8423294731754587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8066916349582863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7718963399231442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6357484096820485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6276953743130186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6058947038429281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'coconut fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'coconut fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'blueberry kiwi cherry lime coconut tomato peach fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.295514723512874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10517895844659146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0832011507052527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04657757332284148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04282448757795409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04193850612881486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03610408580619136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.033671142587279525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.023026220913970663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021944947228840918}]
result = search.search('blueberry kiwi cherry lime coconut tomato peach fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'blueberry kiwi cherry lime coconut tomato peach fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'blueberry kiwi cherry lime coconut tomato peach fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'blueberry kiwi cherry lime coconut tomato peach fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9256620664708206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9165295571640983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8809456850956909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.780398892445908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7097970280617001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6993699960494947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5117226945940531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.49771755459865324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4743455520270924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.37332177517283444}]
result = search.search('blueberry kiwi cherry lime coconut tomato peach fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'blueberry kiwi cherry lime coconut tomato peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'blueberry kiwi cherry lime coconut tomato peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'coconut apricot banana apricot apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3195974343084476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10265342611740245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08442376869993334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.044238146876788224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04412558625023501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04274693519677292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut apricot banana apricot apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'coconut apricot banana apricot apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'coconut apricot banana apricot apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'coconut apricot banana apricot apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9912213220900395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9562186676551894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9537856414108277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9011172544194608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8628814098079822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut apricot banana apricot apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'coconut apricot banana apricot apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'coconut apricot banana apricot apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'pear lime pear fig coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2673445015399663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11410509050828616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11407552863534103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04329323641897731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04208456704820778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02399585731008344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.016362027783678346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.009236311165031394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.009236311165031394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear lime pear fig coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'pear lime pear fig coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'pear lime pear fig coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'pear lime pear fig coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9588930121131809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9557081436756283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9357941905282893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8871543500684846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.829160505757363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5186764890988557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.1996451881421188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.1996451881421188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.1996451881421188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear lime pear fig coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'pear lime pear fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'pear lime pear fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'fig peach peach cherry lime tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29552729875947376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10535922171584497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06766250720884968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04110324242922128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.039311527567157584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.038098769492631926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.033565833963364364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.017579916752963685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017579916752963685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig peach peach cherry lime tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'fig peach peach cherry lime tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'fig peach peach cherry lime tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'fig peach peach cherry lime tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9165685588932179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8824555132169759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8286979084064549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.823514481856877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7255339406638778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5687556842451772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5015310251592909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3799943207799335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3799943207799335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig peach peach cherry lime tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'fig peach peach cherry lime tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'fig peach peach cherry lime tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'blueberry fig banana papaya papaya blueberry kiwi pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29701956818529746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11198596199172842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09413359669415561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05828628858328532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05186630871058225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03299514887620972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.030044043285873182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.028499105510466215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.028454977187392556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.028454977187392556}]
result = search.search('blueberry fig banana papaya papaya blueberry kiwi pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'blueberry fig banana papaya papaya blueberry kiwi pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'blueberry fig banana papaya papaya blueberry kiwi pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'blueberry fig banana papaya papaya blueberry kiwi pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9413285889904097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9211967852629952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7884332289938338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7131984390161803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7111940649510259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6333367684209863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6160153312136472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6150614864151099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6150614864151099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4157112760101942}]
result = search.search('blueberry fig banana papaya papaya blueberry kiwi pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'blueberry fig banana papaya papaya blueberry kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'blueberry fig banana papaya papaya blueberry kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'lime tomato apple fig fig blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2285671127432784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1009703713660331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08536874277964576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04583225013578842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.043500079715278306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.026266155836749194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.02488435375546645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.015218458583031075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.013170883390915988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.013137371071992011}]
result = search.search('lime tomato apple fig fig blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'lime tomato apple fig fig blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'lime tomato apple fig fig blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'lime tomato apple fig fig blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9906756104080462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9402651603849883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8487340334214925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7150215851582246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7088936623347201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.3208093294106502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.30363238303878953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.28469195608443887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.2839675788848068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2105246629311369}]
result = search.search('lime tomato apple fig fig blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'lime tomato apple fig fig blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'lime tomato apple fig fig blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'fig kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3084041414467189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10901827878433282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.049943869505471396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04470253788755517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018989447476008524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('fig kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'fig kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'fig kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9662565961159679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9565056787277847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.4003028215649755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'fig pear lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3128293736625128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1177333333244985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.045421889404052916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03403385304041906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03385338337457973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.024187257096552783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('fig pear lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'fig pear lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'fig pear lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'fig pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9896396884430357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.981805560013507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9702303963150396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7317493934866013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7174430650507335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.29512659173577693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('fig pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'fig pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'fig pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'coconut banana pear fig tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31572695426973907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11642794474840724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11102622037622972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04008103988466844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.032823240515045954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.031500778218540415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.023104842035861595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.023104842035861595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut banana pear fig tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'coconut banana pear fig tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'coconut banana pear fig tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'coconut banana pear fig tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.979217150813154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9751636360113886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9332612187178796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8663617547881952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6919230171219551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6808972415171206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4994169699162408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4994169699162408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut banana pear fig tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'coconut banana pear fig tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'coconut banana pear fig tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'kiwi peach tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30529974367124346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.043731231208801805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi peach tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'kiwi peach tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'kiwi peach tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'kiwi peach tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9468774873314472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9218664874536563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi peach tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'kiwi peach tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'kiwi peach tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'blueberry tomato lime tomato apricot cherry pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.289803375815117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10045980360981516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08092671165139946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04629651032686436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04344007463733084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.025811605918250217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.020822045105215924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02000314871688074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.015298521434487367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.015298521434487367}]
result = search.search('blueberry tomato lime tomato apricot cherry pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'blueberry tomato lime tomato apricot cherry pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'blueberry tomato lime tomato apricot cherry pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'blueberry tomato lime tomato apricot cherry pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9759432830191689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9389681355379197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8988159931358499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8414195369748424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6802515773903194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4323730889595753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3306813873538534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3306813873538534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.2540651542397013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.20688142069302123}]
result = search.search('blueberry tomato lime tomato apricot cherry pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'blueberry tomato lime tomato apricot cherry pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'blueberry tomato lime tomato apricot cherry pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'orange orange blueberry apple lime pear pear fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.23476829075388167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10622211412872135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10081643375486272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043528323567171574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.039919180579481045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.025376585535243145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.022539971503926913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.021354195415116704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017904762834840757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.014727419636842688}]
result = search.search('orange orange blueberry apple lime pear pear fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'orange orange blueberry apple lime pear pear fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'orange orange blueberry apple lime pear pear fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'orange orange blueberry apple lime pear pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9408756583450871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8928789915628269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.844406558258327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8415074025043141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7281264195672251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5485212768458053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3870159505166096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3183368784041393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.2605583132872618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.18065909350551282}]
result = search.search('orange orange blueberry apple lime pear pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'orange orange blueberry apple lime pear pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'orange orange blueberry apple lime pear pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'fig orange papaya papaya pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3016547705218454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1129878382289181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0764073847450164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05415484722176604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.034580840036754004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.033165529695999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03224109911495247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02760028648780294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.025409561949654328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig orange papaya papaya pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'fig orange papaya papaya pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'fig orange papaya papaya pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'fig orange papaya papaya pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9497501333333199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9355727185308251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7474735521458367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6991385680272557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6968994638338939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6607832968712017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6399640849718822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5965871320463538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5492340703346494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig orange papaya papaya pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'fig orange papaya papaya pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'fig orange papaya papaya pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'orange papaya blueberry cherry fig cherry banana apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2996572304828386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11403597409477861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06270348000767847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04061524008846338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038597228742127086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03350588402239539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03343777108096801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.031693748741924016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.028648989091619753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.027613062052421398}]
result = search.search('orange papaya blueberry cherry fig cherry banana apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'orange papaya blueberry cherry fig cherry banana apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'orange papaya blueberry cherry fig cherry banana apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'orange papaya blueberry cherry fig cherry banana apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9585605256193959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9293774113542312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8779086265085825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8136402909870166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7242381076164623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6850683478991425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5968632790877756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5251845137951011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4079989465102959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.22962320064333885}]
result = search.search('orange papaya blueberry cherry fig cherry banana apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'orange papaya blueberry cherry fig cherry banana apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'orange papaya blueberry cherry fig cherry banana apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'apricot papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apricot papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'apricot papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'apricot papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'apricot papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apricot papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'apricot papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'apricot papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'apple kiwi pear kiwi blueberry peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27707626502436816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10724265441380534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08331262616762437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06939362230437214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06127470819645287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04000269670367481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03912626306194887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.024745600376793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.012696039542126012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.012696039542126012}]
result = search.search('apple kiwi pear kiwi blueberry peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'apple kiwi pear kiwi blueberry peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'apple kiwi pear kiwi blueberry peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'apple kiwi pear kiwi blueberry peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8982305497161142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8593432620368349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8457240137030685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8432679455745204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7476579802924719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7003070334945016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.55619364462762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5348823739956504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.27442808690160797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.27442808690160797}]
result = search.search('apple kiwi pear kiwi blueberry peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'apple kiwi pear kiwi blueberry peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'apple kiwi pear kiwi blueberry peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'apricot lime banana apple fig orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2553441162519619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11225939300756645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0927607830516546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043780258574711774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04284816904623156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03506096440386093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.025181967023006208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021793846558397497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021738393760375684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apricot lime banana apple fig orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'apricot lime banana apple fig orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'apricot lime banana apple fig orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'apricot lime banana apple fig orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9463212968777489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9436269880731809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9261739473619319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7919416907925172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7769349761810731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.5308428517786657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4710794730438196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4698808468719355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4278047273477573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apricot lime banana apple fig orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'apricot lime banana apple fig orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'apricot lime banana apple fig orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'lime coconut lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.28881871502256595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11498777734064247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11457616518523235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07140996007155372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04622704983239531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04568731371271496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.040310688884251544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02270180269087849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02270180269087849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime coconut lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'lime coconut lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'lime coconut lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'lime coconut lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9992093051157284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9631012493665345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9631012493665345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9631012493665345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8957620988681609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8713256756554348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8713256756554348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.49070517313719036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.49070517313719036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime coconut lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'lime coconut lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'lime coconut lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'papaya papaya apricot kiwi fig papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26906484302157135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1042098107140048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0724134460768093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06098719430124879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04180673563351587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03977256358235763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03977256358235763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.025511800394298113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02284401389346559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.022834478685735793}]
result = search.search('papaya papaya apricot kiwi fig papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'papaya papaya apricot kiwi fig papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'papaya papaya apricot kiwi fig papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'papaya papaya apricot kiwi fig papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8835699497127788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8812975867602801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8759640256125802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8596939619527404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8596939619527404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8344960903859842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5108094476240628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.4937791040376466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4935729981251047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.20447846316595886}]
result = search.search('papaya papaya apricot kiwi fig papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'papaya papaya apricot kiwi fig papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'papaya papaya apricot kiwi fig papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'orange blueberry fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2993355458665578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11442502635135393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1014822699949074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.046366875422558455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.045654220977607574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04469028223388571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03045738220123482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.01762941786812988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.017193092628990235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017193092628990235}]
result = search.search('orange blueberry fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'orange blueberry fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'orange blueberry fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'orange blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9868274653916285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9659916870804313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.961830810619516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.928379716703347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8499833919835398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.37163302008004234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.37163302008004234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.37163302008004234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.37163302008004234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.37163302008004234}]
result = search.search('orange blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'orange blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'orange blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'apple blueberry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22768065382508063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11808293065114119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09313792885287137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07203323321735582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06691641239511242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.043825491249772475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03612029567147614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.036045311367756204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03602839030474836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03490272643330415}]
result = search.search('apple blueberry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'apple blueberry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'apple blueberry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'apple blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.992578324253725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9472990125221563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7807492727597276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7800938301109928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7791284681813208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7787627151498989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7357591572484694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7061443380706633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5773502691896257}]
result = search.search('apple blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'apple blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'apple blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'coconut pear peach pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2643994470676706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11801239321220171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09839087218965392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04720165308148134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0460592690433167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04237512327537963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.026716870105604317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.008814120745188747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.008814120745188747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut pear peach pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'coconut pear peach pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'coconut pear peach pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'coconut pear peach pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9950239434254311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.988434475141679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9159489440858273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.827051348584778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8200265125700499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5774918648254304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5620031670533069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.1905194360647743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.1905194360647743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut pear peach pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'coconut pear peach pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'coconut pear peach pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'pear apricot lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30840414144671885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11674212668155656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.046162724004906765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear apricot lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'pear apricot lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'pear apricot lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'pear apricot lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9813078302886417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9731230302322414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9565056787277846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear apricot lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'pear apricot lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'pear apricot lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'pear kiwi papaya lime apple apple lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3050164016304512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10770276807545615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09044141975105015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05840586744946476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04195676042995818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.033913101131748155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.031309149764517985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02732059024916117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.027320590249161163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.024739903625958595}]
result = search.search('pear kiwi papaya lime apple apple lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'pear kiwi papaya lime apple apple lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'pear kiwi papaya lime apple apple lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'pear kiwi papaya lime apple apple lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9459987109642792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9053250327065008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8844601510948373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7575087228504289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7330402078227892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7126531350340158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5905414275233524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5905414275233523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5347592372940158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2509445326450711}]
result = search.search('pear kiwi papaya lime apple apple lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'pear kiwi papaya lime apple apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'pear kiwi papaya lime apple apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'coconut kiwi papaya blueberry kiwi apricot orange papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.25491424665663986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08872523408462758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07228813043600046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06432590889617261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.058280161676533195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.042492364776465494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03894881216892005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03229779341474209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.023459415447958643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02249507959521983}]
result = search.search('coconut kiwi papaya blueberry kiwi apricot orange papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'coconut kiwi papaya blueberry kiwi apricot orange papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'coconut kiwi papaya blueberry kiwi apricot orange papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'coconut kiwi papaya blueberry kiwi apricot orange papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8957508393268262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8820408810045967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8418883680333066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7906084638549373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7458041876257246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6981249253786431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5155756469379797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5070811633700424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.48813619866460084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.48623680144759773}]
result = search.search('coconut kiwi papaya blueberry kiwi apricot orange papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'coconut kiwi papaya blueberry kiwi apricot orange papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'coconut kiwi papaya blueberry kiwi apricot orange papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'orange kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.22799097236207078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10360479815141346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045081493020550145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04405772409580497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04402627782870174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('orange kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'orange kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'orange kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'orange kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9523187838800627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.951639064910009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9503303810860111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}]
result = search.search('orange kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'orange kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'orange kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'papaya banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'papaya banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'papaya banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'papaya banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'papaya banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'papaya banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'kiwi coconut papaya papaya tomato cherry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.25686832392923864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07760646017940441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07006578487042821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.045777084375027526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.044529146371049544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04232895451757846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03942438762265066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03382571093570364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02439028678454221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.012542759805549792}]
result = search.search('kiwi coconut papaya papaya tomato cherry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'kiwi coconut papaya papaya tomato cherry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'kiwi coconut papaya papaya tomato cherry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'kiwi coconut papaya papaya tomato cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9625086948904146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8923061057300332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8549244010412719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8521680510408786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7966689726378149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6523422968194449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5272021813617203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.3834143782372543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.2711149068559864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2711149068559864}]
result = search.search('kiwi coconut papaya papaya tomato cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'kiwi coconut papaya papaya tomato cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'kiwi coconut papaya papaya tomato cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'coconut kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31673743285406164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0882223329527108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0841215639769089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045081493020550145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}]
result = search.search('coconut kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'coconut kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'coconut kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9823511181444725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9503303810860111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}]
result = search.search('coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'peach apple pear banana apple blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3037275024258463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10261587909018438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09754965182521937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05941014179343035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.044687448956108905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.039189284788192655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03560608263684987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02463983085328801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02463983085328801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.020438615542022157}]
result = search.search('peach apple pear banana apple blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'peach apple pear banana apple blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'peach apple pear banana apple blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'peach apple pear banana apple blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9420238228769824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9420012308956618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8625657980159026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8470862441615459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8170450261841219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7249070281943316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5325961391511811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5325961391511811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.4417858138755741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2853846825553882}]
result = search.search('peach apple pear banana apple blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'peach apple pear banana apple blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'peach apple pear banana apple blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'tomato banana peach coconut fig kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2915601708310884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09318080673176768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04937196694911028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04194093817658334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.040271216332424066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03986401639333151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.029691377634052857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.014781796706548818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.014781796706548818}]
result = search.search('tomato banana peach coconut fig kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'tomato banana peach coconut fig kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'tomato banana peach coconut fig kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'tomato banana peach coconut fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9065639240070463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9042646372469656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8704724665229966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7832567204118113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6259024786307705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6024238413978337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3195122524380067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3195122524380067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3195122524380067}]
result = search.search('tomato banana peach coconut fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'tomato banana peach coconut fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'tomato banana peach coconut fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'fig lime pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3128293736625128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1177333333244985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.045421889404052916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03403385304041906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03385338337457973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.024187257096552783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('fig lime pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'fig lime pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'fig lime pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'fig lime pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9896396884430357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.981805560013507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9702303963150396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7317493934866013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7174430650507335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.29512659173577693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('fig lime pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'fig lime pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'fig lime pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'cherry apricot peach blueberry coconut papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29073265286620753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08590480407874716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07798876096413625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.058035868582649794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.043275159255031254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.040132693634610916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.035373763450542925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03504851443345013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034955035860813465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.028058155411404738}]
result = search.search('cherry apricot peach blueberry coconut papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'cherry apricot peach blueberry coconut papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'cherry apricot peach blueberry coconut papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'cherry apricot peach blueberry coconut papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9122523641274426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9016981164831885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7646127911016998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7575824518190248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7555618889679203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7220962928989041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7081385055300047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6532091919526094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6064840839531923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.32166571509196984}]
result = search.search('cherry apricot peach blueberry coconut papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'cherry apricot peach blueberry coconut papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'cherry apricot peach blueberry coconut papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'tomato papaya apple orange apple blueberry kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29001270586531175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10837982109570186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0623627131524328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.061253267308005205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05850024077488301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04290398906295732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.038877349570698876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.036383148007248095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.034326974897051984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.023680281420176093}]
result = search.search('tomato papaya apple orange apple blueberry kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #80 checking search results for 'tomato papaya apple orange apple blueberry kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #80 checking search results for 'tomato papaya apple orange apple blueberry kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking search results for 'tomato papaya apple orange apple blueberry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9110161867840688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9044279934944515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8994652236578539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8403436860047272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7864308920870913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7609335325044568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7419861933211989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5130379909628098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5118552368924338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.468882601133872}]
result = search.search('tomato papaya apple orange apple blueberry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'tomato papaya apple orange apple blueberry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'tomato papaya apple orange apple blueberry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'papaya cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10323393269715217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04657076288956151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.044125586250235015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'papaya cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'papaya cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'papaya cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9817246031343432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9537856414108279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'papaya kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30529974367124346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10085465848703534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07723371404100288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04593784332870304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02453720402607222}]
result = search.search('papaya kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'papaya kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'papaya kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'papaya kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9683824831829646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9468774873314472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9423856000300839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}]
result = search.search('papaya kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'papaya kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'papaya kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'peach apricot coconut pear kiwi peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26693104390089917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11403110892907271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07259413507219065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.062410518246565364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04300950260111232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03651975559201241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0351456178953545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.031056758275424205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.011516016917666698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.011516016917666698}]
result = search.search('peach apricot coconut pear kiwi peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'peach apricot coconut pear kiwi peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'peach apricot coconut pear kiwi peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'peach apricot coconut pear kiwi peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9550884973704432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9066522481543152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8278781799824044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7893836993793757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7615168377731208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7596813675630661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6102098291706584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.2489216011777334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2489216011777334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.2489216011777334}]
result = search.search('peach apricot coconut pear kiwi peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'peach apricot coconut pear kiwi peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'peach apricot coconut pear kiwi peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'tomato cherry blueberry tomato pear banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31018365830695765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09982082009762684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08122745102411179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.046294072125290436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0433867601915417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.026529121597017636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.018401660715180075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.01742639737053074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01572379249379185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01572379249379185}]
result = search.search('tomato cherry blueberry tomato pear banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'tomato cherry blueberry tomato pear banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'tomato cherry blueberry tomato pear banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'tomato cherry blueberry tomato pear banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9758918850534924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9620247939193824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9378157303871962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8360676132039351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6827795243252224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.3977565231364826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.33987372822773876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.33987372822773876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.21263234775517528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.21263234775517528}]
result = search.search('tomato cherry blueberry tomato pear banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'tomato cherry blueberry tomato pear banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'tomato cherry blueberry tomato pear banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'coconut lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.31673743285406164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04743770578925645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04402627782870174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'coconut lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'coconut lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'coconut lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9823511181444725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.951639064910009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'coconut lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'coconut lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'papaya fig orange kiwi lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29223647342068854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11068412636394817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08704070807994352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05023007813179945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.039031258108691645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03825037716106169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03797282434180953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03331500512803056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02576150812821993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.025301459898821155}]
result = search.search('papaya fig orange kiwi lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'papaya fig orange kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'papaya fig orange kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'papaya fig orange kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9303856540653489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9063621683127167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8436704577510687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8267915197291004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7290254376272044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7022895516076086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6128942898520119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5568414754750967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.546897417325508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.3043542456227244}]
result = search.search('papaya fig orange kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'papaya fig orange kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'papaya fig orange kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking search results for 'apple pear lime kiwi tomato banana blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2786007424700814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1086772230945012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10437807925927958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05804431367496842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04433560004516509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04225973432556276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04200713700559511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02349572693133888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.015219166031952374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.015219166031952374}]
result = search.search('apple pear lime kiwi tomato banana blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #98 checking search results for 'apple pear lime kiwi tomato banana blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #98 checking search results for 'apple pear lime kiwi tomato banana blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking search results for 'apple pear lime kiwi tomato banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.913454782922989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9102460431940627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8855221032866385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8773784528271866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8640713805603957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.540971408277418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5078660452131978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4652283207120526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.3289661003755223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3289661003755223}]
result = search.search('apple pear lime kiwi tomato banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #99 checking search results for 'apple pear lime kiwi tomato banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #99 checking search results for 'apple pear lime kiwi tomato banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
