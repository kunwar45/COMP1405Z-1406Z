
import testingtools
import crawler
import searchdata
import search
output = open('fruits2-search-failed.txt', 'w')
success_output = open('fruits2-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')
#Test #0 checking search results for 'tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'pear apple banana banana tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014755826559580458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011719504815071996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01085306800911093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.00958230275179781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009359803338655734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009166200711120896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008199775525083003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007561100572674869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007323098209274983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007160889043871164}]
result = search.search('pear apple banana banana tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'pear apple banana banana tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'pear apple banana banana tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'banana peach coconut banana peach coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015232665899595835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011632099472918688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010947635542353087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01068867215369517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010478861116047657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009649858202255108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008759347049154454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007877578955608387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007416077413073041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007359548790400669}]
result = search.search('banana peach coconut banana peach coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'banana peach coconut banana peach coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'banana peach coconut banana peach coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'banana banana pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014891520186207277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011757736446136818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010913537857246842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009662115771747045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009423538112991937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009222788972846927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008251246889314955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007577431417968408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007319335749386361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007193806825724004}]
result = search.search('banana banana pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'banana banana pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'banana banana pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'pear apple peach coconut pear apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-90.html', 'title': 'N-90', 'score': 0.9995017636961095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-619.html', 'title': 'N-619', 'score': 0.9957202765197342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-641.html', 'title': 'N-641', 'score': 0.9931311385556205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-594.html', 'title': 'N-594', 'score': 0.9927520606940768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html', 'title': 'N-919', 'score': 0.9921385955205577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-462.html', 'title': 'N-462', 'score': 0.9884880223251084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-821.html', 'title': 'N-821', 'score': 0.987855856038467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-707.html', 'title': 'N-707', 'score': 0.9876354895596652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-785.html', 'title': 'N-785', 'score': 0.987359315952615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-134.html', 'title': 'N-134', 'score': 0.9872384740418036}]
result = search.search('pear apple peach coconut pear apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'pear apple peach coconut pear apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'pear apple peach coconut pear apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'pear peach coconut coconut coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-413.html', 'title': 'N-413', 'score': 0.9896406496726318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-537.html', 'title': 'N-537', 'score': 0.9812734042973792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.97961507217617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-807.html', 'title': 'N-807', 'score': 0.9669977063929894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-250.html', 'title': 'N-250', 'score': 0.9667121316239959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-854.html', 'title': 'N-854', 'score': 0.9657755135341863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-308.html', 'title': 'N-308', 'score': 0.9651017114492267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-370.html', 'title': 'N-370', 'score': 0.9628276680462446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-746.html', 'title': 'N-746', 'score': 0.961630469516465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-788.html', 'title': 'N-788', 'score': 0.9584219653099854}]
result = search.search('pear peach coconut coconut coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'pear peach coconut coconut coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'pear peach coconut coconut coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'tomato pear coconut banana banana banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013445124108257296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010750185792533534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.00988430233190658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.008694410183981737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.00869433949135795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00834788042862835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.0076485764615256465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0072422045666702085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007167982100917517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.00658719500396883}]
result = search.search('tomato pear coconut banana banana banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'tomato pear coconut banana banana banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'tomato pear coconut banana banana banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'tomato pear coconut banana banana banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-553.html', 'title': 'N-553', 'score': 0.9941934596640045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-53.html', 'title': 'N-53', 'score': 0.989668456368943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html', 'title': 'N-848', 'score': 0.9890204159742366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-666.html', 'title': 'N-666', 'score': 0.9882839160872913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 0.9855671001300641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-258.html', 'title': 'N-258', 'score': 0.9847760382287285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html', 'title': 'N-917', 'score': 0.9837655811292295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-801.html', 'title': 'N-801', 'score': 0.9832203239901083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.9815631546663481}]
result = search.search('tomato pear coconut banana banana banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'tomato pear coconut banana banana banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'tomato pear coconut banana banana banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'pear tomato coconut peach banana banana banana pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014592951376891912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01098068735556652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01037935713409913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009617772999875675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009564852362972142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.008833106473226729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008193624031861762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007269073961728897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007235131707972523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0068872055809681655}]
result = search.search('pear tomato coconut peach banana banana banana pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'pear tomato coconut peach banana banana banana pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'pear tomato coconut peach banana banana banana pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'pear tomato coconut peach banana banana banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-253.html', 'title': 'N-253', 'score': 0.9999898572917161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html', 'title': 'N-609', 'score': 0.9970627428477153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-840.html', 'title': 'N-840', 'score': 0.9966476594750283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-280.html', 'title': 'N-280', 'score': 0.99611513874561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-258.html', 'title': 'N-258', 'score': 0.9950044133711018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-694.html', 'title': 'N-694', 'score': 0.9938431380659182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-579.html', 'title': 'N-579', 'score': 0.99323369259951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.992077765059079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html', 'title': 'N-718', 'score': 0.9920518849460873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-212.html', 'title': 'N-212', 'score': 0.9903485058466356}]
result = search.search('pear tomato coconut peach banana banana banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'pear tomato coconut peach banana banana banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'pear tomato coconut peach banana banana banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'tomato coconut banana banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014527422822819772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011312595357173562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010582891467349134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009793825164607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009354206797174016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00897143555157799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008938513954582096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007756899216020201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007622578774242248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007391881240471361}]
result = search.search('tomato coconut banana banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'tomato coconut banana banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'tomato coconut banana banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'banana peach peach banana peach coconut pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.012218776372004685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01003728001309618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010021676023794519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009206192844280566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009101185733601002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.008692237370322346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008256357895503698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00717037023381943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.006757372792445074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0067175905053519155}]
result = search.search('banana peach peach banana peach coconut pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'banana peach peach banana peach coconut pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'banana peach peach banana peach coconut pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'banana peach peach banana peach coconut pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-643.html', 'title': 'N-643', 'score': 0.9967979372423516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-802.html', 'title': 'N-802', 'score': 0.9913947753169928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-234.html', 'title': 'N-234', 'score': 0.9891774184611725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-613.html', 'title': 'N-613', 'score': 0.9874744228662591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-874.html', 'title': 'N-874', 'score': 0.9869767270443427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-390.html', 'title': 'N-390', 'score': 0.9869767270443427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 0.9845761426064517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-40.html', 'title': 'N-40', 'score': 0.9791783671433001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-53.html', 'title': 'N-53', 'score': 0.9791428524608708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html', 'title': 'N-861', 'score': 0.9772148412168439}]
result = search.search('banana peach peach banana peach coconut pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'banana peach peach banana peach coconut pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'banana peach peach banana peach coconut pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'pear tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'pear tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'pear tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01760043385328955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012113974494578992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012090788373318907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735556738228342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001729294882303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049859168975073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009027256499602359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007793463871817541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007253331382606732}]
result = search.search('apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'pear coconut coconut tomato coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html', 'title': 'N-255', 'score': 0.9998521882500488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-864.html', 'title': 'N-864', 'score': 0.9968083150485416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-413.html', 'title': 'N-413', 'score': 0.9907464328719213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html', 'title': 'N-256', 'score': 0.9895941120910848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-351.html', 'title': 'N-351', 'score': 0.9895931464904099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-537.html', 'title': 'N-537', 'score': 0.9887246792852062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.9833199553425468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-788.html', 'title': 'N-788', 'score': 0.9799675313646403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-202.html', 'title': 'N-202', 'score': 0.9774707569712586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'title': 'N-248', 'score': 0.9773339183125139}]
result = search.search('pear coconut coconut tomato coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'pear coconut coconut tomato coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'pear coconut coconut tomato coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'peach peach banana peach apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9944653470286094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html', 'title': 'N-290', 'score': 0.9941894944015716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-122.html', 'title': 'N-122', 'score': 0.9903299627007025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-964.html', 'title': 'N-964', 'score': 0.9900138324749637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-768.html', 'title': 'N-768', 'score': 0.9875610751219823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-524.html', 'title': 'N-524', 'score': 0.987054189982867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9867980367857454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-546.html', 'title': 'N-546', 'score': 0.986333789026565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.9849421661895418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-970.html', 'title': 'N-970', 'score': 0.9842838112009579}]
result = search.search('peach peach banana peach apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'peach peach banana peach apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'peach peach banana peach apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'banana banana apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015308099512549439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011755002128742415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01076093339956093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010319186143919697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010294891389279026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009338517799835138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00828857303989262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0076922558838949965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007626783615365798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007413747620440299}]
result = search.search('banana banana apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'banana banana apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'banana banana apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016095350631103317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01173849251039794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01173717685922528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010985216997917413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010879474014584126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129116652445442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851592713703313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007840601893309988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074259064541596365}]
result = search.search('peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'apple banana banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015369568474357501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011721002456452079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011248230667082538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010749769503502043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010444751957286884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009189684274774927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008265801352796164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007767435195391194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007578465418222607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007412290383079957}]
result = search.search('apple banana banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'apple banana banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'apple banana banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'pear peach pear banana pear pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-462.html', 'title': 'N-462', 'score': 0.9948723631096205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-291.html', 'title': 'N-291', 'score': 0.9917085013817878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-542.html', 'title': 'N-542', 'score': 0.985874371306029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html', 'title': 'N-919', 'score': 0.9848158294081079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-464.html', 'title': 'N-464', 'score': 0.9801752890813109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-619.html', 'title': 'N-619', 'score': 0.9739685344461386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-118.html', 'title': 'N-118', 'score': 0.9699471523789575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-345.html', 'title': 'N-345', 'score': 0.968152813870874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html', 'title': 'N-187', 'score': 0.967040602541072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html', 'title': 'N-159', 'score': 0.9665475293857531}]
result = search.search('pear peach pear banana pear pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'pear peach pear banana pear pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'pear peach pear banana pear pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'banana pear banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013716873586519336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011914959976089995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011167035081936918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009737275597155278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009418037712933848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00934004734065954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008239589770669228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007772965346398517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007332479304237139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007200403401611276}]
result = search.search('banana pear banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'banana pear banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'banana pear banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'peach pear apple banana tomato coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015014386136917543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01150619284906365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010764705691226194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010185848671101077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009806822441484963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009334742400079931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008374613045077174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007621742972801732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007322154281901735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007040618735236562}]
result = search.search('peach pear apple banana tomato coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'peach pear apple banana tomato coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'peach pear apple banana tomato coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'apple banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015469688248481307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01175101558301189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011293518586939718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010799446051210047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010478821573120606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009232769545516419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008304121444387377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007779022748677028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0076001029823598515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007416838162734326}]
result = search.search('apple banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'apple banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'apple banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'tomato tomato banana banana coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015230506653695837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011418773893517926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010679483909657065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01000100104615979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009794036834400152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009095730803647768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008414497971276651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007611404364669743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007532365892282671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.00738940937010634}]
result = search.search('tomato tomato banana banana coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'tomato tomato banana banana coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'tomato tomato banana banana coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'apple coconut apple pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9999530758407115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-797.html', 'title': 'N-797', 'score': 0.9997592242707691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-865.html', 'title': 'N-865', 'score': 0.9997105889721634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-163.html', 'title': 'N-163', 'score': 0.9997105889721634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html', 'title': 'N-695', 'score': 0.9996584478128838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-551.html', 'title': 'N-551', 'score': 0.9994011244383982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html', 'title': 'N-867', 'score': 0.9989252694290002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9987414073692988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-605.html', 'title': 'N-605', 'score': 0.9982094995744437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html', 'title': 'N-939', 'score': 0.9980159754146594}]
result = search.search('apple coconut apple pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'apple coconut apple pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'apple coconut apple pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'tomato apple apple tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato apple apple tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'tomato apple apple tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'tomato apple apple tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'coconut peach banana apple banana apple apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html', 'title': 'N-344', 'score': 0.99763727619582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-988.html', 'title': 'N-988', 'score': 0.9968391055400966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-517.html', 'title': 'N-517', 'score': 0.9959602963480232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-392.html', 'title': 'N-392', 'score': 0.9956039253404269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-506.html', 'title': 'N-506', 'score': 0.9955562889300751}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-936.html', 'title': 'N-936', 'score': 0.9953397963080849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-134.html', 'title': 'N-134', 'score': 0.9950722269479049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-626.html', 'title': 'N-626', 'score': 0.9938508466216377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-585.html', 'title': 'N-585', 'score': 0.9923575883344925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-794.html', 'title': 'N-794', 'score': 0.9918252068929332}]
result = search.search('coconut peach banana apple banana apple apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'coconut peach banana apple banana apple apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'coconut peach banana apple banana apple apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'peach pear banana peach coconut peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html', 'title': 'N-145', 'score': 0.989477704761862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-431.html', 'title': 'N-431', 'score': 0.9873648374805097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-105.html', 'title': 'N-105', 'score': 0.9801788707655614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-279.html', 'title': 'N-279', 'score': 0.9794015196999691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9764471286916397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-970.html', 'title': 'N-970', 'score': 0.9754723771499105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-337.html', 'title': 'N-337', 'score': 0.9685044499430029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-546.html', 'title': 'N-546', 'score': 0.9681807998669087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-964.html', 'title': 'N-964', 'score': 0.9675091080328045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html', 'title': 'N-395', 'score': 0.9655282825289786}]
result = search.search('peach pear banana peach coconut peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'peach pear banana peach coconut peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'peach pear banana peach coconut peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'tomato apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016095350631103317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01173849251039794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01173717685922528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010985216997917413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010879474014584126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129116652445442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851592713703313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007840601893309988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074259064541596365}]
result = search.search('tomato apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'tomato apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'tomato apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'banana coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014717912590507634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01138486598448854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010673085992621907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009877931319644524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009484924179354858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009051986296344511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008969561317055971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007780832902138458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0075888483482094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007403386567966819}]
result = search.search('banana coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'banana coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'banana coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'pear tomato apple peach coconut pear apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html', 'title': 'N-870', 'score': 0.9971244050790321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html', 'title': 'N-609', 'score': 0.9970726498597385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-324.html', 'title': 'N-324', 'score': 0.996994961786143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-536.html', 'title': 'N-536', 'score': 0.9956198429865825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html', 'title': 'N-463', 'score': 0.9955570916433744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-286.html', 'title': 'N-286', 'score': 0.9944287771988511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-678.html', 'title': 'N-678', 'score': 0.99387099726771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-298.html', 'title': 'N-298', 'score': 0.9926967529155302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-840.html', 'title': 'N-840', 'score': 0.9924840764315805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-962.html', 'title': 'N-962', 'score': 0.992063577053925}]
result = search.search('pear tomato apple peach coconut pear apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'pear tomato apple peach coconut pear apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'pear tomato apple peach coconut pear apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'peach banana banana peach coconut tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013598434765019275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010746494249198565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01052440244132839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01017471995597895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009812833257778793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009137240667442446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008642123346759026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007624430580145511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007504864142030239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007159877367354528}]
result = search.search('peach banana banana peach coconut tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'peach banana banana peach coconut tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'peach banana banana peach coconut tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'tomato apple banana tomato pear coconut pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html', 'title': 'N-752', 'score': 0.9999352532138995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9973956421687445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html', 'title': 'N-159', 'score': 0.9965923716082979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-462.html', 'title': 'N-462', 'score': 0.9958239772478288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-542.html', 'title': 'N-542', 'score': 0.995456153874756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html', 'title': 'N-290', 'score': 0.994575610113077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9942691522013442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9924766016776246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-38.html', 'title': 'N-38', 'score': 0.9900461215341649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-768.html', 'title': 'N-768', 'score': 0.9851939336213383}]
result = search.search('tomato apple banana tomato pear coconut pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'tomato apple banana tomato pear coconut pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'tomato apple banana tomato pear coconut pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'apple banana peach coconut tomato tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999992961835997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9987120630744257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9978158565804276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9972751992112096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9971554520219191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9969887509409239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9949272973759633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9946124891058862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9942864797851001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9926055227393175}]
result = search.search('apple banana peach coconut tomato tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'apple banana peach coconut tomato tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'apple banana peach coconut tomato tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'peach apple banana coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015020908208399924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01144318740184773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010638118222899971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010138502555013546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010138455617100124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009279948354746924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00839604357342081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007657062298206072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007458868823990721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007398316719964204}]
result = search.search('peach apple banana coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'peach apple banana coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'peach apple banana coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016095350631103317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01173849251039794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01173717685922528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010985216997917413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010879474014584126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129116652445442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851592713703313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007840601893309988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074259064541596365}]
result = search.search('apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'tomato tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'tomato tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'tomato tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'banana pear banana peach banana tomato pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014526000188003861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01199952203414646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011374566525481668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010516199239239821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009967939192994907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009743771350405021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008650658111208968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007793365459547822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007476733409282537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007219617140381301}]
result = search.search('banana pear banana peach banana tomato pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'banana pear banana peach banana tomato pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'banana pear banana peach banana tomato pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'peach tomato pear peach pear banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-747.html', 'title': 'N-747', 'score': 0.998025629028374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.997719469935884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-515.html', 'title': 'N-515', 'score': 0.9971167279856292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html', 'title': 'N-357', 'score': 0.9968251778598058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.996562440670027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9964802475151552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-717.html', 'title': 'N-717', 'score': 0.9962422936362276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'title': 'N-786', 'score': 0.9961073050894469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9955183393635708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.9947017476742858}]
result = search.search('peach tomato pear peach pear banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'peach tomato pear peach pear banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'peach tomato pear peach pear banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'banana coconut apple peach tomato banana banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 0.9999843493115781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-258.html', 'title': 'N-258', 'score': 0.9971375772097583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html', 'title': 'N-718', 'score': 0.9923520672712157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-553.html', 'title': 'N-553', 'score': 0.9893530421974421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html', 'title': 'N-987', 'score': 0.9866861155492651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-293.html', 'title': 'N-293', 'score': 0.9853211512077666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.9839351612990067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html', 'title': 'N-871', 'score': 0.981740298974174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-212.html', 'title': 'N-212', 'score': 0.9814105472374383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-130.html', 'title': 'N-130', 'score': 0.980733831740723}]
result = search.search('banana coconut apple peach tomato banana banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'banana coconut apple peach tomato banana banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'banana coconut apple peach tomato banana banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'peach apple apple peach peach banana peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-365.html', 'title': 'N-365', 'score': 0.9987105600673686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html', 'title': 'N-377', 'score': 0.9984350195877364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-556.html', 'title': 'N-556', 'score': 0.9981445958821352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html', 'title': 'N-978', 'score': 0.9967428926830338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-717.html', 'title': 'N-717', 'score': 0.9965674540346873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-702.html', 'title': 'N-702', 'score': 0.9965105890779536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html', 'title': 'N-297', 'score': 0.9961420211859116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-337.html', 'title': 'N-337', 'score': 0.9961140360686367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-764.html', 'title': 'N-764', 'score': 0.9945332189957649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-846.html', 'title': 'N-846', 'score': 0.9929733190118406}]
result = search.search('peach apple apple peach peach banana peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'peach apple apple peach peach banana peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'peach apple apple peach peach banana peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'apple coconut peach banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999395191314641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.998921517252274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9980620077490978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9978835810356514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9976482473570287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9962892926678882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9955289709631839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9949772431926911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9948581986819997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9936019352659154}]
result = search.search('apple coconut peach banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'apple coconut peach banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'apple coconut peach banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'coconut banana apple apple banana coconut apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html', 'title': 'N-344', 'score': 0.9976372761958201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-988.html', 'title': 'N-988', 'score': 0.9968391055400967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-517.html', 'title': 'N-517', 'score': 0.9959602963480233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-392.html', 'title': 'N-392', 'score': 0.9956039253404269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-506.html', 'title': 'N-506', 'score': 0.9955562889300751}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-936.html', 'title': 'N-936', 'score': 0.9953397963080849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-134.html', 'title': 'N-134', 'score': 0.9950722269479048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-626.html', 'title': 'N-626', 'score': 0.9938508466216378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-585.html', 'title': 'N-585', 'score': 0.9923575883344925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-794.html', 'title': 'N-794', 'score': 0.9918252068929332}]
result = search.search('coconut banana apple apple banana coconut apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'coconut banana apple apple banana coconut apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'coconut banana apple apple banana coconut apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'coconut banana coconut tomato coconut coconut coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-864.html', 'title': 'N-864', 'score': 0.9998393696363134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-308.html', 'title': 'N-308', 'score': 0.9950672490834517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-37.html', 'title': 'N-37', 'score': 0.9911193395940603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-413.html', 'title': 'N-413', 'score': 0.9860347121813088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.9813700881615712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-405.html', 'title': 'N-405', 'score': 0.9805303896706664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-127.html', 'title': 'N-127', 'score': 0.9800094821194524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-17.html', 'title': 'N-17', 'score': 0.9787221722701944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-375.html', 'title': 'N-375', 'score': 0.9782830217480047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.9754654715887751}]
result = search.search('coconut banana coconut tomato coconut coconut coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'coconut banana coconut tomato coconut coconut coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'coconut banana coconut tomato coconut coconut coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'apple peach pear coconut pear peach banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9978885919677356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9958340135005436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9954591153379323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'title': 'N-786', 'score': 0.9937282358787972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9926616535978974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-374.html', 'title': 'N-374', 'score': 0.9924195995417906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9919703746583587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-728.html', 'title': 'N-728', 'score': 0.9919389919744652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.991773626254912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-272.html', 'title': 'N-272', 'score': 0.9916044349380306}]
result = search.search('apple peach pear coconut pear peach banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'apple peach pear coconut pear peach banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'apple peach pear coconut pear peach banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'apple pear apple coconut pear apple coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-319.html', 'title': 'N-319', 'score': 0.9998144021207487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html', 'title': 'N-344', 'score': 0.9986831751984306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html', 'title': 'N-822', 'score': 0.9968616240716933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-392.html', 'title': 'N-392', 'score': 0.9966187403009475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-651.html', 'title': 'N-651', 'score': 0.9964127889537228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-517.html', 'title': 'N-517', 'score': 0.9960280997511747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-694.html', 'title': 'N-694', 'score': 0.9952331654138973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-936.html', 'title': 'N-936', 'score': 0.9948751002807735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-128.html', 'title': 'N-128', 'score': 0.9948106170038724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-988.html', 'title': 'N-988', 'score': 0.9942968424261633}]
result = search.search('apple pear apple coconut pear apple coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'apple pear apple coconut pear apple coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'apple pear apple coconut pear apple coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'apple coconut pear coconut tomato tomato peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-356.html', 'title': 'N-356', 'score': 0.997010558413578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-715.html', 'title': 'N-715', 'score': 0.9965961044379905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html', 'title': 'N-720', 'score': 0.9962511885088874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html', 'title': 'N-818', 'score': 0.9958010167610062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-862.html', 'title': 'N-862', 'score': 0.9956591439505514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-467.html', 'title': 'N-467', 'score': 0.9950771816711395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-108.html', 'title': 'N-108', 'score': 0.9950449772935283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-787.html', 'title': 'N-787', 'score': 0.9946229886185386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-241.html', 'title': 'N-241', 'score': 0.9939082667433811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'title': 'N-686', 'score': 0.9934063953036387}]
result = search.search('apple coconut pear coconut tomato tomato peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'apple coconut pear coconut tomato tomato peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'apple coconut pear coconut tomato tomato peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'pear pear coconut apple pear peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-130.html', 'title': 'N-130', 'score': 0.9872541259052019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-462.html', 'title': 'N-462', 'score': 0.986206500686251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-542.html', 'title': 'N-542', 'score': 0.9856248364810715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-154.html', 'title': 'N-154', 'score': 0.9844302166307627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-526.html', 'title': 'N-526', 'score': 0.9751164858282234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-280.html', 'title': 'N-280', 'score': 0.9729659672849298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-304.html', 'title': 'N-304', 'score': 0.9723887401859858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html', 'title': 'N-718', 'score': 0.9659751676224088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-187.html', 'title': 'N-187', 'score': 0.965120502002744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html', 'title': 'N-159', 'score': 0.9647050998446918}]
result = search.search('pear pear coconut apple pear peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'pear pear coconut apple pear peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'pear pear coconut apple pear peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'peach coconut tomato banana apple coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 0.999998333364449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-502.html', 'title': 'N-502', 'score': 0.99612611091302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-886.html', 'title': 'N-886', 'score': 0.9952400512281249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html', 'title': 'N-691', 'score': 0.9942371636226627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-195.html', 'title': 'N-195', 'score': 0.9932393094782053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.9910616422737997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-559.html', 'title': 'N-559', 'score': 0.9904154155130431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html', 'title': 'N-961', 'score': 0.9899564507324599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html', 'title': 'N-803', 'score': 0.9896898296092526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-151.html', 'title': 'N-151', 'score': 0.9880379354174563}]
result = search.search('peach coconut tomato banana apple coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'peach coconut tomato banana apple coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'peach coconut tomato banana apple coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'apple apple pear tomato apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 0.9998848307567855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.998350822319289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html', 'title': 'N-772', 'score': 0.9976703427780413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 0.9965309886065296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9963771417003481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-249.html', 'title': 'N-249', 'score': 0.9960365790155136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html', 'title': 'N-165', 'score': 0.996013976439549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html', 'title': 'N-395', 'score': 0.9958880887815234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-260.html', 'title': 'N-260', 'score': 0.9913755723251826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html', 'title': 'N-939', 'score': 0.9913455149474277}]
result = search.search('apple apple pear tomato apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'apple apple pear tomato apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'apple apple pear tomato apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'apple peach banana banana banana peach pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html', 'title': 'N-256', 'score': 0.9970721167892145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html', 'title': 'N-848', 'score': 0.9960211098706335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'title': 'N-31', 'score': 0.9925750974337377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-351.html', 'title': 'N-351', 'score': 0.9916890240178245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-591.html', 'title': 'N-591', 'score': 0.9908738854157685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-738.html', 'title': 'N-738', 'score': 0.9901875974347953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html', 'title': 'N-917', 'score': 0.9898164711593372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'title': 'N-248', 'score': 0.9894841339856223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-553.html', 'title': 'N-553', 'score': 0.9894634507803856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-182.html', 'title': 'N-182', 'score': 0.9887383414598612}]
result = search.search('apple peach banana banana banana peach pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'apple peach banana banana banana peach pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'apple peach banana banana banana peach pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'tomato tomato apple tomato coconut coconut coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html', 'title': 'N-256', 'score': 0.9980809981355859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-537.html', 'title': 'N-537', 'score': 0.9976968038390804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html', 'title': 'N-255', 'score': 0.9950419660368146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.9949565763731758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-788.html', 'title': 'N-788', 'score': 0.9919732413800286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'title': 'N-248', 'score': 0.9914459950068659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-202.html', 'title': 'N-202', 'score': 0.9912223422575805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-413.html', 'title': 'N-413', 'score': 0.9911150950817826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-351.html', 'title': 'N-351', 'score': 0.9907585904667948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-807.html', 'title': 'N-807', 'score': 0.99073860902923}]
result = search.search('tomato tomato apple tomato coconut coconut coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'tomato tomato apple tomato coconut coconut coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'tomato tomato apple tomato coconut coconut coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'pear peach peach banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html', 'title': 'N-320', 'score': 0.9998647184636478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'title': 'N-360', 'score': 0.9997969769435322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html', 'title': 'N-873', 'score': 0.9996917756123894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9941910695764278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9934582111535624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-337.html', 'title': 'N-337', 'score': 0.9924929898036947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-970.html', 'title': 'N-970', 'score': 0.9919805782507236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9898504732504192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-546.html', 'title': 'N-546', 'score': 0.989083146586297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-903.html', 'title': 'N-903', 'score': 0.98901270752062}]
result = search.search('pear peach peach banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'pear peach peach banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'pear peach peach banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'peach banana banana banana pear apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-553.html', 'title': 'N-553', 'score': 0.9899486988931214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-258.html', 'title': 'N-258', 'score': 0.9859867115278266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html', 'title': 'N-987', 'score': 0.9797134075924301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.9791257065186315}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html', 'title': 'N-921', 'score': 0.9706515177088519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-579.html', 'title': 'N-579', 'score': 0.9689718005696355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html', 'title': 'N-52', 'score': 0.9681755872895285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html', 'title': 'N-745', 'score': 0.9675191926463961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html', 'title': 'N-848', 'score': 0.967310484169984}]
result = search.search('peach banana banana banana pear apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'peach banana banana banana pear apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'peach banana banana banana pear apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'tomato peach tomato peach tomato apple peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'title': 'N-360', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-307.html', 'title': 'N-307', 'score': 0.9999914901198582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html', 'title': 'N-255', 'score': 0.9999463444464269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html', 'title': 'N-379', 'score': 0.9999319780657018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-53.html', 'title': 'N-53', 'score': 0.9958421259993754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-643.html', 'title': 'N-643', 'score': 0.9951631407664401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9946217932166057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html', 'title': 'N-815', 'score': 0.9939525827996027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-801.html', 'title': 'N-801', 'score': 0.993674134006067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'title': 'N-458', 'score': 0.9936356099526854}]
result = search.search('tomato peach tomato peach tomato apple peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #80 checking search results for 'tomato peach tomato peach tomato apple peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #80 checking search results for 'tomato peach tomato peach tomato apple peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking search results for 'banana coconut peach tomato pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9999822061228667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.9988534612389155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html', 'title': 'N-998', 'score': 0.9986649689159565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9982912322393562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.996437054335509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-419.html', 'title': 'N-419', 'score': 0.9962411741093309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html', 'title': 'N-644', 'score': 0.9953467799017663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9952402161014384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-540.html', 'title': 'N-540', 'score': 0.9946911812404837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-558.html', 'title': 'N-558', 'score': 0.9946898489219974}]
result = search.search('banana coconut peach tomato pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'banana coconut peach tomato pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'banana coconut peach tomato pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'pear coconut peach coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 0.9997455738222784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 0.9995997019242934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-588.html', 'title': 'N-588', 'score': 0.9975121435701361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.9967862797145324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-343.html', 'title': 'N-343', 'score': 0.9964181390103305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-537.html', 'title': 'N-537', 'score': 0.9961513426197107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-250.html', 'title': 'N-250', 'score': 0.9951000723384822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-149.html', 'title': 'N-149', 'score': 0.9944460397108138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html', 'title': 'N-697', 'score': 0.9938391692540998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 0.9933787487044271}]
result = search.search('pear coconut peach coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'pear coconut peach coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'pear coconut peach coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'banana peach apple peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999395191314643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9989215172522742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9980620077490979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9978835810356514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9976482473570288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9962892926678885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9955289709631842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9949772431926912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9948581986819997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9936019352659156}]
result = search.search('banana peach apple peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'banana peach apple peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'banana peach apple peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'apple apple banana coconut peach pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html', 'title': 'N-939', 'score': 0.9904474035545832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html', 'title': 'N-772', 'score': 0.9836401147200826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html', 'title': 'N-165', 'score': 0.9822482256528547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-712.html', 'title': 'N-712', 'score': 0.9814522103054402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-896.html', 'title': 'N-896', 'score': 0.9790200237018561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-271.html', 'title': 'N-271', 'score': 0.9771938469128628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-870.html', 'title': 'N-870', 'score': 0.975600562817494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'title': 'N-183', 'score': 0.9722335315525794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-94.html', 'title': 'N-94', 'score': 0.9713954478109526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 0.9699275008579847}]
result = search.search('apple apple banana coconut peach pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'apple apple banana coconut peach pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'apple apple banana coconut peach pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'pear tomato tomato coconut coconut coconut apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html', 'title': 'N-256', 'score': 0.9980809981355859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-537.html', 'title': 'N-537', 'score': 0.9976968038390804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html', 'title': 'N-255', 'score': 0.9950419660368146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.9949565763731758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-788.html', 'title': 'N-788', 'score': 0.9919732413800285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'title': 'N-248', 'score': 0.9914459950068659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-202.html', 'title': 'N-202', 'score': 0.9912223422575807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-413.html', 'title': 'N-413', 'score': 0.9911150950817826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-351.html', 'title': 'N-351', 'score': 0.9907585904667948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-807.html', 'title': 'N-807', 'score': 0.99073860902923}]
result = search.search('pear tomato tomato coconut coconut coconut apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'pear tomato tomato coconut coconut coconut apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'pear tomato tomato coconut coconut coconut apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'banana coconut pear tomato coconut banana tomato apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-307.html', 'title': 'N-307', 'score': 0.9999976846755828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'title': 'N-248', 'score': 0.9996572993417292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'title': 'N-458', 'score': 0.9986951646134814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-453.html', 'title': 'N-453', 'score': 0.9979237715504982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-488.html', 'title': 'N-488', 'score': 0.9972250682755449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-252.html', 'title': 'N-252', 'score': 0.9969831928190231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html', 'title': 'N-256', 'score': 0.9969367440321153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-532.html', 'title': 'N-532', 'score': 0.9965236020935934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 0.9961773180235887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-89.html', 'title': 'N-89', 'score': 0.9949857178251043}]
result = search.search('banana coconut pear tomato coconut banana tomato apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'banana coconut pear tomato coconut banana tomato apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'banana coconut pear tomato coconut banana tomato apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'pear apple coconut peach apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-356.html', 'title': 'N-356', 'score': 0.9973671739527322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-715.html', 'title': 'N-715', 'score': 0.9970147582161917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html', 'title': 'N-720', 'score': 0.9961490499731357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-862.html', 'title': 'N-862', 'score': 0.9960422245555336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html', 'title': 'N-818', 'score': 0.9959684455658472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-467.html', 'title': 'N-467', 'score': 0.9955331417764565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-108.html', 'title': 'N-108', 'score': 0.9953511763056424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-787.html', 'title': 'N-787', 'score': 0.995207542574036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-241.html', 'title': 'N-241', 'score': 0.9944899421496162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'title': 'N-686', 'score': 0.9940752590830517}]
result = search.search('pear apple coconut peach apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'pear apple coconut peach apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'pear apple coconut peach apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'peach pear banana peach apple peach tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html', 'title': 'N-662', 'score': 0.9982979391294693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-524.html', 'title': 'N-524', 'score': 0.99569261602167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html', 'title': 'N-411', 'score': 0.9931565418320589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-122.html', 'title': 'N-122', 'score': 0.9922823982574257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.990317820395073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html', 'title': 'N-752', 'score': 0.9897282966500607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-266.html', 'title': 'N-266', 'score': 0.9884989378565309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-964.html', 'title': 'N-964', 'score': 0.9873050192588293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.986843295768116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-374.html', 'title': 'N-374', 'score': 0.9863053912059428}]
result = search.search('peach pear banana peach apple peach tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'peach pear banana peach apple peach tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'peach pear banana peach apple peach tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'pear coconut coconut tomato banana apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.9943155891232405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-413.html', 'title': 'N-413', 'score': 0.9902768617002009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-788.html', 'title': 'N-788', 'score': 0.988806071160524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-431.html', 'title': 'N-431', 'score': 0.988178491706162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'title': 'N-360', 'score': 0.98690712377746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-255.html', 'title': 'N-255', 'score': 0.9860881490472571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-610.html', 'title': 'N-610', 'score': 0.9856733917938864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-370.html', 'title': 'N-370', 'score': 0.9840776611852143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-564.html', 'title': 'N-564', 'score': 0.9829039153036144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-864.html', 'title': 'N-864', 'score': 0.9817904333418616}]
result = search.search('pear coconut coconut tomato banana apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'pear coconut coconut tomato banana apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'pear coconut coconut tomato banana apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'tomato apple apple pear peach coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html', 'title': 'N-165', 'score': 0.9963921054350606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 0.9958458332207719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-249.html', 'title': 'N-249', 'score': 0.9931567610474987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-773.html', 'title': 'N-773', 'score': 0.9890604861099458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html', 'title': 'N-470', 'score': 0.9860329564687668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html', 'title': 'N-720', 'score': 0.9859314502998275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-585.html', 'title': 'N-585', 'score': 0.9853105428518666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 0.9850425876903681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-306.html', 'title': 'N-306', 'score': 0.9847652080587797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html', 'title': 'N-361', 'score': 0.9847512594314494}]
result = search.search('tomato apple apple pear peach coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'tomato apple apple pear peach coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'tomato apple apple pear peach coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'apple banana coconut pear banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 0.9999744559162611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-553.html', 'title': 'N-553', 'score': 0.99393789636339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html', 'title': 'N-848', 'score': 0.9897220643904623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-53.html', 'title': 'N-53', 'score': 0.9895031034402101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-666.html', 'title': 'N-666', 'score': 0.98823396196513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-311.html', 'title': 'N-311', 'score': 0.9867518999311445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-258.html', 'title': 'N-258', 'score': 0.9856714956309096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html', 'title': 'N-917', 'score': 0.9836573743888252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-801.html', 'title': 'N-801', 'score': 0.9825537516291761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.9821383519939395}]
result = search.search('apple banana coconut pear banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'apple banana coconut pear banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'apple banana coconut pear banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'peach pear peach peach peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html', 'title': 'N-815', 'score': 0.9995520856318788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-551.html', 'title': 'N-551', 'score': 0.9977582406029571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html', 'title': 'N-917', 'score': 0.9974428201733714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-379.html', 'title': 'N-379', 'score': 0.9955959872287407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-554.html', 'title': 'N-554', 'score': 0.99473633398272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html', 'title': 'N-395', 'score': 0.994011863428002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-431.html', 'title': 'N-431', 'score': 0.9922935046817455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html', 'title': 'N-145', 'score': 0.9909014791917988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html', 'title': 'N-560', 'score': 0.9895860067134157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9887336391981898}]
result = search.search('peach pear peach peach peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'peach pear peach peach peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'peach pear peach peach peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'banana banana peach banana pear coconut banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-163.html', 'title': 'N-163', 'score': 0.9949908327217156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 0.993933792700405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-286.html', 'title': 'N-286', 'score': 0.9896944114155438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-797.html', 'title': 'N-797', 'score': 0.9886760210777369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-926.html', 'title': 'N-926', 'score': 0.9819667320880416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-553.html', 'title': 'N-553', 'score': 0.9817912684962145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.9794387111994585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html', 'title': 'N-745', 'score': 0.9724980998816386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html', 'title': 'N-64', 'score': 0.9683905643125292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-694.html', 'title': 'N-694', 'score': 0.9656168911117031}]
result = search.search('banana banana peach banana pear coconut banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'banana banana peach banana pear coconut banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'banana banana peach banana pear coconut banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'peach pear coconut tomato pear banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-747.html', 'title': 'N-747', 'score': 0.998025629028374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.997719469935884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-515.html', 'title': 'N-515', 'score': 0.9971167279856292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html', 'title': 'N-357', 'score': 0.9968251778598057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9965624406700269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9964802475151552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-717.html', 'title': 'N-717', 'score': 0.9962422936362276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'title': 'N-786', 'score': 0.9961073050894469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9955183393635708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.9947017476742858}]
result = search.search('peach pear coconut tomato pear banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'peach pear coconut tomato pear banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'peach pear coconut tomato pear banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'tomato pear peach banana coconut coconut coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 0.9955534113988204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-413.html', 'title': 'N-413', 'score': 0.9852497822196631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'title': 'N-161', 'score': 0.9838898705997277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 0.9815039874263439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-343.html', 'title': 'N-343', 'score': 0.9688225303821207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-195.html', 'title': 'N-195', 'score': 0.9608349262141341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-502.html', 'title': 'N-502', 'score': 0.9606848713246627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-984.html', 'title': 'N-984', 'score': 0.9605501722763723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-564.html', 'title': 'N-564', 'score': 0.9591380617705902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-552.html', 'title': 'N-552', 'score': 0.9583820129987413}]
result = search.search('tomato pear peach banana coconut coconut coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'tomato pear peach banana coconut coconut coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'tomato pear peach banana coconut coconut coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'banana coconut pear pear pear tomato tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-462.html', 'title': 'N-462', 'score': 0.9999946105458158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html', 'title': 'N-297', 'score': 0.999971746138693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-464.html', 'title': 'N-464', 'score': 0.999966532814308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html', 'title': 'N-752', 'score': 0.9999463668658266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html', 'title': 'N-290', 'score': 0.9980164083969506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html', 'title': 'N-357', 'score': 0.99779355381562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html', 'title': 'N-159', 'score': 0.9976500200920828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9971905307777618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-542.html', 'title': 'N-542', 'score': 0.9959696099896382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9950525049658223}]
result = search.search('banana coconut pear pear pear tomato tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'banana coconut pear pear pear tomato tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'banana coconut pear pear pear tomato tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'peach coconut banana peach pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9999822061228667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.9988534612389155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html', 'title': 'N-998', 'score': 0.9986649689159565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9982912322393562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.996437054335509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-419.html', 'title': 'N-419', 'score': 0.9962411741093308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html', 'title': 'N-644', 'score': 0.9953467799017663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9952402161014385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-540.html', 'title': 'N-540', 'score': 0.9946911812404838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-558.html', 'title': 'N-558', 'score': 0.9946898489219974}]
result = search.search('peach coconut banana peach pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'peach coconut banana peach pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'peach coconut banana peach pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
