
import testingtools
import crawler
import searchdata
import search
output = open('fruits3-search-failed.txt', 'w')
success_output = open('fruits3-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')
#Test #0 checking search results for 'pear blueberry papaya lime orange banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html', 'title': 'N-188', 'score': 0.9999051798602855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.994323812369816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html', 'title': 'N-225', 'score': 0.9907130583896067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9895632775109864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html', 'title': 'N-508', 'score': 0.9879482828551673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html', 'title': 'N-674', 'score': 0.9861890230054041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 0.9854063864184348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-62.html', 'title': 'N-62', 'score': 0.984699052005761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-275.html', 'title': 'N-275', 'score': 0.9842294814649326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-436.html', 'title': 'N-436', 'score': 0.9831336079539081}]
result = search.search('pear blueberry papaya lime orange banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'pear blueberry papaya lime orange banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'pear blueberry papaya lime orange banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'peach apple tomato banana cherry peach apricot pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9955726368737204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'title': 'N-51', 'score': 0.9949804941057596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html', 'title': 'N-577', 'score': 0.9949598107742346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-583.html', 'title': 'N-583', 'score': 0.9933663628515783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html', 'title': 'N-229', 'score': 0.992971455686078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9928478060851231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-807.html', 'title': 'N-807', 'score': 0.9898041050697847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9870931958769718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-39.html', 'title': 'N-39', 'score': 0.9866806509151594}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html', 'title': 'N-294', 'score': 0.9862636381847759}]
result = search.search('peach apple tomato banana cherry peach apricot pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'peach apple tomato banana cherry peach apricot pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'peach apple tomato banana cherry peach apricot pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'papaya blueberry apricot orange apricot papaya pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-645.html', 'title': 'N-645', 'score': 0.9981332449483815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html', 'title': 'N-387', 'score': 0.9969351570772759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-286.html', 'title': 'N-286', 'score': 0.9960816150134452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-353.html', 'title': 'N-353', 'score': 0.9945247241201886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-230.html', 'title': 'N-230', 'score': 0.9933772867004927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html', 'title': 'N-755', 'score': 0.9931792082001928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-587.html', 'title': 'N-587', 'score': 0.9929116683302325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html', 'title': 'N-133', 'score': 0.9924604650556486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-682.html', 'title': 'N-682', 'score': 0.9917061685794958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-97.html', 'title': 'N-97', 'score': 0.991557266570742}]
result = search.search('papaya blueberry apricot orange apricot papaya pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'papaya blueberry apricot orange apricot papaya pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'papaya blueberry apricot orange apricot papaya pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'tomato fig apple banana peach orange kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9961936642448268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9937091652974095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 0.9897948518165156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'title': 'N-541', 'score': 0.9891435477933547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9889554495836245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html', 'title': 'N-387', 'score': 0.9883383484601705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 0.988257932877417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html', 'title': 'N-536', 'score': 0.9881888473495417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-933.html', 'title': 'N-933', 'score': 0.9880816601653373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 0.9878937908431887}]
result = search.search('tomato fig apple banana peach orange kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'tomato fig apple banana peach orange kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'tomato fig apple banana peach orange kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'pear orange peach orange pear kiwi kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html', 'title': 'N-767', 'score': 0.9999430454358147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html', 'title': 'N-542', 'score': 0.9999279120039409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html', 'title': 'N-957', 'score': 0.9984752072517759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-14.html', 'title': 'N-14', 'score': 0.9981640395485436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html', 'title': 'N-615', 'score': 0.9975059389383352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html', 'title': 'N-438', 'score': 0.9974683304851011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html', 'title': 'N-532', 'score': 0.9971164897163497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html', 'title': 'N-975', 'score': 0.9965300225741853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-290.html', 'title': 'N-290', 'score': 0.996474044252015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9962433542016191}]
result = search.search('pear orange peach orange pear kiwi kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'pear orange peach orange pear kiwi kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'pear orange peach orange pear kiwi kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'banana blueberry orange papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-183.html', 'title': 'N-183', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html', 'title': 'N-188', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-375.html', 'title': 'N-375', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html', 'title': 'N-717', 'score': 0.9988328139156781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9979618556786457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html', 'title': 'N-966', 'score': 0.997829890973641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-62.html', 'title': 'N-62', 'score': 0.9977782272363034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9973336601995291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'title': 'N-48', 'score': 0.9973128795270343}]
result = search.search('banana blueberry orange papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'banana blueberry orange papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'banana blueberry orange papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'lime pear peach apple kiwi fig cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9974142927281384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'title': 'N-333', 'score': 0.9964470927427262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html', 'title': 'N-567', 'score': 0.9961799160002707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.9928294224252019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html', 'title': 'N-886', 'score': 0.9920511714244868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html', 'title': 'N-334', 'score': 0.9916361224388792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'title': 'N-687', 'score': 0.9914421282772565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html', 'title': 'N-536', 'score': 0.9890495096592343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.9885524080168732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.9874328814625376}]
result = search.search('lime pear peach apple kiwi fig cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'lime pear peach apple kiwi fig cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'lime pear peach apple kiwi fig cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'papaya peach cherry orange peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html', 'title': 'N-506', 'score': 0.999900342805585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'title': 'N-138', 'score': 0.9997680078087605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html', 'title': 'N-928', 'score': 0.9997539941140168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9959840827769271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9937085906463841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-829.html', 'title': 'N-829', 'score': 0.9924368969608764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html', 'title': 'N-180', 'score': 0.9899794648307608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9895074410187628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-229.html', 'title': 'N-229', 'score': 0.9891701922978509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9886066042818242}]
result = search.search('papaya peach cherry orange peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'papaya peach cherry orange peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'papaya peach cherry orange peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'apricot papaya cherry tomato apple orange coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 0.9973858025421851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9971217462950059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html', 'title': 'N-628', 'score': 0.9945977006906699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html', 'title': 'N-127', 'score': 0.9927020523869151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9924738034972892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-452.html', 'title': 'N-452', 'score': 0.9890232577992443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-962.html', 'title': 'N-962', 'score': 0.9886784542045227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 0.9882836713761702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html', 'title': 'N-101', 'score': 0.98756724918511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.9873944922378777}]
result = search.search('apricot papaya cherry tomato apple orange coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'apricot papaya cherry tomato apple orange coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'apricot papaya cherry tomato apple orange coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'peach blueberry apple banana papaya apple apple lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html', 'title': 'N-176', 'score': 0.9882582478070621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html', 'title': 'N-79', 'score': 0.987160060893431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html', 'title': 'N-272', 'score': 0.9855402325845154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'title': 'N-497', 'score': 0.9849814600672684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-342.html', 'title': 'N-342', 'score': 0.9842771552395015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html', 'title': 'N-565', 'score': 0.9837882028177471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-375.html', 'title': 'N-375', 'score': 0.9810035503331851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-212.html', 'title': 'N-212', 'score': 0.9804760825586606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html', 'title': 'N-485', 'score': 0.9739576466107991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-717.html', 'title': 'N-717', 'score': 0.9729546329005894}]
result = search.search('peach blueberry apple banana papaya apple apple lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'peach blueberry apple banana papaya apple apple lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'peach blueberry apple banana papaya apple apple lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'apple banana papaya lime apple cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-874.html', 'title': 'N-874', 'score': 0.9998426445556169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html', 'title': 'N-615', 'score': 0.9922191022354361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html', 'title': 'N-555', 'score': 0.9911707192672277}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-507.html', 'title': 'N-507', 'score': 0.9882242549515406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-168.html', 'title': 'N-168', 'score': 0.9879047095295487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-825.html', 'title': 'N-825', 'score': 0.9877773620690936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-750.html', 'title': 'N-750', 'score': 0.9876411502991047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html', 'title': 'N-29', 'score': 0.9869983753502842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html', 'title': 'N-854', 'score': 0.9863671124288597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-152.html', 'title': 'N-152', 'score': 0.9850955612859394}]
result = search.search('apple banana papaya lime apple cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'apple banana papaya lime apple cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'apple banana papaya lime apple cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'papaya peach coconut orange apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-713.html', 'title': 'N-713', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html', 'title': 'N-930', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9985053341563609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 0.9973130819444413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html', 'title': 'N-628', 'score': 0.9950957899428614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-986.html', 'title': 'N-986', 'score': 0.9950347210403964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-962.html', 'title': 'N-962', 'score': 0.9947874750178309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html', 'title': 'N-858', 'score': 0.9945967167328081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html', 'title': 'N-384', 'score': 0.994422320388288}]
result = search.search('papaya peach coconut orange apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'papaya peach coconut orange apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'papaya peach coconut orange apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'pear banana kiwi orange blueberry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html', 'title': 'N-181', 'score': 0.9998002424279288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-89.html', 'title': 'N-89', 'score': 0.9997690819038664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.9944702074756604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-230.html', 'title': 'N-230', 'score': 0.9929946312344856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9929517451761516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-147.html', 'title': 'N-147', 'score': 0.9926720867256005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-978.html', 'title': 'N-978', 'score': 0.9925082836997969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-104.html', 'title': 'N-104', 'score': 0.99221279395705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 0.9920857039775893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-855.html', 'title': 'N-855', 'score': 0.9908819222638416}]
result = search.search('pear banana kiwi orange blueberry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'pear banana kiwi orange blueberry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'pear banana kiwi orange blueberry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'banana tomato banana blueberry apricot tomato kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-49.html', 'title': 'N-49', 'score': 0.9976011964144371}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-769.html', 'title': 'N-769', 'score': 0.9973808323225034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-585.html', 'title': 'N-585', 'score': 0.9972156844193433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-171.html', 'title': 'N-171', 'score': 0.9942977802134658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9936648023955252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html', 'title': 'N-277', 'score': 0.9934072012856677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 0.9928463117612725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html', 'title': 'N-704', 'score': 0.9922933875004215}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-308.html', 'title': 'N-308', 'score': 0.9920982550223522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-812.html', 'title': 'N-812', 'score': 0.9913562784219632}]
result = search.search('banana tomato banana blueberry apricot tomato kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'banana tomato banana blueberry apricot tomato kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'banana tomato banana blueberry apricot tomato kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'cherry apple apricot cherry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 0.9997437905803862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-78.html', 'title': 'N-78', 'score': 0.9965158798396743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-116.html', 'title': 'N-116', 'score': 0.9963752473313121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html', 'title': 'N-322', 'score': 0.9962900839827689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-681.html', 'title': 'N-681', 'score': 0.9962348645628706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9955100238321126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html', 'title': 'N-348', 'score': 0.9954320496064258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-451.html', 'title': 'N-451', 'score': 0.9947201976233734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html', 'title': 'N-118', 'score': 0.9946233753018845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 0.9945359144462083}]
result = search.search('cherry apple apricot cherry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'cherry apple apricot cherry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'cherry apple apricot cherry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'cherry banana blueberry cherry tomato pear blueberry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-748.html', 'title': 'N-748', 'score': 0.9999495394698827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html', 'title': 'N-503', 'score': 0.9998086090472944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html', 'title': 'N-54', 'score': 0.9977648080753914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html', 'title': 'N-200', 'score': 0.9959953580225337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9952769520472756}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-295.html', 'title': 'N-295', 'score': 0.9943494341264202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 0.9939364365701048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-820.html', 'title': 'N-820', 'score': 0.9925437178836669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html', 'title': 'N-297', 'score': 0.9921892315184487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-590.html', 'title': 'N-590', 'score': 0.991588567026435}]
result = search.search('cherry banana blueberry cherry tomato pear blueberry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'cherry banana blueberry cherry tomato pear blueberry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'cherry banana blueberry cherry tomato pear blueberry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'papaya blueberry apple lime orange apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9963010877496571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-805.html', 'title': 'N-805', 'score': 0.9917106666070047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html', 'title': 'N-699', 'score': 0.9903145392550673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9901771712572449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 0.9900028723857138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html', 'title': 'N-740', 'score': 0.9899004299936183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 0.9888305765800784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.988490799787682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-228.html', 'title': 'N-228', 'score': 0.9883143883754605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9876090356108166}]
result = search.search('papaya blueberry apple lime orange apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'papaya blueberry apple lime orange apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'papaya blueberry apple lime orange apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'coconut cherry apricot tomato blueberry pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9987227939571641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9940583738684685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-362.html', 'title': 'N-362', 'score': 0.993534872839098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html', 'title': 'N-536', 'score': 0.9933331317711821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.9931196032838696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-593.html', 'title': 'N-593', 'score': 0.9923625080815132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9923169143391515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html', 'title': 'N-94', 'score': 0.9921176019409873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-360.html', 'title': 'N-360', 'score': 0.990320330570544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'title': 'N-50', 'score': 0.9890156705369366}]
result = search.search('coconut cherry apricot tomato blueberry pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'coconut cherry apricot tomato blueberry pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'coconut cherry apricot tomato blueberry pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'tomato kiwi orange pear banana blueberry blueberry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html', 'title': 'N-200', 'score': 0.9956945343976874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 0.9949543645416178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html', 'title': 'N-759', 'score': 0.9944354544939009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html', 'title': 'N-566', 'score': 0.9941894809152121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html', 'title': 'N-298', 'score': 0.9941780755502801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html', 'title': 'N-279', 'score': 0.9939977973314498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-83.html', 'title': 'N-83', 'score': 0.9933804729987905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-601.html', 'title': 'N-601', 'score': 0.9929388056538551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-757.html', 'title': 'N-757', 'score': 0.9908051658997152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-152.html', 'title': 'N-152', 'score': 0.9902688763802762}]
result = search.search('tomato kiwi orange pear banana blueberry blueberry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'tomato kiwi orange pear banana blueberry blueberry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'tomato kiwi orange pear banana blueberry blueberry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'pear apple fig lime banana lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.9999021383581983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9985462119315115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html', 'title': 'N-128', 'score': 0.9969963445514946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-739.html', 'title': 'N-739', 'score': 0.9952344887736844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-903.html', 'title': 'N-903', 'score': 0.9950643097951434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html', 'title': 'N-759', 'score': 0.9930004859594239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-124.html', 'title': 'N-124', 'score': 0.9923386127957553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-597.html', 'title': 'N-597', 'score': 0.9917879025977938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html', 'title': 'N-227', 'score': 0.9912289370144474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html', 'title': 'N-679', 'score': 0.9911438045270559}]
result = search.search('pear apple fig lime banana lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'pear apple fig lime banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'pear apple fig lime banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'tomato orange blueberry orange blueberry pear banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html', 'title': 'N-759', 'score': 0.9952284413789597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-671.html', 'title': 'N-671', 'score': 0.994880770432557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html', 'title': 'N-566', 'score': 0.993940109678943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html', 'title': 'N-298', 'score': 0.9939282050345006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-328.html', 'title': 'N-328', 'score': 0.993416320880962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-605.html', 'title': 'N-605', 'score': 0.9932089492279529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-498.html', 'title': 'N-498', 'score': 0.9930744075466306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-601.html', 'title': 'N-601', 'score': 0.9930489920908457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html', 'title': 'N-849', 'score': 0.9927454575700616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'title': 'N-51', 'score': 0.9922541647733405}]
result = search.search('tomato orange blueberry orange blueberry pear banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'tomato orange blueberry orange blueberry pear banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'tomato orange blueberry orange blueberry pear banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'fig coconut apple kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-649.html', 'title': 'N-649', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-818.html', 'title': 'N-818', 'score': 0.9982558148779832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.996274309725231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-718.html', 'title': 'N-718', 'score': 0.9949272991004672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9948412466360549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html', 'title': 'N-128', 'score': 0.9948005748765592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.9947309491319004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9929242975616891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html', 'title': 'N-11', 'score': 0.992870655553507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html', 'title': 'N-385', 'score': 0.9928230622376601}]
result = search.search('fig coconut apple kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'fig coconut apple kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'fig coconut apple kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'banana pear lime fig cherry peach orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9957501282731782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html', 'title': 'N-281', 'score': 0.9936656633120573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html', 'title': 'N-387', 'score': 0.9928739747459212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-373.html', 'title': 'N-373', 'score': 0.9928449673872157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html', 'title': 'N-966', 'score': 0.9924249258339488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-827.html', 'title': 'N-827', 'score': 0.9885923779998835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html', 'title': 'N-886', 'score': 0.9885657989045084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'title': 'N-394', 'score': 0.9884640364829843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'title': 'N-48', 'score': 0.9882988368118558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.9881674208449016}]
result = search.search('banana pear lime fig cherry peach orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'banana pear lime fig cherry peach orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'banana pear lime fig cherry peach orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'lime apricot tomato blueberry coconut pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html', 'title': 'N-749', 'score': 0.9999184322086396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-660.html', 'title': 'N-660', 'score': 0.9945396110055577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-548.html', 'title': 'N-548', 'score': 0.9927588369459752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9925165622491654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.9908815155842874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-507.html', 'title': 'N-507', 'score': 0.9903132505543789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 0.9891022744786385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-554.html', 'title': 'N-554', 'score': 0.9883104891627732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html', 'title': 'N-348', 'score': 0.9876527469425467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html', 'title': 'N-15', 'score': 0.9871639369409988}]
result = search.search('lime apricot tomato blueberry coconut pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'lime apricot tomato blueberry coconut pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'lime apricot tomato blueberry coconut pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'cherry cherry fig pear blueberry orange kiwi pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-368.html', 'title': 'N-368', 'score': 0.9959631459891364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-852.html', 'title': 'N-852', 'score': 0.9908065747627359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html', 'title': 'N-972', 'score': 0.9888504255753194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-974.html', 'title': 'N-974', 'score': 0.986728571333793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-499.html', 'title': 'N-499', 'score': 0.9864586867584297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-171.html', 'title': 'N-171', 'score': 0.9864248820795155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html', 'title': 'N-348', 'score': 0.9862773687198951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 0.9858103167357872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-763.html', 'title': 'N-763', 'score': 0.9835390629024221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'title': 'N-87', 'score': 0.9831409104639}]
result = search.search('cherry cherry fig pear blueberry orange kiwi pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'cherry cherry fig pear blueberry orange kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'cherry cherry fig pear blueberry orange kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'coconut papaya blueberry blueberry tomato cherry apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-569.html', 'title': 'N-569', 'score': 0.9956449601500563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-433.html', 'title': 'N-433', 'score': 0.9905877911644809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-815.html', 'title': 'N-815', 'score': 0.9900402607722568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-722.html', 'title': 'N-722', 'score': 0.9900207956022604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.98987255403949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-989.html', 'title': 'N-989', 'score': 0.9895436824453746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-863.html', 'title': 'N-863', 'score': 0.9894049250745073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9892567872677055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html', 'title': 'N-777', 'score': 0.9891540912816775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-316.html', 'title': 'N-316', 'score': 0.9883199861163124}]
result = search.search('coconut papaya blueberry blueberry tomato cherry apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'coconut papaya blueberry blueberry tomato cherry apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'coconut papaya blueberry blueberry tomato cherry apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'apple cherry apricot banana coconut pear orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9987241943234321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 0.9979673996830613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9948414484141958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html', 'title': 'N-628', 'score': 0.9941937747425612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.993294038168692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html', 'title': 'N-734', 'score': 0.9914614889945786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html', 'title': 'N-18', 'score': 0.9895679349052758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-80.html', 'title': 'N-80', 'score': 0.9879692671998743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.9872014398774772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 0.9869691545581748}]
result = search.search('apple cherry apricot banana coconut pear orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'apple cherry apricot banana coconut pear orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'apple cherry apricot banana coconut pear orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'banana coconut orange lime peach peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9965810737206505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9956117310126767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html', 'title': 'N-84', 'score': 0.9936334199274143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.9924407059033371}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.991568360388305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9900852663501227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9888235630440931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-37.html', 'title': 'N-37', 'score': 0.9875251168490297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'title': 'N-99', 'score': 0.9868991592854954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'title': 'N-394', 'score': 0.9854167372531295}]
result = search.search('banana coconut orange lime peach peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'banana coconut orange lime peach peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'banana coconut orange lime peach peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'peach banana banana tomato apricot coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 0.9998764810136828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-327.html', 'title': 'N-327', 'score': 0.9998248186617084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-300.html', 'title': 'N-300', 'score': 0.9998155464825901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-89.html', 'title': 'N-89', 'score': 0.9997665885053381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html', 'title': 'N-114', 'score': 0.9991049383170076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-524.html', 'title': 'N-524', 'score': 0.998849121870105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html', 'title': 'N-510', 'score': 0.9987656577327385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'title': 'N-580', 'score': 0.9979587968185983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-809.html', 'title': 'N-809', 'score': 0.9977952576029333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-305.html', 'title': 'N-305', 'score': 0.9977286714956884}]
result = search.search('peach banana banana tomato apricot coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'peach banana banana tomato apricot coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'peach banana banana tomato apricot coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'kiwi tomato papaya peach blueberry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html', 'title': 'N-868', 'score': 0.9998797653243167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-978.html', 'title': 'N-978', 'score': 0.9998326937086961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html', 'title': 'N-528', 'score': 0.9997878302126173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-996.html', 'title': 'N-996', 'score': 0.9996949578162792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html', 'title': 'N-118', 'score': 0.999686431852606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9988934752215823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html', 'title': 'N-36', 'score': 0.9984201376282907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html', 'title': 'N-176', 'score': 0.9979420954050973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.9967817241846996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.9967438840611184}]
result = search.search('kiwi tomato papaya peach blueberry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'kiwi tomato papaya peach blueberry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'kiwi tomato papaya peach blueberry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'apricot pear cherry apricot blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-214.html', 'title': 'N-214', 'score': 0.9998055960492834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'title': 'N-394', 'score': 0.9997084901100498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-387.html', 'title': 'N-387', 'score': 0.9997056854473082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-837.html', 'title': 'N-837', 'score': 0.9996511350777817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html', 'title': 'N-264', 'score': 0.9996321580911736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-861.html', 'title': 'N-861', 'score': 0.9995563062393924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-546.html', 'title': 'N-546', 'score': 0.9994773211375261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-806.html', 'title': 'N-806', 'score': 0.997592110878247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'title': 'N-110', 'score': 0.9975395927006632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html', 'title': 'N-841', 'score': 0.9974041750506615}]
result = search.search('apricot pear cherry apricot blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'apricot pear cherry apricot blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'apricot pear cherry apricot blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'fig apricot lime coconut cherry lime blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 0.9998492034142408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9993014952245303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html', 'title': 'N-202', 'score': 0.9962439151391154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'title': 'N-198', 'score': 0.9961951186513878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html', 'title': 'N-101', 'score': 0.9955804053724046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 0.9947445326230296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-885.html', 'title': 'N-885', 'score': 0.9907986764491246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-795.html', 'title': 'N-795', 'score': 0.9897957729360267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-673.html', 'title': 'N-673', 'score': 0.98961995727729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html', 'title': 'N-484', 'score': 0.9890765674581249}]
result = search.search('fig apricot lime coconut cherry lime blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'fig apricot lime coconut cherry lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'fig apricot lime coconut cherry lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'fig papaya tomato orange banana apricot papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-893.html', 'title': 'N-893', 'score': 0.9929866108810427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-357.html', 'title': 'N-357', 'score': 0.9917909532089763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-44.html', 'title': 'N-44', 'score': 0.990834313318818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html', 'title': 'N-680', 'score': 0.9907979040872177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html', 'title': 'N-88', 'score': 0.9901191715150454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-531.html', 'title': 'N-531', 'score': 0.9897844804486724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.989423645912276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html', 'title': 'N-917', 'score': 0.9887818385349595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.988776359832021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 0.9873038271418785}]
result = search.search('fig papaya tomato orange banana apricot papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'fig papaya tomato orange banana apricot papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'fig papaya tomato orange banana apricot papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'apple peach coconut kiwi pear coconut cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.995267155557805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html', 'title': 'N-655', 'score': 0.9938838933682042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-469.html', 'title': 'N-469', 'score': 0.9909666420722661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-983.html', 'title': 'N-983', 'score': 0.9904883162305012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 0.9903517313507106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 0.9903368367457445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-175.html', 'title': 'N-175', 'score': 0.9901577165065542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-299.html', 'title': 'N-299', 'score': 0.9899792410561746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html', 'title': 'N-527', 'score': 0.9876775033674625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html', 'title': 'N-679', 'score': 0.9869529436119236}]
result = search.search('apple peach coconut kiwi pear coconut cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'apple peach coconut kiwi pear coconut cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'apple peach coconut kiwi pear coconut cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'peach papaya kiwi coconut cherry blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 0.9998632710347812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-692.html', 'title': 'N-692', 'score': 0.9977732489268003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-995.html', 'title': 'N-995', 'score': 0.9950661599518662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-29.html', 'title': 'N-29', 'score': 0.9948470508416924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 0.9942890639963036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'title': 'N-592', 'score': 0.993665661236718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html', 'title': 'N-858', 'score': 0.990755615483488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html', 'title': 'N-777', 'score': 0.9900384454025036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-139.html', 'title': 'N-139', 'score': 0.989569312351833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html', 'title': 'N-369', 'score': 0.9893462942989399}]
result = search.search('peach papaya kiwi coconut cherry blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'peach papaya kiwi coconut cherry blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'peach papaya kiwi coconut cherry blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'apricot blueberry peach apple orange blueberry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-895.html', 'title': 'N-895', 'score': 0.999902294187652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-789.html', 'title': 'N-789', 'score': 0.9989094417212094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-773.html', 'title': 'N-773', 'score': 0.9956772127481248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-433.html', 'title': 'N-433', 'score': 0.9928222200631617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-951.html', 'title': 'N-951', 'score': 0.9926390338328802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-85.html', 'title': 'N-85', 'score': 0.9905597817170355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html', 'title': 'N-858', 'score': 0.9902495929384072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.9888628746007829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html', 'title': 'N-667', 'score': 0.987642691935492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html', 'title': 'N-777', 'score': 0.9876330210774532}]
result = search.search('apricot blueberry peach apple orange blueberry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'apricot blueberry peach apple orange blueberry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'apricot blueberry peach apple orange blueberry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'blueberry tomato papaya apple apple orange lime cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html', 'title': 'N-272', 'score': 0.9939039994699997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-779.html', 'title': 'N-779', 'score': 0.9935959992466153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html', 'title': 'N-615', 'score': 0.9915985450702004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-934.html', 'title': 'N-934', 'score': 0.9905279902069587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-750.html', 'title': 'N-750', 'score': 0.9895911806287843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-152.html', 'title': 'N-152', 'score': 0.9887980351403545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9881765408938787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-132.html', 'title': 'N-132', 'score': 0.9868763848664854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html', 'title': 'N-854', 'score': 0.9860260209016557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'title': 'N-497', 'score': 0.9847690249749781}]
result = search.search('blueberry tomato papaya apple apple orange lime cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'blueberry tomato papaya apple apple orange lime cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'blueberry tomato papaya apple apple orange lime cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'banana banana apple coconut lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html', 'title': 'N-472', 'score': 0.9998768136913342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-790.html', 'title': 'N-790', 'score': 0.9998062354031491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-609.html', 'title': 'N-609', 'score': 0.9996418257155328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 0.9996149067480279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html', 'title': 'N-319', 'score': 0.999598618150246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-189.html', 'title': 'N-189', 'score': 0.9995563364036056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html', 'title': 'N-680', 'score': 0.9995326408599388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-770.html', 'title': 'N-770', 'score': 0.9995118100733122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-148.html', 'title': 'N-148', 'score': 0.9981773918792735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'title': 'N-687', 'score': 0.9972336197560132}]
result = search.search('banana banana apple coconut lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'banana banana apple coconut lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'banana banana apple coconut lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'peach lime blueberry peach coconut pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-257.html', 'title': 'N-257', 'score': 0.9998776465035799}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html', 'title': 'N-706', 'score': 0.9957155181554552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 0.994884782150652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-199.html', 'title': 'N-199', 'score': 0.9947002083394628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html', 'title': 'N-577', 'score': 0.9937980577847498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-326.html', 'title': 'N-326', 'score': 0.9933528676293493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-534.html', 'title': 'N-534', 'score': 0.9932125959810671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html', 'title': 'N-385', 'score': 0.9928282941101363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-251.html', 'title': 'N-251', 'score': 0.9920795169845321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html', 'title': 'N-658', 'score': 0.9917452516621659}]
result = search.search('peach lime blueberry peach coconut pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'peach lime blueberry peach coconut pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'peach lime blueberry peach coconut pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'papaya papaya papaya banana blueberry papaya lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html', 'title': 'N-925', 'score': 0.998097797434275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html', 'title': 'N-264', 'score': 0.9972671119516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-837.html', 'title': 'N-837', 'score': 0.9890954826423944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.986370570015177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 0.9844768867757399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-645.html', 'title': 'N-645', 'score': 0.9840839215384577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-503.html', 'title': 'N-503', 'score': 0.9833085915347801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.9831658690202293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html', 'title': 'N-566', 'score': 0.9823993649439001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-715.html', 'title': 'N-715', 'score': 0.9809660880206065}]
result = search.search('papaya papaya papaya banana blueberry papaya lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'papaya papaya papaya banana blueberry papaya lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'papaya papaya papaya banana blueberry papaya lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'apricot banana peach orange peach kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'title': 'N-99', 'score': 0.9920523810173529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9913845949946546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9904797562620422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.9900028099690636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-959.html', 'title': 'N-959', 'score': 0.9894744763944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html', 'title': 'N-755', 'score': 0.9890337187420464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-735.html', 'title': 'N-735', 'score': 0.9882474259406472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-460.html', 'title': 'N-460', 'score': 0.9878707273365123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 0.987579668552675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9869906825509338}]
result = search.search('apricot banana peach orange peach kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'apricot banana peach orange peach kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'apricot banana peach orange peach kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'apricot peach orange kiwi cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-792.html', 'title': 'N-792', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html', 'title': 'N-485', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9986229095838403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html', 'title': 'N-94', 'score': 0.9970820914789055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html', 'title': 'N-521', 'score': 0.9967681235614372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.9963932809439893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-419.html', 'title': 'N-419', 'score': 0.9963269493538813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.9961896316572237}]
result = search.search('apricot peach orange kiwi cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'apricot peach orange kiwi cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'apricot peach orange kiwi cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'kiwi kiwi coconut apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-32.html', 'title': 'N-32', 'score': 0.9997169751155333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 0.9996123046892044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-732.html', 'title': 'N-732', 'score': 0.9994521778908186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html', 'title': 'N-580', 'score': 0.9983791677304589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'title': 'N-51', 'score': 0.9976853323895299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-429.html', 'title': 'N-429', 'score': 0.9973949194883973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.9969050294461168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.9964276645527474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html', 'title': 'N-130', 'score': 0.9962446256961572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-537.html', 'title': 'N-537', 'score': 0.9962315017233144}]
result = search.search('kiwi kiwi coconut apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'kiwi kiwi coconut apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'kiwi kiwi coconut apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'orange fig apple pear orange blueberry fig coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html', 'title': 'N-838', 'score': 0.9936010426465147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.9895223051648382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-807.html', 'title': 'N-807', 'score': 0.9893844174183521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-131.html', 'title': 'N-131', 'score': 0.9892685944011407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html', 'title': 'N-422', 'score': 0.9886376017706135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html', 'title': 'N-374', 'score': 0.9878596393090332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-803.html', 'title': 'N-803', 'score': 0.9872248678819047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-997.html', 'title': 'N-997', 'score': 0.9867869255489352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'title': 'N-51', 'score': 0.9837465787421857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-151.html', 'title': 'N-151', 'score': 0.9831050527512161}]
result = search.search('orange fig apple pear orange blueberry fig coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'orange fig apple pear orange blueberry fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'orange fig apple pear orange blueberry fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'apricot peach kiwi cherry cherry apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-123.html', 'title': 'N-123', 'score': 0.9957216421779131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-899.html', 'title': 'N-899', 'score': 0.9952103914053699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-744.html', 'title': 'N-744', 'score': 0.9924653153651576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html', 'title': 'N-834', 'score': 0.9918416816635591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html', 'title': 'N-325', 'score': 0.9917904663809494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-869.html', 'title': 'N-869', 'score': 0.9904506470753692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-469.html', 'title': 'N-469', 'score': 0.990430545653508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html', 'title': 'N-133', 'score': 0.9894527417601712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html', 'title': 'N-438', 'score': 0.9892440478527476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-428.html', 'title': 'N-428', 'score': 0.9891958264019179}]
result = search.search('apricot peach kiwi cherry cherry apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'apricot peach kiwi cherry cherry apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'apricot peach kiwi cherry cherry apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'fig apricot fig papaya apricot orange pear orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-644.html', 'title': 'N-644', 'score': 0.9999083847106455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'title': 'N-497', 'score': 0.9943910543343377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-521.html', 'title': 'N-521', 'score': 0.9933519185447347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9929617341605319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html', 'title': 'N-841', 'score': 0.991280943302556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html', 'title': 'N-834', 'score': 0.9905072298382751}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html', 'title': 'N-422', 'score': 0.9902860448456933}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-882.html', 'title': 'N-882', 'score': 0.9901442595178405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-185.html', 'title': 'N-185', 'score': 0.9898555091825418}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-150.html', 'title': 'N-150', 'score': 0.9897452438114762}]
result = search.search('fig apricot fig papaya apricot orange pear orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'fig apricot fig papaya apricot orange pear orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'fig apricot fig papaya apricot orange pear orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'kiwi apple blueberry coconut fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 0.996258702330896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.9950242130957253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9949967253176625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9943125782554244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html', 'title': 'N-77', 'score': 0.993305978183088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9927262224418353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.9924017689001846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9922815537194531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-331.html', 'title': 'N-331', 'score': 0.9915776617692285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html', 'title': 'N-517', 'score': 0.9914557754801933}]
result = search.search('kiwi apple blueberry coconut fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'kiwi apple blueberry coconut fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'kiwi apple blueberry coconut fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'cherry apricot tomato apricot lime apricot apricot peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'title': 'N-711', 'score': 0.9980580409978024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-939.html', 'title': 'N-939', 'score': 0.9973176031895346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-184.html', 'title': 'N-184', 'score': 0.9955249068159031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html', 'title': 'N-93', 'score': 0.9930231814384334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-440.html', 'title': 'N-440', 'score': 0.9923336991910928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-994.html', 'title': 'N-994', 'score': 0.9882754846155883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html', 'title': 'N-58', 'score': 0.9865814057753908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-877.html', 'title': 'N-877', 'score': 0.9859551765385639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 0.9856904525516434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-845.html', 'title': 'N-845', 'score': 0.9854412330201027}]
result = search.search('cherry apricot tomato apricot lime apricot apricot peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'cherry apricot tomato apricot lime apricot apricot peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'cherry apricot tomato apricot lime apricot apricot peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'cherry pear kiwi banana lime orange pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 0.9940329273737172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9919626027158598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html', 'title': 'N-555', 'score': 0.9917846016370208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-316.html', 'title': 'N-316', 'score': 0.989936296457334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html', 'title': 'N-250', 'score': 0.9892679959632193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-825.html', 'title': 'N-825', 'score': 0.9849454144947156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9846966982427287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-891.html', 'title': 'N-891', 'score': 0.9846656148167507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 0.9844029585071428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-274.html', 'title': 'N-274', 'score': 0.9823928920229701}]
result = search.search('cherry pear kiwi banana lime orange pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'cherry pear kiwi banana lime orange pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'cherry pear kiwi banana lime orange pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'cherry banana kiwi kiwi fig coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'title': 'N-736', 'score': 0.9998328852236202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html', 'title': 'N-957', 'score': 0.9978435041238648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html', 'title': 'N-510', 'score': 0.9945175637471922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 0.9932206949287018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-344.html', 'title': 'N-344', 'score': 0.9925076736144108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-231.html', 'title': 'N-231', 'score': 0.9925042625370171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-798.html', 'title': 'N-798', 'score': 0.9917955625905982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-905.html', 'title': 'N-905', 'score': 0.9914325993741393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html', 'title': 'N-699', 'score': 0.9902732400007092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-803.html', 'title': 'N-803', 'score': 0.9900704279296145}]
result = search.search('cherry banana kiwi kiwi fig coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'cherry banana kiwi kiwi fig coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'cherry banana kiwi kiwi fig coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
