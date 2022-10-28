
import testingtools
import crawler
import searchdata
import search
output = open('fruits4-search-failed.txt', 'w')
success_output = open('fruits4-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html')
#Test #0 checking search results for 'lime pear kiwi apple cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.998615035917524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html', 'title': 'N-470', 'score': 0.9946908365146312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html', 'title': 'N-904', 'score': 0.994645368347933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9946069422766785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html', 'title': 'N-244', 'score': 0.9945025623505718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9944221062091793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9935144205534002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-770.html', 'title': 'N-770', 'score': 0.9932098784326342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-509.html', 'title': 'N-509', 'score': 0.9928907555554024}]
result = search.search('lime pear kiwi apple cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'lime pear kiwi apple cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'lime pear kiwi apple cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'kiwi kiwi blueberry apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html', 'title': 'N-332', 'score': 0.9996940146119044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-786.html', 'title': 'N-786', 'score': 0.9996320352927528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-663.html', 'title': 'N-663', 'score': 0.9995692033165865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-629.html', 'title': 'N-629', 'score': 0.998493415237082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9976973786805461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html', 'title': 'N-596', 'score': 0.9973106655985868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html', 'title': 'N-427', 'score': 0.9963688141773636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html', 'title': 'N-768', 'score': 0.9962909374203431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-188.html', 'title': 'N-188', 'score': 0.9961955952908129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html', 'title': 'N-774', 'score': 0.9961420631724335}]
result = search.search('kiwi kiwi blueberry apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'kiwi kiwi blueberry apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'kiwi kiwi blueberry apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'pear lime tomato banana coconut fig banana orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html', 'title': 'N-52', 'score': 0.997419184025665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html', 'title': 'N-349', 'score': 0.9930077099726238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.9927399773515425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-856.html', 'title': 'N-856', 'score': 0.9925923219390882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html', 'title': 'N-440', 'score': 0.991817322186811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'title': 'N-382', 'score': 0.9897353088929639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-109.html', 'title': 'N-109', 'score': 0.9896035981555269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html', 'title': 'N-854', 'score': 0.9892971152314511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html', 'title': 'N-295', 'score': 0.9886658002080523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-452.html', 'title': 'N-452', 'score': 0.9866274532314246}]
result = search.search('pear lime tomato banana coconut fig banana orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'pear lime tomato banana coconut fig banana orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'pear lime tomato banana coconut fig banana orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'pear papaya banana apricot papaya fig papaya peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-652.html', 'title': 'N-652', 'score': 0.9901944850252179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html', 'title': 'N-620', 'score': 0.9887464045108609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html', 'title': 'N-427', 'score': 0.9874531402281157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-515.html', 'title': 'N-515', 'score': 0.9870931886475415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.986428716361849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html', 'title': 'N-742', 'score': 0.9864277590658899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html', 'title': 'N-113', 'score': 0.9845705689147963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html', 'title': 'N-100', 'score': 0.9831439767919934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html', 'title': 'N-975', 'score': 0.9812491964888176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-241.html', 'title': 'N-241', 'score': 0.9805423815148732}]
result = search.search('pear papaya banana apricot papaya fig papaya peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'pear papaya banana apricot papaya fig papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'pear papaya banana apricot papaya fig papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'pear blueberry banana peach pear papaya kiwi pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html', 'title': 'N-563', 'score': 0.9916637263418195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-897.html', 'title': 'N-897', 'score': 0.9853621796739606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9847350267122179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'title': 'N-22', 'score': 0.9825103342375952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.982294949863787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-702.html', 'title': 'N-702', 'score': 0.9801245515435952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html', 'title': 'N-464', 'score': 0.9800249832966437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-969.html', 'title': 'N-969', 'score': 0.9797137759343173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-889.html', 'title': 'N-889', 'score': 0.9745606427974736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 0.9714160273488991}]
result = search.search('pear blueberry banana peach pear papaya kiwi pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'pear blueberry banana peach pear papaya kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'pear blueberry banana peach pear papaya kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'coconut apricot banana kiwi orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-631.html', 'title': 'N-631', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'title': 'N-253', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-507.html', 'title': 'N-507', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9980301560011663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-498.html', 'title': 'N-498', 'score': 0.9970999152038936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9965879511034207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-360.html', 'title': 'N-360', 'score': 0.996078161254115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html', 'title': 'N-216', 'score': 0.9959154604929009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html', 'title': 'N-134', 'score': 0.9959008147614735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-327.html', 'title': 'N-327', 'score': 0.9958748649374096}]
result = search.search('coconut apricot banana kiwi orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'coconut apricot banana kiwi orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'coconut apricot banana kiwi orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'orange tomato kiwi papaya pear kiwi papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-276.html', 'title': 'N-276', 'score': 0.9998051507762387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.9984037104258714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-686.html', 'title': 'N-686', 'score': 0.9983949042519741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-944.html', 'title': 'N-944', 'score': 0.9969849373302916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 0.996782769341712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html', 'title': 'N-169', 'score': 0.9960917837494226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-515.html', 'title': 'N-515', 'score': 0.9959445717787443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html', 'title': 'N-461', 'score': 0.9956395647532265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-962.html', 'title': 'N-962', 'score': 0.9956289536437439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-401.html', 'title': 'N-401', 'score': 0.994727628376729}]
result = search.search('orange tomato kiwi papaya pear kiwi papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'orange tomato kiwi papaya pear kiwi papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'orange tomato kiwi papaya pear kiwi papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'coconut pear banana coconut coconut lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-711.html', 'title': 'N-711', 'score': 0.9991517771923238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-496.html', 'title': 'N-496', 'score': 0.9990641222784021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-686.html', 'title': 'N-686', 'score': 0.9981274180687161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-947.html', 'title': 'N-947', 'score': 0.9970457371955932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-91.html', 'title': 'N-91', 'score': 0.9953230978453446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-962.html', 'title': 'N-962', 'score': 0.9951800008379892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html', 'title': 'N-671', 'score': 0.994662413390707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-167.html', 'title': 'N-167', 'score': 0.9944718495171372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-832.html', 'title': 'N-832', 'score': 0.9932053328623701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'title': 'N-567', 'score': 0.9918092760553315}]
result = search.search('coconut pear banana coconut coconut lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'coconut pear banana coconut coconut lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'coconut pear banana coconut coconut lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'blueberry cherry orange coconut fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html', 'title': 'N-415', 'score': 0.9958511676917476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-358.html', 'title': 'N-358', 'score': 0.9955181454275709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-460.html', 'title': 'N-460', 'score': 0.9950180870989617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.994770125955852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html', 'title': 'N-877', 'score': 0.9941026658606265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-361.html', 'title': 'N-361', 'score': 0.9931118901397067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-207.html', 'title': 'N-207', 'score': 0.9928630375194399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-885.html', 'title': 'N-885', 'score': 0.992824368830564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-988.html', 'title': 'N-988', 'score': 0.9918275928394891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html', 'title': 'N-151', 'score': 0.9917287559416628}]
result = search.search('blueberry cherry orange coconut fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'blueberry cherry orange coconut fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'blueberry cherry orange coconut fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'lime blueberry fig kiwi papaya pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.995317433013888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9951781753983385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-496.html', 'title': 'N-496', 'score': 0.9951034349712095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-770.html', 'title': 'N-770', 'score': 0.9940528947381345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-152.html', 'title': 'N-152', 'score': 0.9938695441929238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9937434278578793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html', 'title': 'N-388', 'score': 0.9926221716487428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9925887487666207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html', 'title': 'N-682', 'score': 0.9921111598846086}]
result = search.search('lime blueberry fig kiwi papaya pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'lime blueberry fig kiwi papaya pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'lime blueberry fig kiwi papaya pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'pear blueberry fig coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-329.html', 'title': 'N-329', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-177.html', 'title': 'N-177', 'score': 0.9984261077056125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html', 'title': 'N-542', 'score': 0.9983951759314037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9979604220768861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9979480695369091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9978390857425533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9978137375969807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9973709906217061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9972441592171736}]
result = search.search('pear blueberry fig coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'pear blueberry fig coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'pear blueberry fig coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'fig apple fig peach tomato apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html', 'title': 'N-706', 'score': 0.9999247078588427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html', 'title': 'N-701', 'score': 0.9998273171785431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html', 'title': 'N-339', 'score': 0.9982222201351031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-519.html', 'title': 'N-519', 'score': 0.998130896998837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-881.html', 'title': 'N-881', 'score': 0.9978337782217245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html', 'title': 'N-60', 'score': 0.9970711799395396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html', 'title': 'N-268', 'score': 0.996879956093847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html', 'title': 'N-58', 'score': 0.9961903130632185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html', 'title': 'N-748', 'score': 0.9961536678783856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html', 'title': 'N-252', 'score': 0.996136636655687}]
result = search.search('fig apple fig peach tomato apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'fig apple fig peach tomato apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'fig apple fig peach tomato apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'orange fig orange cherry apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01734818982825989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.016713349433752613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014095461426901244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.01315766313440713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00805040513436269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006896449836629856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.00652230793669615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006251447920879089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006177273485343697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006012567286147391}]
result = search.search('orange fig orange cherry apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'orange fig orange cherry apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'orange fig orange cherry apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'kiwi apricot cherry lime orange coconut orange orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html', 'title': 'N-294', 'score': 0.990375300944365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-187.html', 'title': 'N-187', 'score': 0.9896687192253389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-367.html', 'title': 'N-367', 'score': 0.9858046581580472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-314.html', 'title': 'N-314', 'score': 0.9854173556779866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9848025917353194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-787.html', 'title': 'N-787', 'score': 0.9845407253244958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-309.html', 'title': 'N-309', 'score': 0.9831769698357762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html', 'title': 'N-843', 'score': 0.9795705590397262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html', 'title': 'N-124', 'score': 0.9784052849303895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.9779386676405524}]
result = search.search('kiwi apricot cherry lime orange coconut orange orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'kiwi apricot cherry lime orange coconut orange orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'kiwi apricot cherry lime orange coconut orange orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'coconut apple papaya apple orange banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html', 'title': 'N-559', 'score': 0.9961490041353882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-336.html', 'title': 'N-336', 'score': 0.9944599596027186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'title': 'N-22', 'score': 0.9896767913759306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-384.html', 'title': 'N-384', 'score': 0.987150574377238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html', 'title': 'N-90', 'score': 0.9870834314356157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-661.html', 'title': 'N-661', 'score': 0.9861125167157367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'title': 'N-614', 'score': 0.9858996747951413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9857133075939671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-463.html', 'title': 'N-463', 'score': 0.9849739345945312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-601.html', 'title': 'N-601', 'score': 0.9840498822896538}]
result = search.search('coconut apple papaya apple orange banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'coconut apple papaya apple orange banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'coconut apple papaya apple orange banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'kiwi cherry banana kiwi lime cherry coconut blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html', 'title': 'N-461', 'score': 0.9928412767682846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'title': 'N-344', 'score': 0.9919603493462662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html', 'title': 'N-957', 'score': 0.9905473393452933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-55.html', 'title': 'N-55', 'score': 0.9903839180258274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html', 'title': 'N-594', 'score': 0.9892793278668206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html', 'title': 'N-377', 'score': 0.9887244689097391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-767.html', 'title': 'N-767', 'score': 0.9885331150659155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 0.9848026287688559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-481.html', 'title': 'N-481', 'score': 0.9846371940592691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-266.html', 'title': 'N-266', 'score': 0.984451253935028}]
result = search.search('kiwi cherry banana kiwi lime cherry coconut blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'kiwi cherry banana kiwi lime cherry coconut blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'kiwi cherry banana kiwi lime cherry coconut blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'cherry cherry cherry banana lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-687.html', 'title': 'N-687', 'score': 0.9999932633254408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.9996599539942872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-38.html', 'title': 'N-38', 'score': 0.9995612153825446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-434.html', 'title': 'N-434', 'score': 0.9995474366803344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html', 'title': 'N-492', 'score': 0.9989228555876861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html', 'title': 'N-380', 'score': 0.9988812541089759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.9986688367405447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'title': 'N-286', 'score': 0.9970628868358731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.9960429971840153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html', 'title': 'N-299', 'score': 0.9958233631835196}]
result = search.search('cherry cherry cherry banana lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'cherry cherry cherry banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'cherry cherry cherry banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'apricot kiwi apricot banana fig papaya orange banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'title': 'N-382', 'score': 0.9912844928495396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-638.html', 'title': 'N-638', 'score': 0.991073333415543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9899689782421199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html', 'title': 'N-769', 'score': 0.9898746837714254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html', 'title': 'N-532', 'score': 0.9888586374245673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.9888583875109416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-835.html', 'title': 'N-835', 'score': 0.9871385438363075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html', 'title': 'N-117', 'score': 0.9868845178474774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-713.html', 'title': 'N-713', 'score': 0.9866989932862104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-570.html', 'title': 'N-570', 'score': 0.9864577846038398}]
result = search.search('apricot kiwi apricot banana fig papaya orange banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'apricot kiwi apricot banana fig papaya orange banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'apricot kiwi apricot banana fig papaya orange banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'apricot kiwi peach papaya orange coconut tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9947257176730829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9943298160394769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-67.html', 'title': 'N-67', 'score': 0.9921202539822157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html', 'title': 'N-261', 'score': 0.9906120363039012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html', 'title': 'N-596', 'score': 0.9905516121944019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html', 'title': 'N-124', 'score': 0.9897614333009682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-787.html', 'title': 'N-787', 'score': 0.9880742415486536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html', 'title': 'N-745', 'score': 0.9879616841906368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html', 'title': 'N-238', 'score': 0.9877917371041203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html', 'title': 'N-508', 'score': 0.9872991709019903}]
result = search.search('apricot kiwi peach papaya orange coconut tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'apricot kiwi peach papaya orange coconut tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'apricot kiwi peach papaya orange coconut tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'apricot cherry lime apple fig fig banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html', 'title': 'N-268', 'score': 0.9945761865642051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9942771849979681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-857.html', 'title': 'N-857', 'score': 0.9883958947922389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 0.98787818851651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html', 'title': 'N-566', 'score': 0.9849459272915623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-66.html', 'title': 'N-66', 'score': 0.9847012374249622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-318.html', 'title': 'N-318', 'score': 0.9841801493611227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-193.html', 'title': 'N-193', 'score': 0.9840977085958125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html', 'title': 'N-774', 'score': 0.983451088137615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 0.9828273313446226}]
result = search.search('apricot cherry lime apple fig fig banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'apricot cherry lime apple fig fig banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'apricot cherry lime apple fig fig banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'cherry orange cherry lime banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 0.9957696974218037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html', 'title': 'N-313', 'score': 0.9950375716359181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-346.html', 'title': 'N-346', 'score': 0.9931052349214601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html', 'title': 'N-105', 'score': 0.9924848106797386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 0.9916903003939792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html', 'title': 'N-466', 'score': 0.9910928012972069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-19.html', 'title': 'N-19', 'score': 0.9909268905242907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html', 'title': 'N-932', 'score': 0.9907931975521014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.9904858383469345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-404.html', 'title': 'N-404', 'score': 0.9891042709956733}]
result = search.search('cherry orange cherry lime banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'cherry orange cherry lime banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'cherry orange cherry lime banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'lime peach apricot blueberry kiwi coconut orange blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 0.9906119910805097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-334.html', 'title': 'N-334', 'score': 0.9886761027972488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-164.html', 'title': 'N-164', 'score': 0.9883734200126055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.9880432245484987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-145.html', 'title': 'N-145', 'score': 0.9878564321038931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html', 'title': 'N-846', 'score': 0.9851693402720546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html', 'title': 'N-877', 'score': 0.9847451056006084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-783.html', 'title': 'N-783', 'score': 0.9833524472269104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.9828859113143509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.9826883974453597}]
result = search.search('lime peach apricot blueberry kiwi coconut orange blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'lime peach apricot blueberry kiwi coconut orange blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'lime peach apricot blueberry kiwi coconut orange blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'banana kiwi peach coconut lime kiwi papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9936105342948671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html', 'title': 'N-45', 'score': 0.9906425329865722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-55.html', 'title': 'N-55', 'score': 0.9886561298255566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.9882757872479797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html', 'title': 'N-957', 'score': 0.9867327362863663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html', 'title': 'N-916', 'score': 0.9863054783821421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-62.html', 'title': 'N-62', 'score': 0.9841246562848253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-399.html', 'title': 'N-399', 'score': 0.9812843752472429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9812434613091336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9811462534841436}]
result = search.search('banana kiwi peach coconut lime kiwi papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'banana kiwi peach coconut lime kiwi papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'banana kiwi peach coconut lime kiwi papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'kiwi tomato orange kiwi kiwi apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-928.html', 'title': 'N-928', 'score': 0.999941222187222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-192.html', 'title': 'N-192', 'score': 0.9999169980172326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-298.html', 'title': 'N-298', 'score': 0.9999076240219337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html', 'title': 'N-851', 'score': 0.9997196065480844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'title': 'N-189', 'score': 0.9994831539127483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9994367875738244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html', 'title': 'N-68', 'score': 0.9979965563163157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html', 'title': 'N-949', 'score': 0.9979965563163157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html', 'title': 'N-339', 'score': 0.9978434732477415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-442.html', 'title': 'N-442', 'score': 0.9974989779388287}]
result = search.search('kiwi tomato orange kiwi kiwi apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'kiwi tomato orange kiwi kiwi apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'kiwi tomato orange kiwi kiwi apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'coconut peach peach coconut peach blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-694.html', 'title': 'N-694', 'score': 0.9993608376443952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html', 'title': 'N-749', 'score': 0.9977153073130574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html', 'title': 'N-568', 'score': 0.9977060972488327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-421.html', 'title': 'N-421', 'score': 0.9968699878863766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-618.html', 'title': 'N-618', 'score': 0.9955065648066248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-523.html', 'title': 'N-523', 'score': 0.9954296707818678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-615.html', 'title': 'N-615', 'score': 0.9946141092466161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-472.html', 'title': 'N-472', 'score': 0.9939031068174843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 0.9933515829243204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-35.html', 'title': 'N-35', 'score': 0.9932762224053285}]
result = search.search('coconut peach peach coconut peach blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'coconut peach peach coconut peach blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'coconut peach peach coconut peach blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'cherry apricot pear lime peach peach cherry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-992.html', 'title': 'N-992', 'score': 0.9903237179896311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-266.html', 'title': 'N-266', 'score': 0.9894408236638776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 0.9893745503818758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-346.html', 'title': 'N-346', 'score': 0.9884782104307713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-687.html', 'title': 'N-687', 'score': 0.9871024884317099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html', 'title': 'N-568', 'score': 0.9869775443535801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-317.html', 'title': 'N-317', 'score': 0.986516511087575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-116.html', 'title': 'N-116', 'score': 0.9846923595368675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html', 'title': 'N-377', 'score': 0.9839943442297918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-800.html', 'title': 'N-800', 'score': 0.9826634010583324}]
result = search.search('cherry apricot pear lime peach peach cherry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'cherry apricot pear lime peach peach cherry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'cherry apricot pear lime peach peach cherry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'fig banana orange cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html', 'title': 'N-347', 'score': 0.9997183858344825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-819.html', 'title': 'N-819', 'score': 0.999695051857328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9963219508242007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9961417013071997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-650.html', 'title': 'N-650', 'score': 0.995307200413845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-345.html', 'title': 'N-345', 'score': 0.9950586047592123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-961.html', 'title': 'N-961', 'score': 0.9938576745842619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-178.html', 'title': 'N-178', 'score': 0.9936710987798227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-903.html', 'title': 'N-903', 'score': 0.9935123697832504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-81.html', 'title': 'N-81', 'score': 0.9933055058991663}]
result = search.search('fig banana orange cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'fig banana orange cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'fig banana orange cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'papaya banana papaya papaya tomato blueberry kiwi orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html', 'title': 'N-226', 'score': 0.9959993870979458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-841.html', 'title': 'N-841', 'score': 0.9912426140445013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 0.9908800018848007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.9905311632958197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-556.html', 'title': 'N-556', 'score': 0.9896377681540144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-536.html', 'title': 'N-536', 'score': 0.9857948182179375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html', 'title': 'N-100', 'score': 0.9848718910653715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html', 'title': 'N-742', 'score': 0.9848261267845848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-91.html', 'title': 'N-91', 'score': 0.9845270250773835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html', 'title': 'N-902', 'score': 0.9844128757119264}]
result = search.search('papaya banana papaya papaya tomato blueberry kiwi orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'papaya banana papaya papaya tomato blueberry kiwi orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'papaya banana papaya papaya tomato blueberry kiwi orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'kiwi apricot lime apricot fig kiwi cherry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-791.html', 'title': 'N-791', 'score': 0.9925524993915222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html', 'title': 'N-951', 'score': 0.9898948922537198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html', 'title': 'N-753', 'score': 0.9876939448825426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-775.html', 'title': 'N-775', 'score': 0.9869936527988655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html', 'title': 'N-926', 'score': 0.9825523900010911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-196.html', 'title': 'N-196', 'score': 0.9822302262842176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html', 'title': 'N-956', 'score': 0.98074857809758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-666.html', 'title': 'N-666', 'score': 0.9792375368931534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-468.html', 'title': 'N-468', 'score': 0.9785712576241573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-325.html', 'title': 'N-325', 'score': 0.9779246375151052}]
result = search.search('kiwi apricot lime apricot fig kiwi cherry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'kiwi apricot lime apricot fig kiwi cherry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'kiwi apricot lime apricot fig kiwi cherry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'apple banana papaya cherry banana blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-438.html', 'title': 'N-438', 'score': 0.9995520315084621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-236.html', 'title': 'N-236', 'score': 0.9984049167766748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-616.html', 'title': 'N-616', 'score': 0.9973113017597678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-927.html', 'title': 'N-927', 'score': 0.995712966725845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-870.html', 'title': 'N-870', 'score': 0.9952690257776641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-880.html', 'title': 'N-880', 'score': 0.9951302691797902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html', 'title': 'N-218', 'score': 0.9945874925635562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html', 'title': 'N-776', 'score': 0.9934888437153496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-835.html', 'title': 'N-835', 'score': 0.9931549062742486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html', 'title': 'N-349', 'score': 0.992806720579891}]
result = search.search('apple banana papaya cherry banana blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'apple banana papaya cherry banana blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'apple banana papaya cherry banana blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'kiwi kiwi apricot banana cherry lime coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 0.993648246847773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html', 'title': 'N-624', 'score': 0.9922900590897685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-229.html', 'title': 'N-229', 'score': 0.9871847279499536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-576.html', 'title': 'N-576', 'score': 0.9867564186871123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 0.9866812773792113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-207.html', 'title': 'N-207', 'score': 0.9833598697852276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-361.html', 'title': 'N-361', 'score': 0.9812891763273157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.9811592344646067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-744.html', 'title': 'N-744', 'score': 0.9776538979165421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html', 'title': 'N-916', 'score': 0.9765410487968543}]
result = search.search('kiwi kiwi apricot banana cherry lime coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'kiwi kiwi apricot banana cherry lime coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'kiwi kiwi apricot banana cherry lime coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'fig cherry fig kiwi fig papaya fig coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.9925602600566298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.9916682866462982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.9887282649635907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html', 'title': 'N-126', 'score': 0.9849211644843044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-484.html', 'title': 'N-484', 'score': 0.982532657266017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-193.html', 'title': 'N-193', 'score': 0.9825314725025758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html', 'title': 'N-424', 'score': 0.9823533445992088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.9790031771108851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-544.html', 'title': 'N-544', 'score': 0.9755910270134707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-525.html', 'title': 'N-525', 'score': 0.9676407586387629}]
result = search.search('fig cherry fig kiwi fig papaya fig coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'fig cherry fig kiwi fig papaya fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'fig cherry fig kiwi fig papaya fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'lime cherry coconut tomato kiwi kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-112.html', 'title': 'N-112', 'score': 0.9998157858534825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 0.9997768548315578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-576.html', 'title': 'N-576', 'score': 0.9997669117706486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 0.9997597656527719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html', 'title': 'N-424', 'score': 0.9996774750146376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-79.html', 'title': 'N-79', 'score': 0.9995820292060628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-309.html', 'title': 'N-309', 'score': 0.9980041337539486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.9976801708478744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html', 'title': 'N-415', 'score': 0.9976545422876512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9975062840767849}]
result = search.search('lime cherry coconut tomato kiwi kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'lime cherry coconut tomato kiwi kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'lime cherry coconut tomato kiwi kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'cherry fig papaya orange papaya apricot banana fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 0.9900264742319208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 0.9852674876120819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-921.html', 'title': 'N-921', 'score': 0.9848172768926622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-733.html', 'title': 'N-733', 'score': 0.984721610594712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 0.9843026250829005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-774.html', 'title': 'N-774', 'score': 0.9837519864346247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-163.html', 'title': 'N-163', 'score': 0.9835875729386052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html', 'title': 'N-129', 'score': 0.9832320389275525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-39.html', 'title': 'N-39', 'score': 0.982369470247795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-148.html', 'title': 'N-148', 'score': 0.981650222853346}]
result = search.search('cherry fig papaya orange papaya apricot banana fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'cherry fig papaya orange papaya apricot banana fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'cherry fig papaya orange papaya apricot banana fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'fig coconut peach cherry fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 0.9996868915628734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-82.html', 'title': 'N-82', 'score': 0.9977575237766847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 0.9965105629507977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-475.html', 'title': 'N-475', 'score': 0.9937634883696065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-511.html', 'title': 'N-511', 'score': 0.9935721532912908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html', 'title': 'N-129', 'score': 0.9932953849291787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-764.html', 'title': 'N-764', 'score': 0.9929897480591222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-398.html', 'title': 'N-398', 'score': 0.9920510597440466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html', 'title': 'N-470', 'score': 0.9917032625737815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.9911345142962282}]
result = search.search('fig coconut peach cherry fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'fig coconut peach cherry fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'fig coconut peach cherry fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'banana peach fig papaya cherry coconut apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9981145668149799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.997257992451524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9930833458586387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9927409033557446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-633.html', 'title': 'N-633', 'score': 0.9921439550780856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-938.html', 'title': 'N-938', 'score': 0.9919887429145998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html', 'title': 'N-183', 'score': 0.9919239394754966}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-207.html', 'title': 'N-207', 'score': 0.991363989545585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.990914896700665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9906801826886322}]
result = search.search('banana peach fig papaya cherry coconut apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'banana peach fig papaya cherry coconut apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'banana peach fig papaya cherry coconut apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'peach kiwi peach blueberry pear fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.9997443663556641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html', 'title': 'N-722', 'score': 0.9966058003748837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html', 'title': 'N-93', 'score': 0.9960559859159014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html', 'title': 'N-834', 'score': 0.9948257429754336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-109.html', 'title': 'N-109', 'score': 0.9946707076135575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-160.html', 'title': 'N-160', 'score': 0.9944461638250456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-635.html', 'title': 'N-635', 'score': 0.9935683841349509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-127.html', 'title': 'N-127', 'score': 0.9935569377528746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-603.html', 'title': 'N-603', 'score': 0.9932182766097264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html', 'title': 'N-532', 'score': 0.9915691239138247}]
result = search.search('peach kiwi peach blueberry pear fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'peach kiwi peach blueberry pear fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'peach kiwi peach blueberry pear fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'coconut banana blueberry orange orange apricot papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-171.html', 'title': 'N-171', 'score': 0.9944983398196042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.9931375193260373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'title': 'N-344', 'score': 0.9924025062257636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 0.9889776452772843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-221.html', 'title': 'N-221', 'score': 0.9888807670692171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-65.html', 'title': 'N-65', 'score': 0.9884856543524703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html', 'title': 'N-843', 'score': 0.9880840162981197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html', 'title': 'N-175', 'score': 0.9874750876767431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html', 'title': 'N-471', 'score': 0.9871316550631037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-546.html', 'title': 'N-546', 'score': 0.9852004817259777}]
result = search.search('coconut banana blueberry orange orange apricot papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'coconut banana blueberry orange orange apricot papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'coconut banana blueberry orange orange apricot papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'tomato orange coconut apple orange orange tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html', 'title': 'N-357', 'score': 0.9953743771591312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.9944258380555437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-751.html', 'title': 'N-751', 'score': 0.9940098890423308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-279.html', 'title': 'N-279', 'score': 0.9939685718072357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-280.html', 'title': 'N-280', 'score': 0.9913146920664132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html', 'title': 'N-124', 'score': 0.9892693365248642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-524.html', 'title': 'N-524', 'score': 0.988666597599268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html', 'title': 'N-723', 'score': 0.9886497017783175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-136.html', 'title': 'N-136', 'score': 0.9883151053431206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-364.html', 'title': 'N-364', 'score': 0.987911950020964}]
result = search.search('tomato orange coconut apple orange orange tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'tomato orange coconut apple orange orange tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'tomato orange coconut apple orange orange tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'kiwi tomato tomato orange fig kiwi coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-207.html', 'title': 'N-207', 'score': 0.9962333831135145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html', 'title': 'N-989', 'score': 0.9952286978986871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html', 'title': 'N-916', 'score': 0.9949363951853217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-642.html', 'title': 'N-642', 'score': 0.994844303297007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-316.html', 'title': 'N-316', 'score': 0.9936628415411793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 0.9930467313480179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-594.html', 'title': 'N-594', 'score': 0.9928284307603187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-399.html', 'title': 'N-399', 'score': 0.9926955305258731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-944.html', 'title': 'N-944', 'score': 0.9923121872494908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-890.html', 'title': 'N-890', 'score': 0.9917104884607905}]
result = search.search('kiwi tomato tomato orange fig kiwi coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'kiwi tomato tomato orange fig kiwi coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'kiwi tomato tomato orange fig kiwi coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'banana peach blueberry banana peach peach fig lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-694.html', 'title': 'N-694', 'score': 0.9994004941549863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-421.html', 'title': 'N-421', 'score': 0.9975968045741564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-800.html', 'title': 'N-800', 'score': 0.9957406447849657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-568.html', 'title': 'N-568', 'score': 0.9938624193154258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-831.html', 'title': 'N-831', 'score': 0.9891018401383019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'title': 'N-267', 'score': 0.9885023495538598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html', 'title': 'N-23', 'score': 0.9869656389752233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-363.html', 'title': 'N-363', 'score': 0.9847974218034562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-160.html', 'title': 'N-160', 'score': 0.9844330201612838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-834.html', 'title': 'N-834', 'score': 0.9839607519840157}]
result = search.search('banana peach blueberry banana peach peach fig lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'banana peach blueberry banana peach peach fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'banana peach blueberry banana peach peach fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'kiwi orange orange cherry kiwi lime blueberry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html', 'title': 'N-688', 'score': 0.9930037085152401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 0.9929702064678755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-134.html', 'title': 'N-134', 'score': 0.9925566617976675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.991748558836052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-713.html', 'title': 'N-713', 'score': 0.9900882619406997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html', 'title': 'N-315', 'score': 0.9890276442058737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-11.html', 'title': 'N-11', 'score': 0.9890259413831199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html', 'title': 'N-552', 'score': 0.9890092949628299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-730.html', 'title': 'N-730', 'score': 0.9883677635793018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html', 'title': 'N-446', 'score': 0.988239136449819}]
result = search.search('kiwi orange orange cherry kiwi lime blueberry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'kiwi orange orange cherry kiwi lime blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'kiwi orange orange cherry kiwi lime blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'peach pear apple lime blueberry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9965181576101754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.995061263645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-152.html', 'title': 'N-152', 'score': 0.9942699708978636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-770.html', 'title': 'N-770', 'score': 0.9941059885956528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9939583700062764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.993496615383347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-18.html', 'title': 'N-18', 'score': 0.9926056337300679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-519.html', 'title': 'N-519', 'score': 0.9924063341400741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-656.html', 'title': 'N-656', 'score': 0.9911383989050285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9903548306750645}]
result = search.search('peach pear apple lime blueberry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'peach pear apple lime blueberry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'peach pear apple lime blueberry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'pear papaya papaya orange kiwi kiwi papaya tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-158.html', 'title': 'N-158', 'score': 0.9968510713333804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-540.html', 'title': 'N-540', 'score': 0.9967545549525032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html', 'title': 'N-902', 'score': 0.9952476315836791}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-728.html', 'title': 'N-728', 'score': 0.993452588308396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-161.html', 'title': 'N-161', 'score': 0.9925966893864694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-534.html', 'title': 'N-534', 'score': 0.992515127246074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-903.html', 'title': 'N-903', 'score': 0.9918178011473971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html', 'title': 'N-313', 'score': 0.9904797207135669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-929.html', 'title': 'N-929', 'score': 0.9904246503376664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html', 'title': 'N-88', 'score': 0.9904067260828946}]
result = search.search('pear papaya papaya orange kiwi kiwi papaya tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'pear papaya papaya orange kiwi kiwi papaya tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'pear papaya papaya orange kiwi kiwi papaya tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'coconut peach fig banana pear orange cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9971271540777324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html', 'title': 'N-90', 'score': 0.9966181442056952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9951005455217299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9945117149671288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-766.html', 'title': 'N-766', 'score': 0.9909216481957941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.9904148882642297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-698.html', 'title': 'N-698', 'score': 0.989830103327703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.98943545361841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html', 'title': 'N-776', 'score': 0.9892287510461761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html', 'title': 'N-154', 'score': 0.9886970354043972}]
result = search.search('coconut peach fig banana pear orange cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'coconut peach fig banana pear orange cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'coconut peach fig banana pear orange cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'banana papaya banana peach lime lime apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-99.html', 'title': 'N-99', 'score': 0.9973558219877847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html', 'title': 'N-339', 'score': 0.997134391157647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-750.html', 'title': 'N-750', 'score': 0.9963035161850924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-860.html', 'title': 'N-860', 'score': 0.9951957108720753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-870.html', 'title': 'N-870', 'score': 0.9928531798990841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'title': 'N-114', 'score': 0.9926058394098703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html', 'title': 'N-986', 'score': 0.9923262534111601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html', 'title': 'N-470', 'score': 0.9914985544764087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html', 'title': 'N-776', 'score': 0.9914125365622176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-634.html', 'title': 'N-634', 'score': 0.9908158196142276}]
result = search.search('banana papaya banana peach lime lime apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'banana papaya banana peach lime lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'banana papaya banana peach lime lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'lime orange apple papaya peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-332.html', 'title': 'N-332', 'score': 0.9998154331016322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html', 'title': 'N-119', 'score': 0.9944944700996388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-114.html', 'title': 'N-114', 'score': 0.9936621209541157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-499.html', 'title': 'N-499', 'score': 0.9924699183427482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-470.html', 'title': 'N-470', 'score': 0.9917107352976516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-860.html', 'title': 'N-860', 'score': 0.9914981145393542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-882.html', 'title': 'N-882', 'score': 0.9913908153612788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-339.html', 'title': 'N-339', 'score': 0.9908535043333427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-265.html', 'title': 'N-265', 'score': 0.9897577505145682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-634.html', 'title': 'N-634', 'score': 0.9895325598334958}]
result = search.search('lime orange apple papaya peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'lime orange apple papaya peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'lime orange apple papaya peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'blueberry tomato orange cherry blueberry apricot peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.9951511337460138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-965.html', 'title': 'N-965', 'score': 0.9939149154454403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html', 'title': 'N-949', 'score': 0.9925949099084146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-207.html', 'title': 'N-207', 'score': 0.9917926388385851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 0.9902785719022491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.9897605552774128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html', 'title': 'N-877', 'score': 0.9895213759008548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-164.html', 'title': 'N-164', 'score': 0.9889395198993213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-460.html', 'title': 'N-460', 'score': 0.9887769784478069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html', 'title': 'N-283', 'score': 0.9871621766442169}]
result = search.search('blueberry tomato orange cherry blueberry apricot peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'blueberry tomato orange cherry blueberry apricot peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'blueberry tomato orange cherry blueberry apricot peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'cherry apple apple peach apricot papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-503.html', 'title': 'N-503', 'score': 0.9997840705568016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-897.html', 'title': 'N-897', 'score': 0.9979043634555433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-763.html', 'title': 'N-763', 'score': 0.9952665241050197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9930070395262297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-710.html', 'title': 'N-710', 'score': 0.9914634456582763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'title': 'N-614', 'score': 0.9913675633634096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html', 'title': 'N-388', 'score': 0.9911195769354625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9910297621135906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html', 'title': 'N-559', 'score': 0.988274193948239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-787.html', 'title': 'N-787', 'score': 0.9881701346109861}]
result = search.search('cherry apple apple peach apricot papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'cherry apple apple peach apricot papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'cherry apple apple peach apricot papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'apple fig apricot kiwi papaya peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-819.html', 'title': 'N-819', 'score': 0.99752178716866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-35.html', 'title': 'N-35', 'score': 0.993774900459011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-636.html', 'title': 'N-636', 'score': 0.9936494008198322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'title': 'N-253', 'score': 0.9929015908456822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-127.html', 'title': 'N-127', 'score': 0.9896152123287647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html', 'title': 'N-84', 'score': 0.9894418687479972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-397.html', 'title': 'N-397', 'score': 0.9892106658968336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-267.html', 'title': 'N-267', 'score': 0.9860425298314252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-919.html', 'title': 'N-919', 'score': 0.9858583614091336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-372.html', 'title': 'N-372', 'score': 0.9858357130124524}]
result = search.search('apple fig apricot kiwi papaya peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'apple fig apricot kiwi papaya peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'apple fig apricot kiwi papaya peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking search results for 'kiwi pear tomato pear pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-693.html', 'title': 'N-693', 'score': 0.9998216975179451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html', 'title': 'N-159', 'score': 0.9993581589533348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html', 'title': 'N-843', 'score': 0.9993200864988849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'title': 'N-21', 'score': 0.9993182626464547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html', 'title': 'N-748', 'score': 0.9992321772890586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-524.html', 'title': 'N-524', 'score': 0.9991505892968086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html', 'title': 'N-126', 'score': 0.9991505892968086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-760.html', 'title': 'N-760', 'score': 0.9991505892968086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.9978457538902702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-707.html', 'title': 'N-707', 'score': 0.9976064848606506}]
result = search.search('kiwi pear tomato pear pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #50 checking search results for 'kiwi pear tomato pear pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #50 checking search results for 'kiwi pear tomato pear pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking search results for 'kiwi pear pear kiwi blueberry cherry tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.017865926274544235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01616702964243555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.014547823595640967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.01149348261094184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008540469254929331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007894303845737236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006747694838538044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.006398631961226956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006326259913773416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006101574643199806}]
result = search.search('kiwi pear pear kiwi blueberry cherry tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #51 checking search results for 'kiwi pear pear kiwi blueberry cherry tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #51 checking search results for 'kiwi pear pear kiwi blueberry cherry tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
