
import testingtools
import crawler
import searchdata
import search
output = open('fruits-search-failed.txt', 'w')
success_output = open('fruits-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')
#Test #0 checking search results for 'peach apple apple apple banana peach peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020647172563080823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01569787289336958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013067535057474813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010025968700866314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008194759266099565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008093039118284323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00784387680235508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007636862626462582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007323665269907148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006711258414350045}]
result = search.search('peach apple apple apple banana peach peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'peach apple apple apple banana peach peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'peach apple apple apple banana peach peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'banana peach tomato tomato pear peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9999853329300575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'title': 'N-172', 'score': 0.9974734177292797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html', 'title': 'N-178', 'score': 0.9945145933787903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.9934491429308954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-86.html', 'title': 'N-86', 'score': 0.9916081919533283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'title': 'N-462', 'score': 0.9911487080204266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-813.html', 'title': 'N-813', 'score': 0.989949965900219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html', 'title': 'N-831', 'score': 0.9898165337469325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html', 'title': 'N-28', 'score': 0.9889050669410079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.9877221259376553}]
result = search.search('banana peach tomato tomato pear peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'banana peach tomato tomato pear peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'banana peach tomato tomato pear peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'pear coconut pear apple banana banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-535.html', 'title': 'N-535', 'score': 0.99869458815025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-351.html', 'title': 'N-351', 'score': 0.9983322353885279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-966.html', 'title': 'N-966', 'score': 0.9977957781913595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.9958404373995062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html', 'title': 'N-690', 'score': 0.9955355469867356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-802.html', 'title': 'N-802', 'score': 0.9937429636095115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html', 'title': 'N-321', 'score': 0.9928627486880888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html', 'title': 'N-847', 'score': 0.9921698792806023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-816.html', 'title': 'N-816', 'score': 0.991795814339078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-595.html', 'title': 'N-595', 'score': 0.9916042560688058}]
result = search.search('pear coconut pear apple banana banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'pear coconut pear apple banana banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'pear coconut pear apple banana banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'tomato apple banana banana tomato banana coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9981715317171782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html', 'title': 'N-915', 'score': 0.9975885091380268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-408.html', 'title': 'N-408', 'score': 0.9974167641123508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-694.html', 'title': 'N-694', 'score': 0.9970957007216915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-545.html', 'title': 'N-545', 'score': 0.9970003863259786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-799.html', 'title': 'N-799', 'score': 0.99683771664375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 0.9963300890325587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-323.html', 'title': 'N-323', 'score': 0.9957042150293863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 0.9956606854646675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9955052414336948}]
result = search.search('tomato apple banana banana tomato banana coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'tomato apple banana banana tomato banana coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'tomato apple banana banana tomato banana coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'pear coconut coconut apple tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9995561228928082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9988892828640841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.998544798942508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9984716365394537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9982082457219194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9975431987597079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 0.9974897348595452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html', 'title': 'N-92', 'score': 0.9965178683287363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9964826978198248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html', 'title': 'N-296', 'score': 0.9957016562577593}]
result = search.search('pear coconut coconut apple tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'pear coconut coconut apple tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'pear coconut coconut apple tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'peach banana pear pear peach coconut peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017391487725818264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014990945501887459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012203563778876252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009980165183898085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008712554457579194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007969148954505288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007735074893550356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007448374813900931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007185442871074211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006559109269214164}]
result = search.search('peach banana pear pear peach coconut peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'peach banana pear pear peach coconut peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'peach banana pear pear peach coconut peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'peach banana pear pear peach coconut peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html', 'title': 'N-142', 'score': 0.997821573482241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-737.html', 'title': 'N-737', 'score': 0.9977776750198906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html', 'title': 'N-600', 'score': 0.9965700198063462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-636.html', 'title': 'N-636', 'score': 0.9958427661229757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-713.html', 'title': 'N-713', 'score': 0.9956789219225559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html', 'title': 'N-116', 'score': 0.9955362770469948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-361.html', 'title': 'N-361', 'score': 0.9951005082379117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-340.html', 'title': 'N-340', 'score': 0.9944460873357251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-2.html', 'title': 'N-2', 'score': 0.9939229409026595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html', 'title': 'N-827', 'score': 0.993216165104886}]
result = search.search('peach banana pear pear peach coconut peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'peach banana pear pear peach coconut peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'peach banana pear pear peach coconut peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'pear coconut peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01918355710620264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014707801862769822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012362877989198098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010294233701147211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008481052398593182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007757104524667243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007639221750984814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007628748088830882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006990022859508908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006531148560900739}]
result = search.search('pear coconut peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'pear coconut peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'pear coconut peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'apple peach apple banana peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020254442531652775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015559908906257733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012261605992702861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009701159241713619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007940466217650422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007916942547577518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007554781702008932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007303255206920801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007270714893669399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00655777346281904}]
result = search.search('apple peach apple banana peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'apple peach apple banana peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'apple peach apple banana peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'tomato banana banana peach coconut tomato peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017913475153358914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01462437330959416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01246577220257667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010079970487356963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008869989914435389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00789154814628027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007807148121135383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007444797655620679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006671540962579327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006498001220874918}]
result = search.search('tomato banana banana peach coconut tomato peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'tomato banana banana peach coconut tomato peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'tomato banana banana peach coconut tomato peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'coconut tomato apple peach peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01978954621403834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015247037696952558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012496369726013687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009542940530548428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008416042271308075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007699069561940119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007648288286441874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007298075918007056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006748423678298874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006606051144350537}]
result = search.search('coconut tomato apple peach peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'coconut tomato apple peach peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'coconut tomato apple peach peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'tomato peach tomato coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('tomato peach tomato coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'tomato peach tomato coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'tomato peach tomato coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'coconut apple banana pear peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 0.9972129876967869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-843.html', 'title': 'N-843', 'score': 0.9953035305484534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html', 'title': 'N-313', 'score': 0.9947717205018723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html', 'title': 'N-578', 'score': 0.9939714310517246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-801.html', 'title': 'N-801', 'score': 0.9938180823861388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html', 'title': 'N-371', 'score': 0.9935689301516948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html', 'title': 'N-558', 'score': 0.9932007882282237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-637.html', 'title': 'N-637', 'score': 0.993141120733607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-599.html', 'title': 'N-599', 'score': 0.9927184689122271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-302.html', 'title': 'N-302', 'score': 0.9923366710923358}]
result = search.search('coconut apple banana pear peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'coconut apple banana pear peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'coconut apple banana pear peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'peach coconut tomato banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019929098689925193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015548139406075231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012338295072619063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00943260311695852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008392737953394635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007725627337417748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0076283953847429194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00716139339644426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0071043325405439435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006616463130220536}]
result = search.search('peach coconut tomato banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'peach coconut tomato banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'peach coconut tomato banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'banana apple peach pear banana peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01959475003283244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014388954247912615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013087623131741166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010352142076000161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008279322271415701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008025493588901944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007845293343415733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00777540897397492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007170094075166142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0064850986831077794}]
result = search.search('banana apple peach pear banana peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'banana apple peach pear banana peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'banana apple peach pear banana peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'coconut coconut peach tomato pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.999999773530811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999911122299763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999911122299763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9984408235572477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9978838759671222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9968537839795928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-935.html', 'title': 'N-935', 'score': 0.9967801905024776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9961522319260571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'title': 'N-683', 'score': 0.9961290706538883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9960927424862465}]
result = search.search('coconut coconut peach tomato pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'coconut coconut peach tomato pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'coconut coconut peach tomato pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'peach pear coconut peach banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01901016188267685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014011112189369271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011556524892146454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008977354161236243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007904505551336897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007271874448092428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007138606157059676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006849202978281342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006504346176500244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006195532872828101}]
result = search.search('peach pear coconut peach banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'peach pear coconut peach banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'peach pear coconut peach banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'coconut apple peach banana coconut apple pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999953983127283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999953983127283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9964764345700029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9930880406915602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html', 'title': 'N-910', 'score': 0.9928309856348724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9926336675123993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-35.html', 'title': 'N-35', 'score': 0.9921078446518454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9915949297148382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'title': 'N-615', 'score': 0.9909856352407156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html', 'title': 'N-152', 'score': 0.9909075437845546}]
result = search.search('coconut apple peach banana coconut apple pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'coconut apple peach banana coconut apple pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'coconut apple peach banana coconut apple pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'pear coconut pear pear coconut pear pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'title': 'N-90', 'score': 0.9983484058219801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9978358027047833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9977736585271292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-776.html', 'title': 'N-776', 'score': 0.9973596790265356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html', 'title': 'N-37', 'score': 0.9970685132975434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-323.html', 'title': 'N-323', 'score': 0.9970143650551471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html', 'title': 'N-775', 'score': 0.9968639080405374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-131.html', 'title': 'N-131', 'score': 0.992747924471673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-408.html', 'title': 'N-408', 'score': 0.9908018718913562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html', 'title': 'N-915', 'score': 0.9907807635274343}]
result = search.search('pear coconut pear pear coconut pear pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'pear coconut pear pear coconut pear pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'pear coconut pear pear coconut pear pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'tomato coconut tomato tomato pear banana peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019284473124450262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014796803758834463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01246217294661018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009566521341022226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008369686760672358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007703834427025131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007651545798430762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007282555433872137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007024607563132384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006542597113201885}]
result = search.search('tomato coconut tomato tomato pear banana peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'tomato coconut tomato tomato pear banana peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'tomato coconut tomato tomato pear banana peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'apple coconut coconut pear peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9995561228928082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9988892828640841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.998544798942508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9984716365394537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9982082457219194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9975431987597079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 0.9974897348595452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html', 'title': 'N-92', 'score': 0.9965178683287363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9964826978198248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html', 'title': 'N-296', 'score': 0.9957016562577593}]
result = search.search('apple coconut coconut pear peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'apple coconut coconut pear peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'apple coconut coconut pear peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'tomato pear peach banana coconut pear peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017581728629207403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015043837419520098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011662205155972435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008974324150146259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008206805093963833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007482829107684738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007245395523056323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007031030460015036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006863471111029205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006411801440971625}]
result = search.search('tomato pear peach banana coconut pear peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'tomato pear peach banana coconut pear peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'tomato pear peach banana coconut pear peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'tomato peach peach coconut pear apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01979057649735695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014143624202996846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01300702813898703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009315940448508262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008043243515239305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007736082297189311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00739601329995945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006941815023295276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00645587052339457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0064009295730342655}]
result = search.search('tomato peach peach coconut pear apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'tomato peach peach coconut pear apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'tomato peach peach coconut pear apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'peach coconut pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01918355710620264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014707801862769822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012362877989198098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010294233701147211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008481052398593182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007757104524667244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007639221750984814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007628748088830882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006990022859508907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006531148560900739}]
result = search.search('peach coconut pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'peach coconut pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'peach coconut pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'tomato peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010417067314545846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008507193563889777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008227390811338423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00787315571136734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007248519972589282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006744943947177922}]
result = search.search('tomato peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'tomato peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'tomato peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'tomato coconut peach peach pear peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018722805076059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01367632843272022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011306918829004545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009870750550526242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008054382500841097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007321538425172306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007203937519586932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007151671544124565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00639495890182212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006125572658115138}]
result = search.search('tomato coconut peach peach pear peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'tomato coconut peach peach pear peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'tomato coconut peach peach pear peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'banana apple apple peach apple tomato pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html', 'title': 'N-178', 'score': 0.9989765714651152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'title': 'N-615', 'score': 0.9953361648931306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'title': 'N-172', 'score': 0.99121576627017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-330.html', 'title': 'N-330', 'score': 0.991162619705869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-269.html', 'title': 'N-269', 'score': 0.9897698670730292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-583.html', 'title': 'N-583', 'score': 0.989259405417693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-215.html', 'title': 'N-215', 'score': 0.9887360168331694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-305.html', 'title': 'N-305', 'score': 0.9876069853977874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-602.html', 'title': 'N-602', 'score': 0.987247911093254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-795.html', 'title': 'N-795', 'score': 0.9866078078376987}]
result = search.search('banana apple apple peach apple tomato pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'banana apple apple peach apple tomato pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'banana apple apple peach apple tomato pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'tomato apple banana coconut peach tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01977398413708179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015234252461753129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012477270016542323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009529137047091548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008410010433071508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007686953303701851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007640450330258488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00728941866833947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006736409395838089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006599943708842697}]
result = search.search('tomato apple banana coconut peach tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'tomato apple banana coconut peach tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'tomato apple banana coconut peach tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'peach apple peach coconut apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019732245521999654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01525399466941783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011765675229150402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010121217480682652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008712458762487304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007926061057159874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007846633843142716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007386550703836505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006830145267354158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00651015366153017}]
result = search.search('peach apple peach coconut apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'peach apple peach coconut apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'peach apple peach coconut apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'peach coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('peach coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'peach coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'peach coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'banana peach apple tomato coconut coconut apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999953983127282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999953983127282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9964764345700029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9930880406915602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html', 'title': 'N-910', 'score': 0.9928309856348724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9926336675123993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-35.html', 'title': 'N-35', 'score': 0.9921078446518455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9915949297148383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'title': 'N-615', 'score': 0.9909856352407156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html', 'title': 'N-152', 'score': 0.9909075437845545}]
result = search.search('banana peach apple tomato coconut coconut apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'banana peach apple tomato coconut coconut apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'banana peach apple tomato coconut coconut apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'peach banana pear tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020240572628715744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01468741042792802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012680615206329153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009570649576755179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008411920001518677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0077665785882033555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007644345831347453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007422301836681493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006960072027470448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006529354806792243}]
result = search.search('peach banana pear tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'peach banana pear tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'peach banana pear tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'peach tomato pear tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01735781777758059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach tomato pear tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'peach tomato pear tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'peach tomato pear tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'apple banana peach peach tomato coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01883763252137762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014480407814594656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01150794551275182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008820793553313382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008035707250876987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007204223757824194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007075525870957989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00682513196788514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0062501695551812845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006143641462834273}]
result = search.search('apple banana peach peach tomato coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'apple banana peach peach tomato coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'apple banana peach peach tomato coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'pear pear pear pear peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-29.html', 'title': 'N-29', 'score': 0.9998386204425965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-704.html', 'title': 'N-704', 'score': 0.9989271369412026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-57.html', 'title': 'N-57', 'score': 0.9984445698134248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-792.html', 'title': 'N-792', 'score': 0.9978457503628081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html', 'title': 'N-849', 'score': 0.9974444664902768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'title': 'N-40', 'score': 0.9971598286797643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html', 'title': 'N-941', 'score': 0.9961796752942721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html', 'title': 'N-995', 'score': 0.9961796752942721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-549.html', 'title': 'N-549', 'score': 0.996025766897781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-490.html', 'title': 'N-490', 'score': 0.9953797059337044}]
result = search.search('pear pear pear pear peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'pear pear pear pear peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'pear pear pear pear peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'coconut peach banana pear apple peach banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.9952859013184676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9938605200762611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9896657843684479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html', 'title': 'N-575', 'score': 0.9894543701511022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-212.html', 'title': 'N-212', 'score': 0.9889573761895871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html', 'title': 'N-378', 'score': 0.9884812376474816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-79.html', 'title': 'N-79', 'score': 0.9880879108811514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html', 'title': 'N-144', 'score': 0.9873967756879893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html', 'title': 'N-485', 'score': 0.9872420850236195}]
result = search.search('coconut peach banana pear apple peach banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'coconut peach banana pear apple peach banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'coconut peach banana pear apple peach banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'coconut peach tomato banana banana tomato peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018364788090959743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015187725661250403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011901989307209735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009920996368936475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008678252706375207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007875602881938878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007640951522420394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00736487412820321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007103550903955413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006505585398146433}]
result = search.search('coconut peach tomato banana banana tomato peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'coconut peach tomato banana banana tomato peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'coconut peach tomato banana banana tomato peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'apple tomato banana tomato banana banana banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html', 'title': 'N-944', 'score': 0.9999856294994323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html', 'title': 'N-446', 'score': 0.9999690219878209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-435.html', 'title': 'N-435', 'score': 0.9970556029659404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html', 'title': 'N-833', 'score': 0.9965188105831618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-137.html', 'title': 'N-137', 'score': 0.9952908673347163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 0.9946176018624566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'title': 'N-90', 'score': 0.9944428412397259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-646.html', 'title': 'N-646', 'score': 0.9943894754632953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-638.html', 'title': 'N-638', 'score': 0.992684064897545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html', 'title': 'N-915', 'score': 0.9921603348183791}]
result = search.search('apple tomato banana tomato banana banana banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'apple tomato banana tomato banana banana banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'apple tomato banana tomato banana banana banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'banana peach pear pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018000894966393018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015611354217421892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012699096075449497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009229732105908585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008485949581633007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007854623373865277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007612599566788923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007339658672375964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0072481617760519566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00665710072793501}]
result = search.search('banana peach pear pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'banana peach pear pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'banana peach pear pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'peach tomato peach tomato coconut apple banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019761564285869494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01522406129596556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01246217294661018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009518219956279302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008405187277773531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0076773790228282105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007634223712235857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0072825554338721375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00672692667274372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006595083839057599}]
result = search.search('peach tomato peach tomato coconut apple banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'peach tomato peach tomato coconut apple banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'peach tomato peach tomato coconut apple banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'peach pear peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01917851330974262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014720462919386786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012822878586848604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00987180736666412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008482622488578005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007738243476914323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007694959288013002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0076217638801188295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006617085377757684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006523509573146744}]
result = search.search('peach pear peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'peach pear peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'peach pear peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01735781777758059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'peach coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('peach coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'peach coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'peach coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'peach banana tomato peach banana apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01806292659533384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014569619211797774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013037161976615681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010069324136991827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00886931190049758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007859393497957423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007850324347093702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007618823624724462}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006570316158993565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006544664767164527}]
result = search.search('peach banana tomato peach banana apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'peach banana tomato peach banana apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'peach banana tomato peach banana apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'coconut coconut coconut tomato apple peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-867.html', 'title': 'N-867', 'score': 0.9999932781949101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-507.html', 'title': 'N-507', 'score': 0.9992793679507403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-755.html', 'title': 'N-755', 'score': 0.999042175539766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-531.html', 'title': 'N-531', 'score': 0.9987184270614808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-855.html', 'title': 'N-855', 'score': 0.998557421606569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-551.html', 'title': 'N-551', 'score': 0.9984594892428973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html', 'title': 'N-30', 'score': 0.9983798572687876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-858.html', 'title': 'N-858', 'score': 0.9981173188822856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-304.html', 'title': 'N-304', 'score': 0.9973423975497047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html', 'title': 'N-963', 'score': 0.9971856747961118}]
result = search.search('coconut coconut coconut tomato apple peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'coconut coconut coconut tomato apple peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'coconut coconut coconut tomato apple peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'banana pear banana peach pear apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01667101085802414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014891844454375422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013087623131741166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009916215200039599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008871145936900353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00797578910592114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007845293343415733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007614307065600858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0068144823773983515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006609279296264199}]
result = search.search('banana pear banana peach pear apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'banana pear banana peach pear apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'banana pear banana peach pear apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'tomato banana peach peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02088750552494393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015596439687478774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012563264399504663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00936773293788988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008368357680629466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007749427617691167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007579919019260437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007261603590792351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007012290726965116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006621079711098909}]
result = search.search('tomato banana peach peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'tomato banana peach peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'tomato banana peach peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'tomato coconut peach pear banana banana pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016676753915358732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015186825598339412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01254896145581991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01021859044692909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008871167159582888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008239072806242212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007918811949842385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007487789600351893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0074264005686414235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006637032181786938}]
result = search.search('tomato coconut peach pear banana banana pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'tomato coconut peach pear banana banana pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'tomato coconut peach pear banana banana pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking search results for 'peach apple peach banana coconut apple banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01899041471380101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015318544829223613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012548961455819907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010373502307068771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008592889958264358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008235386911110162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007918811949842385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007561161165669869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007291481053787892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006619042320466238}]
result = search.search('peach apple peach banana coconut apple banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #52 checking search results for 'peach apple peach banana coconut apple banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #52 checking search results for 'peach apple peach banana coconut apple banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking search results for 'coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #53 checking search results for 'coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #53 checking search results for 'coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking search results for 'peach banana peach tomato peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019263232561998363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014971025362353865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011319940651870376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008768567457716488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00795541834702167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007201808020460346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007151297769155847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006725902760355549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0065817568367193425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006288441263830484}]
result = search.search('peach banana peach tomato peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #54 checking search results for 'peach banana peach tomato peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #54 checking search results for 'peach banana peach tomato peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking search results for 'peach banana peach tomato peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html', 'title': 'N-31', 'score': 0.9999764120760435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-931.html', 'title': 'N-931', 'score': 0.9999589495904073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.999924885974288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html', 'title': 'N-59', 'score': 0.9938167991652156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html', 'title': 'N-853', 'score': 0.9932205095217291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-990.html', 'title': 'N-990', 'score': 0.9912732995057555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html', 'title': 'N-227', 'score': 0.9910586659482239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'title': 'N-266', 'score': 0.9894737707765816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html', 'title': 'N-934', 'score': 0.9888911408520543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html', 'title': 'N-481', 'score': 0.9886222122273766}]
result = search.search('peach banana peach tomato peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #55 checking search results for 'peach banana peach tomato peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #55 checking search results for 'peach banana peach tomato peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking search results for 'peach coconut tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271725}]
result = search.search('peach coconut tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #56 checking search results for 'peach coconut tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #56 checking search results for 'peach coconut tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking search results for 'peach banana banana pear banana peach apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.9952859013184675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.993860520076261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9896657843684479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html', 'title': 'N-575', 'score': 0.9894543701511022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-212.html', 'title': 'N-212', 'score': 0.9889573761895871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html', 'title': 'N-378', 'score': 0.9884812376474816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-79.html', 'title': 'N-79', 'score': 0.9880879108811514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html', 'title': 'N-144', 'score': 0.9873967756879893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html', 'title': 'N-485', 'score': 0.9872420850236195}]
result = search.search('peach banana banana pear banana peach apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #57 checking search results for 'peach banana banana pear banana peach apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #57 checking search results for 'peach banana banana pear banana peach apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking search results for 'peach banana coconut peach peach peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9947328980069812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html', 'title': 'N-537', 'score': 0.9889094665331017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'title': 'N-462', 'score': 0.9840129158786876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html', 'title': 'N-853', 'score': 0.9771998525524453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html', 'title': 'N-227', 'score': 0.9665962222105103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'title': 'N-172', 'score': 0.9655578815195963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html', 'title': 'N-831', 'score': 0.9557628127149446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-82.html', 'title': 'N-82', 'score': 0.9539032889328928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-931.html', 'title': 'N-931', 'score': 0.9526594485236441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-793.html', 'title': 'N-793', 'score': 0.9525612525026692}]
result = search.search('peach banana coconut peach peach peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #58 checking search results for 'peach banana coconut peach peach peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #58 checking search results for 'peach banana coconut peach peach peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking search results for 'coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #59 checking search results for 'coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #59 checking search results for 'coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking search results for 'banana peach apple tomato peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01990026712213297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01516233961797169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012656863112068272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009542498515062645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008383757869645276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007702330429590654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007598771807920936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00740614694983707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006613299748389652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006590609935960895}]
result = search.search('banana peach apple tomato peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #60 checking search results for 'banana peach apple tomato peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #60 checking search results for 'banana peach apple tomato peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking search results for 'peach tomato tomato pear banana apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9999980650161843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9989400211212545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.9986532265478112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.997738235134129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 0.9970922893653977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9967380196032567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9967137961192948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9962169438919931}]
result = search.search('peach tomato tomato pear banana apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #61 checking search results for 'peach tomato tomato pear banana apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #61 checking search results for 'peach tomato tomato pear banana apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking search results for 'pear peach peach apple tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01917037365901352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014679785631854275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012793033780686202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00984795586775382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00847028456044176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007726784366646493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007677049536561884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007596002957802541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006590234824301288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006510009359438739}]
result = search.search('pear peach peach apple tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #62 checking search results for 'pear peach peach apple tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #62 checking search results for 'pear peach peach apple tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking search results for 'peach pear coconut peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018786828717849303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013783321423165922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011412985101970379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009920153848107504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008101724779829431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0073575844230964185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007250932072479207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00721334517736459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006454760182398718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006168604887954666}]
result = search.search('peach pear coconut peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #63 checking search results for 'peach pear coconut peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #63 checking search results for 'peach pear coconut peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking search results for 'coconut pear banana coconut peach banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019578172436756153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014084156649550917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013118649350412554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009937372561297168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008288754548782062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007843811437306829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007785015370139531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0073511456575745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007117270779214914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006465379241384935}]
result = search.search('coconut pear banana coconut peach banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #64 checking search results for 'coconut pear banana coconut peach banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #64 checking search results for 'coconut pear banana coconut peach banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking search results for 'peach tomato banana apple peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01990026712213297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01516233961797169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012656863112068272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009542498515062645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008383757869645276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007702330429590654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007598771807920936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00740614694983707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006613299748389652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006590609935960895}]
result = search.search('peach tomato banana apple peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #65 checking search results for 'peach tomato banana apple peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #65 checking search results for 'peach tomato banana apple peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking search results for 'pear peach peach coconut tomato tomato apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019163425695010287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014871470176361895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012596813108105518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009637915835248546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008377747189149527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00773642710350506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007670652676389621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0073891613634160655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00684185862334913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006565714839657764}]
result = search.search('pear peach peach coconut tomato tomato apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #66 checking search results for 'pear peach peach coconut tomato tomato apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #66 checking search results for 'pear peach peach coconut tomato tomato apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking search results for 'peach apple peach pear tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01665971652126837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015322198016212773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012935541309322417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009612123403793546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873889690832994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007819344985478337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007762567747130899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0075518213828985525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006665726585440125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006634221313210295}]
result = search.search('peach apple peach pear tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #67 checking search results for 'peach apple peach pear tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #67 checking search results for 'peach apple peach pear tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking search results for 'banana peach pear pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018000894966393018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015611354217421892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012699096075449497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009229732105908585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008485949581633007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007854623373865277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007612599566788923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007339658672375964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0072481617760519566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00665710072793501}]
result = search.search('banana peach pear pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #68 checking search results for 'banana peach pear pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #68 checking search results for 'banana peach pear pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking search results for 'pear pear pear apple tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html', 'title': 'N-833', 'score': 0.9999387037593074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html', 'title': 'N-811', 'score': 0.9998343948353516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'title': 'N-406', 'score': 0.9997314860627989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-857.html', 'title': 'N-857', 'score': 0.9985913586561219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html', 'title': 'N-72', 'score': 0.9973549911672658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.9965754422583784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html', 'title': 'N-37', 'score': 0.9949792167853136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html', 'title': 'N-394', 'score': 0.9937438283214642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9925039096730666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-580.html', 'title': 'N-580', 'score': 0.9923232269113246}]
result = search.search('pear pear pear apple tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #69 checking search results for 'pear pear pear apple tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #69 checking search results for 'pear pear pear apple tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking search results for 'banana banana peach tomato apple pear peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01789524359584542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.013939176529031969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012904704531775961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010105674565088584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008606575735946838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007818580473401983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0077601673431134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007606137752193702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006623837178897532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006394063481214497}]
result = search.search('banana banana peach tomato apple pear peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #70 checking search results for 'banana banana peach tomato apple pear peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #70 checking search results for 'banana banana peach tomato apple pear peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking search results for 'pear tomato banana coconut pear apple banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-535.html', 'title': 'N-535', 'score': 0.9986384044047792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-351.html', 'title': 'N-351', 'score': 0.9982442918139148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-966.html', 'title': 'N-966', 'score': 0.9977420780027837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.9957953635026456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html', 'title': 'N-690', 'score': 0.995363991314049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-802.html', 'title': 'N-802', 'score': 0.9935044573540738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html', 'title': 'N-321', 'score': 0.9926970123994766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-847.html', 'title': 'N-847', 'score': 0.9919381938372916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-816.html', 'title': 'N-816', 'score': 0.9914672253301744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-595.html', 'title': 'N-595', 'score': 0.9913411729795268}]
result = search.search('pear tomato banana coconut pear apple banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #71 checking search results for 'pear tomato banana coconut pear apple banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #71 checking search results for 'pear tomato banana coconut pear apple banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking search results for 'banana peach coconut pear coconut pear tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-295.html', 'title': 'N-295', 'score': 0.9973644984497038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9963464256805502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-102.html', 'title': 'N-102', 'score': 0.9941357138588123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.9939993070740365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-777.html', 'title': 'N-777', 'score': 0.9931314153014861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-750.html', 'title': 'N-750', 'score': 0.9929636797115595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'title': 'N-406', 'score': 0.9925489799677634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-657.html', 'title': 'N-657', 'score': 0.9923423262121669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'title': 'N-13', 'score': 0.9916951571011264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-35.html', 'title': 'N-35', 'score': 0.9903856548958909}]
result = search.search('banana peach coconut pear coconut pear tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #72 checking search results for 'banana peach coconut pear coconut pear tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #72 checking search results for 'banana peach coconut pear coconut pear tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking search results for 'peach apple peach apple pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-996.html', 'title': 'N-996', 'score': 0.9999797412847515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-749.html', 'title': 'N-749', 'score': 0.9987937700136872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html', 'title': 'N-566', 'score': 0.9980259541604632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-343.html', 'title': 'N-343', 'score': 0.9978306144318222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-322.html', 'title': 'N-322', 'score': 0.9975162817968097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-333.html', 'title': 'N-333', 'score': 0.9974046760673101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-305.html', 'title': 'N-305', 'score': 0.9970355724737235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html', 'title': 'N-227', 'score': 0.9963789925131378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-840.html', 'title': 'N-840', 'score': 0.9963546466861648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-2.html', 'title': 'N-2', 'score': 0.995534108568162}]
result = search.search('peach apple peach apple pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #73 checking search results for 'peach apple peach apple pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #73 checking search results for 'peach apple peach apple pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking search results for 'peach peach peach tomato peach coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html', 'title': 'N-537', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html', 'title': 'N-161', 'score': 0.9998146437571263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-631.html', 'title': 'N-631', 'score': 0.999082939107518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-27.html', 'title': 'N-27', 'score': 0.9964686326109332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html', 'title': 'N-259', 'score': 0.9962250660980166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-441.html', 'title': 'N-441', 'score': 0.9962250660980166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9958485658296418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html', 'title': 'N-853', 'score': 0.9949717491029668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-864.html', 'title': 'N-864', 'score': 0.992232099607561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-484.html', 'title': 'N-484', 'score': 0.9916696572407998}]
result = search.search('peach peach peach tomato peach coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #74 checking search results for 'peach peach peach tomato peach coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #74 checking search results for 'peach peach peach tomato peach coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking search results for 'banana peach coconut banana apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-638.html', 'title': 'N-638', 'score': 0.9924030881920997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 0.9915452048198747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html', 'title': 'N-313', 'score': 0.9895675646995399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'title': 'N-90', 'score': 0.9892366083352107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 0.9886099876243117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-212.html', 'title': 'N-212', 'score': 0.9883997724545991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html', 'title': 'N-915', 'score': 0.9856337444346667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html', 'title': 'N-240', 'score': 0.9854068336275925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.9851113043275028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-535.html', 'title': 'N-535', 'score': 0.9830643626318121}]
result = search.search('banana peach coconut banana apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #75 checking search results for 'banana peach coconut banana apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #75 checking search results for 'banana peach coconut banana apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking search results for 'pear coconut pear pear banana tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-704.html', 'title': 'N-704', 'score': 0.99837825388474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html', 'title': 'N-934', 'score': 0.9969644011090796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html', 'title': 'N-481', 'score': 0.9967397706382043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html', 'title': 'N-849', 'score': 0.9964609223078084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'title': 'N-40', 'score': 0.9961065067643657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'title': 'N-266', 'score': 0.9960370532425887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-733.html', 'title': 'N-733', 'score': 0.9941164429718286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-767.html', 'title': 'N-767', 'score': 0.9924092803401082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html', 'title': 'N-457', 'score': 0.9921380393524454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html', 'title': 'N-430', 'score': 0.991454716819943}]
result = search.search('pear coconut pear pear banana tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #76 checking search results for 'pear coconut pear pear banana tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #76 checking search results for 'pear coconut pear pear banana tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking search results for 'peach peach pear apple tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-419.html', 'title': 'N-419', 'score': 0.9999275623227509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'title': 'N-462', 'score': 0.9997704628920938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'title': 'N-877', 'score': 0.999741473771283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html', 'title': 'N-901', 'score': 0.9982560862445686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html', 'title': 'N-346', 'score': 0.9970290020757706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html', 'title': 'N-504', 'score': 0.9968892721858443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.995083434842722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.9944162647931679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-87.html', 'title': 'N-87', 'score': 0.9939283368364088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9935222752554088}]
result = search.search('peach peach pear apple tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #77 checking search results for 'peach peach pear apple tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #77 checking search results for 'peach peach pear apple tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking search results for 'peach apple pear apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9999336571960098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9993319458888701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9991906331659415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9990837797980069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'title': 'N-781', 'score': 0.9988688937201871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.997387249229536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 0.9972249829181133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'title': 'N-74', 'score': 0.9969763548427109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 0.9967850676249099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-663.html', 'title': 'N-663', 'score': 0.9961377767178238}]
result = search.search('peach apple pear apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #78 checking search results for 'peach apple pear apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #78 checking search results for 'peach apple pear apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking search results for 'peach coconut banana apple apple apple banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9929764042867817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html', 'title': 'N-294', 'score': 0.9894509786265964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-949.html', 'title': 'N-949', 'score': 0.9890065618710074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9888746310638502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9886747969503082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9885213649216982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.9845792740288246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-603.html', 'title': 'N-603', 'score': 0.9839960582872329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html', 'title': 'N-652', 'score': 0.9834796082181068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html', 'title': 'N-140', 'score': 0.9803105257154068}]
result = search.search('peach coconut banana apple apple apple banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #79 checking search results for 'peach coconut banana apple apple apple banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #79 checking search results for 'peach coconut banana apple apple apple banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking search results for 'apple banana tomato apple coconut apple apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-166.html', 'title': 'N-166', 'score': 0.9999899728810812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html', 'title': 'N-995', 'score': 0.9998662095067029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9988883794196362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-594.html', 'title': 'N-594', 'score': 0.9988165214098059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.9988119304438804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html', 'title': 'N-652', 'score': 0.9986192134707896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-29.html', 'title': 'N-29', 'score': 0.9981718620568345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html', 'title': 'N-430', 'score': 0.9979531973085581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-737.html', 'title': 'N-737', 'score': 0.9964483142650072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html', 'title': 'N-294', 'score': 0.9960911332731462}]
result = search.search('apple banana tomato apple coconut apple apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #80 checking search results for 'apple banana tomato apple coconut apple apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #80 checking search results for 'apple banana tomato apple coconut apple apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking search results for 'apple apple peach tomato peach pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9999923562359395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html', 'title': 'N-259', 'score': 0.9999749809533423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-441.html', 'title': 'N-441', 'score': 0.9999749809533423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.9993950594834431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html', 'title': 'N-181', 'score': 0.9991327871671074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-355.html', 'title': 'N-355', 'score': 0.9986054664196766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-976.html', 'title': 'N-976', 'score': 0.998103503024501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html', 'title': 'N-139', 'score': 0.9979786896745261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html', 'title': 'N-21', 'score': 0.9976884311689308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html', 'title': 'N-485', 'score': 0.9970918901088555}]
result = search.search('apple apple peach tomato peach pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #81 checking search results for 'apple apple peach tomato peach pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #81 checking search results for 'apple apple peach tomato peach pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking search results for 'peach peach coconut peach tomato pear peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html', 'title': 'N-537', 'score': 0.9911310745787737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9869602420357445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'title': 'N-462', 'score': 0.983887568703133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-27.html', 'title': 'N-27', 'score': 0.9835686775171887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html', 'title': 'N-346', 'score': 0.9824148993605353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-694.html', 'title': 'N-694', 'score': 0.976778180630285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html', 'title': 'N-161', 'score': 0.976778180630285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9763464860041925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-87.html', 'title': 'N-87', 'score': 0.9763153279858849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-80.html', 'title': 'N-80', 'score': 0.9628521420318127}]
result = search.search('peach peach coconut peach tomato pear peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #82 checking search results for 'peach peach coconut peach tomato pear peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #82 checking search results for 'peach peach coconut peach tomato pear peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking search results for 'tomato apple apple apple peach apple apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-651.html', 'title': 'N-651', 'score': 0.9988177839114634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 0.9963601492134625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-111.html', 'title': 'N-111', 'score': 0.9949479653537954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 0.9948021744789057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.994110851383404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9921578704511713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9916910121728856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9881598915800921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html', 'title': 'N-236', 'score': 0.9880900093746433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-78.html', 'title': 'N-78', 'score': 0.9862166520756204}]
result = search.search('tomato apple apple apple peach apple apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #83 checking search results for 'tomato apple apple apple peach apple apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #83 checking search results for 'tomato apple apple apple peach apple apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking search results for 'coconut coconut pear coconut coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html', 'title': 'N-178', 'score': 0.9990391453949294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-86.html', 'title': 'N-86', 'score': 0.9989615862550103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9988275322696596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 0.9961787734631828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'title': 'N-615', 'score': 0.9939742512990813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'title': 'N-937', 'score': 0.9919938186385481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9907532121231901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html', 'title': 'N-183', 'score': 0.9895836838883708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.9893126848800455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.983239984764087}]
result = search.search('coconut coconut pear coconut coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #84 checking search results for 'coconut coconut pear coconut coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #84 checking search results for 'coconut coconut pear coconut coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking search results for 'tomato coconut peach coconut banana coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.9999963804940447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-205.html', 'title': 'N-205', 'score': 0.9995938996925613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9992758095995772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'title': 'N-937', 'score': 0.9984885636890911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9981608629654231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9976953353115855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-295.html', 'title': 'N-295', 'score': 0.996722002643961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9964025202521145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-544.html', 'title': 'N-544', 'score': 0.9962135862287896}]
result = search.search('tomato coconut peach coconut banana coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #85 checking search results for 'tomato coconut peach coconut banana coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #85 checking search results for 'tomato coconut peach coconut banana coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking search results for 'banana apple peach tomato coconut coconut pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999953983127282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999953983127282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9964764345700028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9930880406915602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html', 'title': 'N-910', 'score': 0.9928309856348724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9926336675123993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-35.html', 'title': 'N-35', 'score': 0.9921078446518454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9915949297148383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'title': 'N-615', 'score': 0.9909856352407156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html', 'title': 'N-152', 'score': 0.9909075437845546}]
result = search.search('banana apple peach tomato coconut coconut pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #86 checking search results for 'banana apple peach tomato coconut coconut pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #86 checking search results for 'banana apple peach tomato coconut coconut pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking search results for 'coconut peach coconut coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html', 'title': 'N-446', 'score': 0.9997589115268474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9989682200985748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-609.html', 'title': 'N-609', 'score': 0.9982613556687719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-435.html', 'title': 'N-435', 'score': 0.9975434542171298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html', 'title': 'N-811', 'score': 0.9975434542171298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.9968280149751101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9966194656204863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 0.9966169860303719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'title': 'N-406', 'score': 0.996173961109241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9949883506148474}]
result = search.search('coconut peach coconut coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #87 checking search results for 'coconut peach coconut coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #87 checking search results for 'coconut peach coconut coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking search results for 'banana peach pear peach apple peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html', 'title': 'N-504', 'score': 0.9974320634418457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html', 'title': 'N-901', 'score': 0.9972184853914918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html', 'title': 'N-346', 'score': 0.9971839011518342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html', 'title': 'N-170', 'score': 0.992634018099052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-27.html', 'title': 'N-27', 'score': 0.9906198943854738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-694.html', 'title': 'N-694', 'score': 0.9901186337482526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html', 'title': 'N-161', 'score': 0.9901186337482526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-590.html', 'title': 'N-590', 'score': 0.9887633329050799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-94.html', 'title': 'N-94', 'score': 0.9885580352871786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-80.html', 'title': 'N-80', 'score': 0.9881846678492179}]
result = search.search('banana peach pear peach apple peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #88 checking search results for 'banana peach pear peach apple peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #88 checking search results for 'banana peach pear peach apple peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking search results for 'pear tomato coconut coconut coconut peach coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'title': 'N-615', 'score': 0.9991411999893013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html', 'title': 'N-963', 'score': 0.9988540624180796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-190.html', 'title': 'N-190', 'score': 0.9976065789143103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-825.html', 'title': 'N-825', 'score': 0.9974408419816841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-86.html', 'title': 'N-86', 'score': 0.9960761686411367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-111.html', 'title': 'N-111', 'score': 0.9951154115221503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.994747428715239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-297.html', 'title': 'N-297', 'score': 0.9946579953213665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-650.html', 'title': 'N-650', 'score': 0.9937139355711991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html', 'title': 'N-178', 'score': 0.9934778093177304}]
result = search.search('pear tomato coconut coconut coconut peach coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #89 checking search results for 'pear tomato coconut coconut coconut peach coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #89 checking search results for 'pear tomato coconut coconut coconut peach coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking search results for 'coconut pear peach apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9995969329171027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9989968972862465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.9986610713300162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9983592106328126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9983260627527692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 0.9978689749912247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9975720694247544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html', 'title': 'N-92', 'score': 0.996511954883613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9963236074788717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html', 'title': 'N-296', 'score': 0.9960932470196479}]
result = search.search('coconut pear peach apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #90 checking search results for 'coconut pear peach apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #90 checking search results for 'coconut pear peach apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking search results for 'apple coconut banana apple coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999934283797164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999934283797164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9981146283762106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html', 'title': 'N-910', 'score': 0.9981011624726115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9975487593337192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-712.html', 'title': 'N-712', 'score': 0.9972932453406709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-330.html', 'title': 'N-330', 'score': 0.9968646185921091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html', 'title': 'N-207', 'score': 0.995637614515259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html', 'title': 'N-28', 'score': 0.995564726161318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html', 'title': 'N-577', 'score': 0.9949756397022615}]
result = search.search('apple coconut banana apple coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #91 checking search results for 'apple coconut banana apple coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #91 checking search results for 'apple coconut banana apple coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking search results for 'apple pear pear coconut coconut pear pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html', 'title': 'N-37', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9999476293682761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.99993713338694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'title': 'N-90', 'score': 0.9998014038116065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-131.html', 'title': 'N-131', 'score': 0.9990341772802985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html', 'title': 'N-775', 'score': 0.9962868363841081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-971.html', 'title': 'N-971', 'score': 0.9942905011897446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-473.html', 'title': 'N-473', 'score': 0.9934872899801962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-693.html', 'title': 'N-693', 'score': 0.9932732361586717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.9911317916595276}]
result = search.search('apple pear pear coconut coconut pear pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #92 checking search results for 'apple pear pear coconut coconut pear pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #92 checking search results for 'apple pear pear coconut coconut pear pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking search results for 'coconut apple apple tomato banana pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html', 'title': 'N-910', 'score': 0.9980402204313188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9979275984082548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9973653003501974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-712.html', 'title': 'N-712', 'score': 0.9970619172653652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-330.html', 'title': 'N-330', 'score': 0.9967920402949619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html', 'title': 'N-28', 'score': 0.9954814092457871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html', 'title': 'N-207', 'score': 0.9953393547453575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-577.html', 'title': 'N-577', 'score': 0.9948178391833132}]
result = search.search('coconut apple apple tomato banana pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #93 checking search results for 'coconut apple apple tomato banana pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #93 checking search results for 'coconut apple apple tomato banana pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking search results for 'apple coconut banana banana apple coconut coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html', 'title': 'N-765', 'score': 0.9999988960615861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html', 'title': 'N-21', 'score': 0.99764445657101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-78.html', 'title': 'N-78', 'score': 0.9969083232806338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-106.html', 'title': 'N-106', 'score': 0.995945609098007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-355.html', 'title': 'N-355', 'score': 0.994837939038826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html', 'title': 'N-67', 'score': 0.9948084793068457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-391.html', 'title': 'N-391', 'score': 0.9946120892518909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-824.html', 'title': 'N-824', 'score': 0.9944597622438599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-761.html', 'title': 'N-761', 'score': 0.9940493143063225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html', 'title': 'N-139', 'score': 0.993908488546033}]
result = search.search('apple coconut banana banana apple coconut coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #94 checking search results for 'apple coconut banana banana apple coconut coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #94 checking search results for 'apple coconut banana banana apple coconut coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking search results for 'tomato pear banana pear pear peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html', 'title': 'N-396', 'score': 0.98837580617924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9881497308399675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9875289337578501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-776.html', 'title': 'N-776', 'score': 0.9872519874409613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-672.html', 'title': 'N-672', 'score': 0.9857907701177495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.9850749444513811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-473.html', 'title': 'N-473', 'score': 0.9849898502621103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-803.html', 'title': 'N-803', 'score': 0.9829410837168889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9825094463361707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-857.html', 'title': 'N-857', 'score': 0.9810179657881881}]
result = search.search('tomato pear banana pear pear peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #95 checking search results for 'tomato pear banana pear pear peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #95 checking search results for 'tomato pear banana pear pear peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking search results for 'pear peach banana peach coconut tomato peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'title': 'N-172', 'score': 0.9953840906861364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.9920869535833773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html', 'title': 'N-28', 'score': 0.9915740872932244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html', 'title': 'N-831', 'score': 0.9876060278302105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html', 'title': 'N-263', 'score': 0.9872787439144053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html', 'title': 'N-139', 'score': 0.9863648281222539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-710.html', 'title': 'N-710', 'score': 0.9858087406365165}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-813.html', 'title': 'N-813', 'score': 0.9850370178852709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-318.html', 'title': 'N-318', 'score': 0.9846357498438657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html', 'title': 'N-566', 'score': 0.9837108518273694}]
result = search.search('pear peach banana peach coconut tomato peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #96 checking search results for 'pear peach banana peach coconut tomato peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #96 checking search results for 'pear peach banana peach coconut tomato peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking search results for 'tomato peach pear apple banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9999974862171608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999911402889735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999911402889735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9990053005161372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.9988627723210646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.9978521062566298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 0.9969892912186983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9968461258891129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9965171043285547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9964087208352386}]
result = search.search('tomato peach pear apple banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #97 checking search results for 'tomato peach pear apple banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #97 checking search results for 'tomato peach pear apple banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking search results for 'coconut tomato coconut coconut peach coconut coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9979336084538429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9976702411611567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 0.9962203961421703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-78.html', 'title': 'N-78', 'score': 0.9949086320384998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'title': 'N-937', 'score': 0.9947143215610522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-646.html', 'title': 'N-646', 'score': 0.9942535439913499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9931661401830454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html', 'title': 'N-236', 'score': 0.9929159159216365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-765.html', 'title': 'N-765', 'score': 0.9920495475606518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html', 'title': 'N-67', 'score': 0.9892439679924756}]
result = search.search('coconut tomato coconut coconut peach coconut coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #98 checking search results for 'coconut tomato coconut coconut peach coconut coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #98 checking search results for 'coconut tomato coconut coconut peach coconut coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking search results for 'tomato peach pear apple coconut coconut apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999953983127282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999953983127282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9964764345700029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9930880406915602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html', 'title': 'N-910', 'score': 0.9928309856348723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9926336675123993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-35.html', 'title': 'N-35', 'score': 0.9921078446518453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9915949297148382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'title': 'N-615', 'score': 0.9909856352407159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html', 'title': 'N-152', 'score': 0.9909075437845546}]
result = search.search('tomato peach pear apple coconut coconut apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #99 checking search results for 'tomato peach pear apple coconut coconut apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #99 checking search results for 'tomato peach pear apple coconut coconut apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
