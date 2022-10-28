
import testingtools
import crawler
import searchdata
import search
output = open('fruits5-search-failed.txt', 'w')
success_output = open('fruits5-search-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
#Test #0 checking search results for 'pear coconut banana lime coconut tomato fig apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html', 'title': 'N-645', 'score': 0.9999676853522363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 0.9952171905483229}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-695.html', 'title': 'N-695', 'score': 0.9894245992377517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html', 'title': 'N-991', 'score': 0.9891432158056633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'title': 'N-199', 'score': 0.9876401348619972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9875842526833465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html', 'title': 'N-574', 'score': 0.9866848309856151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9864447850215492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-738.html', 'title': 'N-738', 'score': 0.9859364666170342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html', 'title': 'N-872', 'score': 0.9857140833098708}]
result = search.search('pear coconut banana lime coconut tomato fig apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #0 checking search results for 'pear coconut banana lime coconut tomato fig apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #0 checking search results for 'pear coconut banana lime coconut tomato fig apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking search results for 'blueberry orange kiwi kiwi peach apple papaya coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9970469029206028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html', 'title': 'N-300', 'score': 0.9943007528237853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.9908512380266402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html', 'title': 'N-652', 'score': 0.9886650481826158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html', 'title': 'N-692', 'score': 0.9885316250091077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9881319350599704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-391.html', 'title': 'N-391', 'score': 0.9868062602275453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9861014512443318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.985812067336662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html', 'title': 'N-891', 'score': 0.9857458643791405}]
result = search.search('blueberry orange kiwi kiwi peach apple papaya coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #1 checking search results for 'blueberry orange kiwi kiwi peach apple papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #1 checking search results for 'blueberry orange kiwi kiwi peach apple papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking search results for 'pear kiwi pear coconut peach blueberry coconut orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9917734426745457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html', 'title': 'N-84', 'score': 0.9887120603176657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html', 'title': 'N-861', 'score': 0.988303350288581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html', 'title': 'N-168', 'score': 0.9875253355252445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'title': 'N-297', 'score': 0.9854894121078281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-922.html', 'title': 'N-922', 'score': 0.9852722590950502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-487.html', 'title': 'N-487', 'score': 0.9848311230115252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-712.html', 'title': 'N-712', 'score': 0.9843834596886528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-776.html', 'title': 'N-776', 'score': 0.9840075367177198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html', 'title': 'N-316', 'score': 0.9833103605486779}]
result = search.search('pear kiwi pear coconut peach blueberry coconut orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #2 checking search results for 'pear kiwi pear coconut peach blueberry coconut orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #2 checking search results for 'pear kiwi pear coconut peach blueberry coconut orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking search results for 'cherry cherry peach apricot coconut lime apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html', 'title': 'N-684', 'score': 0.9998230284981261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 0.9962031408517467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-511.html', 'title': 'N-511', 'score': 0.9933389922289131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html', 'title': 'N-64', 'score': 0.9929212230443506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-752.html', 'title': 'N-752', 'score': 0.991019766502592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-147.html', 'title': 'N-147', 'score': 0.9908360994119886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-257.html', 'title': 'N-257', 'score': 0.9900822500111274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-656.html', 'title': 'N-656', 'score': 0.9897240459971307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.9896758294388848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html', 'title': 'N-934', 'score': 0.9884427809629602}]
result = search.search('cherry cherry peach apricot coconut lime apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #3 checking search results for 'cherry cherry peach apricot coconut lime apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #3 checking search results for 'cherry cherry peach apricot coconut lime apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking search results for 'blueberry coconut papaya pear papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html', 'title': 'N-685', 'score': 0.9998399607007826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html', 'title': 'N-588', 'score': 0.9997064984508051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-730.html', 'title': 'N-730', 'score': 0.9996945911124274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9996876539172734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html', 'title': 'N-540', 'score': 0.9996327496280348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-892.html', 'title': 'N-892', 'score': 0.9995570428974405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-579.html', 'title': 'N-579', 'score': 0.9995570428974405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html', 'title': 'N-679', 'score': 0.9994782149285382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html', 'title': 'N-371', 'score': 0.9985201305266375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-635.html', 'title': 'N-635', 'score': 0.9981716238847593}]
result = search.search('blueberry coconut papaya pear papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #4 checking search results for 'blueberry coconut papaya pear papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #4 checking search results for 'blueberry coconut papaya pear papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking search results for 'banana orange apricot papaya blueberry papaya kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-815.html', 'title': 'N-815', 'score': 0.9952083269926192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-481.html', 'title': 'N-481', 'score': 0.9950784164695486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html', 'title': 'N-843', 'score': 0.9900419061022685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html', 'title': 'N-168', 'score': 0.9874384242092481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9864183459393829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 0.9861666974550786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-647.html', 'title': 'N-647', 'score': 0.9860810852028129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'title': 'N-368', 'score': 0.9859821955701223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html', 'title': 'N-371', 'score': 0.9858234545110465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-816.html', 'title': 'N-816', 'score': 0.9836012084768518}]
result = search.search('banana orange apricot papaya blueberry papaya kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #5 checking search results for 'banana orange apricot papaya blueberry papaya kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #5 checking search results for 'banana orange apricot papaya blueberry papaya kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking search results for 'lime papaya apricot kiwi pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-936.html', 'title': 'N-936', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html', 'title': 'N-484', 'score': 0.9986473488458185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html', 'title': 'N-836', 'score': 0.998006069965419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9977911815436747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'title': 'N-65', 'score': 0.9972723637203524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9961557709343994}]
result = search.search('lime papaya apricot kiwi pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #6 checking search results for 'lime papaya apricot kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #6 checking search results for 'lime papaya apricot kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking search results for 'papaya apricot tomato banana cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-432.html', 'title': 'N-432', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html', 'title': 'N-146', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'title': 'N-128', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-626.html', 'title': 'N-626', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html', 'title': 'N-953', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-725.html', 'title': 'N-725', 'score': 0.9989930056154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'title': 'N-101', 'score': 0.9981112369352279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'title': 'N-199', 'score': 0.9973614651912628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-864.html', 'title': 'N-864', 'score': 0.9972587878106587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9972445258584502}]
result = search.search('papaya apricot tomato banana cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #7 checking search results for 'papaya apricot tomato banana cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #7 checking search results for 'papaya apricot tomato banana cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking search results for 'fig blueberry lime tomato orange coconut tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-949.html', 'title': 'N-949', 'score': 0.9987660121837048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html', 'title': 'N-678', 'score': 0.9965452752083742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9961423720791674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.995685216120266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html', 'title': 'N-658', 'score': 0.9949172941340505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9948247652309072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9944687583158757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-888.html', 'title': 'N-888', 'score': 0.9944336671910375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html', 'title': 'N-880', 'score': 0.9943385533312498}]
result = search.search('fig blueberry lime tomato orange coconut tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #8 checking search results for 'fig blueberry lime tomato orange coconut tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #8 checking search results for 'fig blueberry lime tomato orange coconut tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking search results for 'cherry banana coconut fig blueberry coconut orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9977548492427628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-598.html', 'title': 'N-598', 'score': 0.9967624666075205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9940397763903079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9925950912054056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-712.html', 'title': 'N-712', 'score': 0.9917649944086728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html', 'title': 'N-828', 'score': 0.9908741538735036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-695.html', 'title': 'N-695', 'score': 0.9903930176111696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-930.html', 'title': 'N-930', 'score': 0.99003767896108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html', 'title': 'N-84', 'score': 0.9895733451883492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.9888813484641233}]
result = search.search('cherry banana coconut fig blueberry coconut orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #9 checking search results for 'cherry banana coconut fig blueberry coconut orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #9 checking search results for 'cherry banana coconut fig blueberry coconut orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking search results for 'apple apple fig pear lime blueberry apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html', 'title': 'N-352', 'score': 0.9928432080220084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html', 'title': 'N-112', 'score': 0.9928031631931793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-396.html', 'title': 'N-396', 'score': 0.9924160748109663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html', 'title': 'N-370', 'score': 0.9908198882279858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'title': 'N-562', 'score': 0.9889158309228095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-962.html', 'title': 'N-962', 'score': 0.9879347018167045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-259.html', 'title': 'N-259', 'score': 0.9877971767048843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-240.html', 'title': 'N-240', 'score': 0.9876628738969259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.9870239014380436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-143.html', 'title': 'N-143', 'score': 0.9858237909620154}]
result = search.search('apple apple fig pear lime blueberry apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #10 checking search results for 'apple apple fig pear lime blueberry apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #10 checking search results for 'apple apple fig pear lime blueberry apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking search results for 'orange banana apricot apricot blueberry apple cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-430.html', 'title': 'N-430', 'score': 0.9924580761502322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'title': 'N-378', 'score': 0.990285911790863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9895955157576234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.9878939293372146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-881.html', 'title': 'N-881', 'score': 0.9860621980126234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-661.html', 'title': 'N-661', 'score': 0.9849890254968784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html', 'title': 'N-192', 'score': 0.9845164409601458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html', 'title': 'N-244', 'score': 0.9838998601951919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html', 'title': 'N-516', 'score': 0.9833948318547806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'title': 'N-420', 'score': 0.9803105626553095}]
result = search.search('orange banana apricot apricot blueberry apple cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #11 checking search results for 'orange banana apricot apricot blueberry apple cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #11 checking search results for 'orange banana apricot apricot blueberry apple cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking search results for 'kiwi blueberry papaya peach papaya orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html', 'title': 'N-513', 'score': 0.9977354734975714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html', 'title': 'N-265', 'score': 0.9962881532306873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9950102684546067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html', 'title': 'N-316', 'score': 0.9945626417143201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-264.html', 'title': 'N-264', 'score': 0.9945064925394993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-922.html', 'title': 'N-922', 'score': 0.9937249548755143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html', 'title': 'N-371', 'score': 0.9934877457381596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-225.html', 'title': 'N-225', 'score': 0.9931635306384266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'title': 'N-9', 'score': 0.9927820938589456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html', 'title': 'N-366', 'score': 0.9927548964348374}]
result = search.search('kiwi blueberry papaya peach papaya orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #12 checking search results for 'kiwi blueberry papaya peach papaya orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #12 checking search results for 'kiwi blueberry papaya peach papaya orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking search results for 'coconut blueberry papaya lime pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html', 'title': 'N-22', 'score': 0.999752575792177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-979.html', 'title': 'N-979', 'score': 0.9951403096637301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-402.html', 'title': 'N-402', 'score': 0.9943281190479044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-72.html', 'title': 'N-72', 'score': 0.9933578041326726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'title': 'N-427', 'score': 0.992742398135829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'title': 'N-297', 'score': 0.990386833929135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-752.html', 'title': 'N-752', 'score': 0.9903677307656505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html', 'title': 'N-342', 'score': 0.9903293820297601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html', 'title': 'N-995', 'score': 0.990002871265078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'title': 'N-429', 'score': 0.9899573452069738}]
result = search.search('coconut blueberry papaya lime pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #13 checking search results for 'coconut blueberry papaya lime pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #13 checking search results for 'coconut blueberry papaya lime pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking search results for 'fig pear banana kiwi coconut papaya kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html', 'title': 'N-652', 'score': 0.9944756583542371}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9938077106026351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html', 'title': 'N-353', 'score': 0.9927727875833988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-257.html', 'title': 'N-257', 'score': 0.9870297286031166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.985708088703748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html', 'title': 'N-720', 'score': 0.9838181683333578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-493.html', 'title': 'N-493', 'score': 0.9834818030205676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-16.html', 'title': 'N-16', 'score': 0.9830269632047529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-790.html', 'title': 'N-790', 'score': 0.9827960667929438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-352.html', 'title': 'N-352', 'score': 0.9824458345840777}]
result = search.search('fig pear banana kiwi coconut papaya kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #14 checking search results for 'fig pear banana kiwi coconut papaya kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #14 checking search results for 'fig pear banana kiwi coconut papaya kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking search results for 'apple cherry coconut kiwi papaya kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 0.9978697048337095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html', 'title': 'N-388', 'score': 0.997739269241622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html', 'title': 'N-652', 'score': 0.9965394189629343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-863.html', 'title': 'N-863', 'score': 0.9962577217456504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html', 'title': 'N-300', 'score': 0.9952899591608332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-569.html', 'title': 'N-569', 'score': 0.9936124110469057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'title': 'N-682', 'score': 0.9929007697928958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-995.html', 'title': 'N-995', 'score': 0.9927317539434956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html', 'title': 'N-813', 'score': 0.9926648048727313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-830.html', 'title': 'N-830', 'score': 0.9923005773768456}]
result = search.search('apple cherry coconut kiwi papaya kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #15 checking search results for 'apple cherry coconut kiwi papaya kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #15 checking search results for 'apple cherry coconut kiwi papaya kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking search results for 'peach apple cherry blueberry apricot papaya peach fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html', 'title': 'N-505', 'score': 0.9876332077929416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9871767167390217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-569.html', 'title': 'N-569', 'score': 0.9862524809188915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'title': 'N-254', 'score': 0.9852225569789701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-394.html', 'title': 'N-394', 'score': 0.9847954793125158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9838313575799336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-445.html', 'title': 'N-445', 'score': 0.9810597397699619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-454.html', 'title': 'N-454', 'score': 0.9810147137536813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9809523961679812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-604.html', 'title': 'N-604', 'score': 0.9803485191894393}]
result = search.search('peach apple cherry blueberry apricot papaya peach fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #16 checking search results for 'peach apple cherry blueberry apricot papaya peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #16 checking search results for 'peach apple cherry blueberry apricot papaya peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking search results for 'apricot orange kiwi apricot pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html', 'title': 'N-795', 'score': 0.9996438547599923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html', 'title': 'N-680', 'score': 0.9984793795894576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html', 'title': 'N-797', 'score': 0.998231685025903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html', 'title': 'N-334', 'score': 0.9978953066325935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html', 'title': 'N-419', 'score': 0.9967407086755539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html', 'title': 'N-104', 'score': 0.996559283336323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-893.html', 'title': 'N-893', 'score': 0.9946191833925223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-757.html', 'title': 'N-757', 'score': 0.9937384905529092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-688.html', 'title': 'N-688', 'score': 0.9934493293544909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html', 'title': 'N-668', 'score': 0.9928843866599402}]
result = search.search('apricot orange kiwi apricot pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #17 checking search results for 'apricot orange kiwi apricot pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #17 checking search results for 'apricot orange kiwi apricot pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking search results for 'pear orange peach apricot lime blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html', 'title': 'N-213', 'score': 0.9977448632203089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.9976421908124623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9963391654838331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-249.html', 'title': 'N-249', 'score': 0.9961734433559281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'title': 'N-55', 'score': 0.9961582463961349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html', 'title': 'N-832', 'score': 0.9959259697853876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'title': 'N-256', 'score': 0.9954186250720212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html', 'title': 'N-954', 'score': 0.9952599556384584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'title': 'N-674', 'score': 0.9943635460229644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9943205545948544}]
result = search.search('pear orange peach apricot lime blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #18 checking search results for 'pear orange peach apricot lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #18 checking search results for 'pear orange peach apricot lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking search results for 'fig orange orange lime fig kiwi apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-978.html', 'title': 'N-978', 'score': 0.9999535951935119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-512.html', 'title': 'N-512', 'score': 0.999886144308818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html', 'title': 'N-988', 'score': 0.9952035377333351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9951995249144314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-777.html', 'title': 'N-777', 'score': 0.9947055298074123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-575.html', 'title': 'N-575', 'score': 0.9926314351515877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html', 'title': 'N-138', 'score': 0.9922505425090895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html', 'title': 'N-658', 'score': 0.9921775549976543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-683.html', 'title': 'N-683', 'score': 0.9913655660949958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-807.html', 'title': 'N-807', 'score': 0.9913506242561267}]
result = search.search('fig orange orange lime fig kiwi apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #19 checking search results for 'fig orange orange lime fig kiwi apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #19 checking search results for 'fig orange orange lime fig kiwi apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking search results for 'banana apricot peach apple apple lime lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-662.html', 'title': 'N-662', 'score': 0.9968112302042191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-566.html', 'title': 'N-566', 'score': 0.9952544659740408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-374.html', 'title': 'N-374', 'score': 0.9951786362142527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9943541575711679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html', 'title': 'N-206', 'score': 0.9940361493176681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html', 'title': 'N-204', 'score': 0.9933050195714099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-642.html', 'title': 'N-642', 'score': 0.9924691127134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-288.html', 'title': 'N-288', 'score': 0.9918704077727568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-779.html', 'title': 'N-779', 'score': 0.9917581900833545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-450.html', 'title': 'N-450', 'score': 0.9915812577580452}]
result = search.search('banana apricot peach apple apple lime lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #20 checking search results for 'banana apricot peach apple apple lime lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #20 checking search results for 'banana apricot peach apple apple lime lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking search results for 'papaya kiwi apricot apricot orange fig tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'title': 'N-844', 'score': 0.9954483355476795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-893.html', 'title': 'N-893', 'score': 0.9944840802427858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html', 'title': 'N-140', 'score': 0.9943096697995555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html', 'title': 'N-920', 'score': 0.993296962044911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-688.html', 'title': 'N-688', 'score': 0.9929501700849542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html', 'title': 'N-419', 'score': 0.9925579542901375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-628.html', 'title': 'N-628', 'score': 0.9905544733451754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9904542474738467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-724.html', 'title': 'N-724', 'score': 0.9904225440392682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html', 'title': 'N-78', 'score': 0.9896821645731337}]
result = search.search('papaya kiwi apricot apricot orange fig tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #21 checking search results for 'papaya kiwi apricot apricot orange fig tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #21 checking search results for 'papaya kiwi apricot apricot orange fig tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking search results for 'papaya apple lime coconut tomato coconut fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-405.html', 'title': 'N-405', 'score': 0.9928977050762132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9917957112379825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-16.html', 'title': 'N-16', 'score': 0.9900989833520683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 0.9898973819240319}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html', 'title': 'N-991', 'score': 0.9896851430378837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 0.9891558886288693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-160.html', 'title': 'N-160', 'score': 0.987153684298309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html', 'title': 'N-872', 'score': 0.987076148386747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html', 'title': 'N-84', 'score': 0.9862013625374004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-712.html', 'title': 'N-712', 'score': 0.9847354850343215}]
result = search.search('papaya apple lime coconut tomato coconut fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #22 checking search results for 'papaya apple lime coconut tomato coconut fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #22 checking search results for 'papaya apple lime coconut tomato coconut fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking search results for 'fig kiwi tomato coconut apricot apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-103.html', 'title': 'N-103', 'score': 0.9999721066178664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-560.html', 'title': 'N-560', 'score': 0.9997567381663528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html', 'title': 'N-920', 'score': 0.9978234661855022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.9970562283084211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-629.html', 'title': 'N-629', 'score': 0.9952709067337254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-688.html', 'title': 'N-688', 'score': 0.9951505490422682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html', 'title': 'N-622', 'score': 0.9943421590740491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-264.html', 'title': 'N-264', 'score': 0.9935056148204567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html', 'title': 'N-455', 'score': 0.9934628308387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-757.html', 'title': 'N-757', 'score': 0.9931447507293135}]
result = search.search('fig kiwi tomato coconut apricot apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #23 checking search results for 'fig kiwi tomato coconut apricot apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #23 checking search results for 'fig kiwi tomato coconut apricot apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking search results for 'banana fig coconut cherry kiwi papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-450.html', 'title': 'N-450', 'score': 0.9974331239379337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-798.html', 'title': 'N-798', 'score': 0.9969834083567742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.9944012738983627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html', 'title': 'N-760', 'score': 0.9943837929674847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.99394463548398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9931744451374639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9924857627422141}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-369.html', 'title': 'N-369', 'score': 0.9921831227691474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-536.html', 'title': 'N-536', 'score': 0.9920181344819967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'title': 'N-254', 'score': 0.9918469381083037}]
result = search.search('banana fig coconut cherry kiwi papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #24 checking search results for 'banana fig coconut cherry kiwi papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #24 checking search results for 'banana fig coconut cherry kiwi papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking search results for 'peach kiwi peach tomato tomato orange pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.9998490131779745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 0.9998376689762266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html', 'title': 'N-46', 'score': 0.9998270401495589}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html', 'title': 'N-632', 'score': 0.999817075746704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-955.html', 'title': 'N-955', 'score': 0.9998077260647499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-893.html', 'title': 'N-893', 'score': 0.9984546928597172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-156.html', 'title': 'N-156', 'score': 0.9981977066392788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9981113407950366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-787.html', 'title': 'N-787', 'score': 0.997205223880602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'title': 'N-211', 'score': 0.9962141863045656}]
result = search.search('peach kiwi peach tomato tomato orange pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #25 checking search results for 'peach kiwi peach tomato tomato orange pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #25 checking search results for 'peach kiwi peach tomato tomato orange pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking search results for 'banana tomato apricot cherry peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-820.html', 'title': 'N-820', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'title': 'N-169', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-36.html', 'title': 'N-36', 'score': 0.998239640065885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.9972148048989439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-662.html', 'title': 'N-662', 'score': 0.9965901311109793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html', 'title': 'N-495', 'score': 0.9946151434649612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.9945566398363818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-725.html', 'title': 'N-725', 'score': 0.9944671574714802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9942900614499526}]
result = search.search('banana tomato apricot cherry peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #26 checking search results for 'banana tomato apricot cherry peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #26 checking search results for 'banana tomato apricot cherry peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking search results for 'banana apricot tomato lime fig cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html', 'title': 'N-645', 'score': 0.999934653991385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html', 'title': 'N-247', 'score': 0.9998686724169769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9975520181693506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html', 'title': 'N-550', 'score': 0.992922692012801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html', 'title': 'N-330', 'score': 0.9924902943993137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-752.html', 'title': 'N-752', 'score': 0.991870608794889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-347.html', 'title': 'N-347', 'score': 0.9915354663313521}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-323.html', 'title': 'N-323', 'score': 0.9912753671414454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9899030013198725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html', 'title': 'N-283', 'score': 0.9893119796126407}]
result = search.search('banana apricot tomato lime fig cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #27 checking search results for 'banana apricot tomato lime fig cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #27 checking search results for 'banana apricot tomato lime fig cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking search results for 'peach banana banana fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html', 'title': 'N-269', 'score': 0.9998054281769738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'title': 'N-429', 'score': 0.9997535961588021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html', 'title': 'N-704', 'score': 0.9997121608864541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-280.html', 'title': 'N-280', 'score': 0.9992253252990336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-876.html', 'title': 'N-876', 'score': 0.9979331804378158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-345.html', 'title': 'N-345', 'score': 0.9978842294955763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html', 'title': 'N-634', 'score': 0.99709612864144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'title': 'N-273', 'score': 0.9963147712425331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html', 'title': 'N-526', 'score': 0.9963132169437634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-205.html', 'title': 'N-205', 'score': 0.9957872357417676}]
result = search.search('peach banana banana fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #28 checking search results for 'peach banana banana fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #28 checking search results for 'peach banana banana fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking search results for 'papaya banana kiwi apple fig kiwi banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html', 'title': 'N-934', 'score': 0.994104401160764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html', 'title': 'N-891', 'score': 0.9935019844701545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-761.html', 'title': 'N-761', 'score': 0.993483313463401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html', 'title': 'N-231', 'score': 0.9923706212285195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-863.html', 'title': 'N-863', 'score': 0.9908112096177936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 0.9901580097173482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html', 'title': 'N-492', 'score': 0.9901188592965267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html', 'title': 'N-109', 'score': 0.9891301441030869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 0.9881863440927336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 0.9874502815726942}]
result = search.search('papaya banana kiwi apple fig kiwi banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #29 checking search results for 'papaya banana kiwi apple fig kiwi banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #29 checking search results for 'papaya banana kiwi apple fig kiwi banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking search results for 'coconut blueberry banana pear orange lime coconut orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'title': 'N-327', 'score': 0.9928662413908678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 0.9924798373865872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-882.html', 'title': 'N-882', 'score': 0.9864000970226512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-574.html', 'title': 'N-574', 'score': 0.9860072271777256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html', 'title': 'N-765', 'score': 0.9857046856792431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html', 'title': 'N-836', 'score': 0.9848950793401094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html', 'title': 'N-245', 'score': 0.9840606707936648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-631.html', 'title': 'N-631', 'score': 0.9837119042538486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.982586129589516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-404.html', 'title': 'N-404', 'score': 0.9820886469725247}]
result = search.search('coconut blueberry banana pear orange lime coconut orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #30 checking search results for 'coconut blueberry banana pear orange lime coconut orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #30 checking search results for 'coconut blueberry banana pear orange lime coconut orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking search results for 'blueberry coconut lime orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-949.html', 'title': 'N-949', 'score': 0.9987660121837048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html', 'title': 'N-678', 'score': 0.9965452752083742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9961423720791674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.995685216120266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html', 'title': 'N-658', 'score': 0.9949172941340505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9948247652309072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9944687583158754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-888.html', 'title': 'N-888', 'score': 0.9944336671910377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-880.html', 'title': 'N-880', 'score': 0.9943385533312498}]
result = search.search('blueberry coconut lime orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #31 checking search results for 'blueberry coconut lime orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #31 checking search results for 'blueberry coconut lime orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking search results for 'fig fig pear pear banana blueberry banana lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html', 'title': 'N-684', 'score': 0.9999338735026314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-401.html', 'title': 'N-401', 'score': 0.9965083562295923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-911.html', 'title': 'N-911', 'score': 0.9959162835734987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-962.html', 'title': 'N-962', 'score': 0.9951302678851448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'title': 'N-387', 'score': 0.9939656034016774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-800.html', 'title': 'N-800', 'score': 0.9927450614182836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html', 'title': 'N-525', 'score': 0.9910990114456556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-792.html', 'title': 'N-792', 'score': 0.9910911100693058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-771.html', 'title': 'N-771', 'score': 0.9904038475471203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-554.html', 'title': 'N-554', 'score': 0.9903749510641876}]
result = search.search('fig fig pear pear banana blueberry banana lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #32 checking search results for 'fig fig pear pear banana blueberry banana lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #32 checking search results for 'fig fig pear pear banana blueberry banana lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking search results for 'papaya kiwi coconut blueberry orange orange papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.996851797670968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-482.html', 'title': 'N-482', 'score': 0.9962386520533366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-762.html', 'title': 'N-762', 'score': 0.995756611767243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-567.html', 'title': 'N-567', 'score': 0.9935442392400068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-730.html', 'title': 'N-730', 'score': 0.9930316631678103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9929786293626384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-575.html', 'title': 'N-575', 'score': 0.9928389940546316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-725.html', 'title': 'N-725', 'score': 0.9922647717318455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html', 'title': 'N-704', 'score': 0.9917187665220908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'title': 'N-674', 'score': 0.9916468335679023}]
result = search.search('papaya kiwi coconut blueberry orange orange papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #33 checking search results for 'papaya kiwi coconut blueberry orange orange papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #33 checking search results for 'papaya kiwi coconut blueberry orange orange papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking search results for 'orange tomato fig orange banana orange cherry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-823.html', 'title': 'N-823', 'score': 0.9995521520195946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html', 'title': 'N-384', 'score': 0.9966977062443027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-984.html', 'title': 'N-984', 'score': 0.9939793873931705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'title': 'N-8', 'score': 0.9897127076708573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-567.html', 'title': 'N-567', 'score': 0.9888467892374532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-290.html', 'title': 'N-290', 'score': 0.987883750057963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html', 'title': 'N-520', 'score': 0.9877235634774908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 0.987513931937789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-887.html', 'title': 'N-887', 'score': 0.9869171274978329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9863463177628565}]
result = search.search('orange tomato fig orange banana orange cherry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #34 checking search results for 'orange tomato fig orange banana orange cherry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #34 checking search results for 'orange tomato fig orange banana orange cherry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking search results for 'cherry cherry apricot pear lime banana apple cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 0.9930338337467189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-285.html', 'title': 'N-285', 'score': 0.9894597850057152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 0.9884892375641233}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html', 'title': 'N-64', 'score': 0.9880150761940278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html', 'title': 'N-245', 'score': 0.9860838953558351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-323.html', 'title': 'N-323', 'score': 0.9854295127950149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html', 'title': 'N-550', 'score': 0.9827098718516245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-402.html', 'title': 'N-402', 'score': 0.9794581934354644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 0.9786840545484765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9772020075857434}]
result = search.search('cherry cherry apricot pear lime banana apple cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #35 checking search results for 'cherry cherry apricot pear lime banana apple cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #35 checking search results for 'cherry cherry apricot pear lime banana apple cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking search results for 'fig orange peach apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html', 'title': 'N-740', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9985191786578984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9983284551376891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9981127585668806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 0.9980139403165718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9974809994130428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html', 'title': 'N-891', 'score': 0.997468234598266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'title': 'N-105', 'score': 0.9964566503620595}]
result = search.search('fig orange peach apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #36 checking search results for 'fig orange peach apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #36 checking search results for 'fig orange peach apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking search results for 'orange tomato peach fig kiwi tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-182.html', 'title': 'N-182', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html', 'title': 'N-513', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9989047815383213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 0.9978340492933243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html', 'title': 'N-860', 'score': 0.9975136692455581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html', 'title': 'N-960', 'score': 0.9968237559356748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9965221199604383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9964755306423034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html', 'title': 'N-678', 'score': 0.9961946866041099}]
result = search.search('orange tomato peach fig kiwi tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #37 checking search results for 'orange tomato peach fig kiwi tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #37 checking search results for 'orange tomato peach fig kiwi tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking search results for 'kiwi kiwi tomato apple kiwi orange blueberry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-116.html', 'title': 'N-116', 'score': 0.9998243917884343}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-463.html', 'title': 'N-463', 'score': 0.9967470258887058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-750.html', 'title': 'N-750', 'score': 0.9898402826915913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-420.html', 'title': 'N-420', 'score': 0.9891156158747232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html', 'title': 'N-300', 'score': 0.98888539884409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-919.html', 'title': 'N-919', 'score': 0.9886562495910454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html', 'title': 'N-96', 'score': 0.9873615126441213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9868904272047127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-822.html', 'title': 'N-822', 'score': 0.9864467396528352}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html', 'title': 'N-834', 'score': 0.9863302650569908}]
result = search.search('kiwi kiwi tomato apple kiwi orange blueberry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #38 checking search results for 'kiwi kiwi tomato apple kiwi orange blueberry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #38 checking search results for 'kiwi kiwi tomato apple kiwi orange blueberry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking search results for 'apricot blueberry papaya kiwi cherry apricot apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'title': 'N-844', 'score': 0.9933084395402801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 0.9919367479093051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.989994831311482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-698.html', 'title': 'N-698', 'score': 0.9891916579373936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-629.html', 'title': 'N-629', 'score': 0.9886476317805495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'title': 'N-651', 'score': 0.9832797725324155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9822834388480636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.9796648620546596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-85.html', 'title': 'N-85', 'score': 0.9794627716947915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html', 'title': 'N-110', 'score': 0.9790517355597459}]
result = search.search('apricot blueberry papaya kiwi cherry apricot apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #39 checking search results for 'apricot blueberry papaya kiwi cherry apricot apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #39 checking search results for 'apricot blueberry papaya kiwi cherry apricot apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking search results for 'fig fig papaya apricot apricot pear coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html', 'title': 'N-193', 'score': 0.993592524016002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'title': 'N-106', 'score': 0.9905231004590063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html', 'title': 'N-988', 'score': 0.9875210493725115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-86.html', 'title': 'N-86', 'score': 0.9873118221330718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-360.html', 'title': 'N-360', 'score': 0.9869186983819985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html', 'title': 'N-189', 'score': 0.9867617946586573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-184.html', 'title': 'N-184', 'score': 0.9866678680994048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9851130548894946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-992.html', 'title': 'N-992', 'score': 0.9842787230584139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-933.html', 'title': 'N-933', 'score': 0.9839178856370161}]
result = search.search('fig fig papaya apricot apricot pear coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #40 checking search results for 'fig fig papaya apricot apricot pear coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #40 checking search results for 'fig fig papaya apricot apricot pear coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking search results for 'banana kiwi papaya peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'title': 'N-939', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-132.html', 'title': 'N-132', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-182.html', 'title': 'N-182', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html', 'title': 'N-774', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-997.html', 'title': 'N-997', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html', 'title': 'N-140', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-361.html', 'title': 'N-361', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'title': 'N-219', 'score': 0.9986817015904694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9985404780860458}]
result = search.search('banana kiwi papaya peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #41 checking search results for 'banana kiwi papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #41 checking search results for 'banana kiwi papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking search results for 'kiwi banana fig blueberry fig kiwi pear orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html', 'title': 'N-692', 'score': 0.9893388304817148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html', 'title': 'N-161', 'score': 0.9889165949366456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html', 'title': 'N-188', 'score': 0.9876132551091549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html', 'title': 'N-600', 'score': 0.9864080571332041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.986034595458637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.985066880124451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9834514049706646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-401.html', 'title': 'N-401', 'score': 0.9831087653161873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-466.html', 'title': 'N-466', 'score': 0.98299156731052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-341.html', 'title': 'N-341', 'score': 0.9824414245961977}]
result = search.search('kiwi banana fig blueberry fig kiwi pear orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #42 checking search results for 'kiwi banana fig blueberry fig kiwi pear orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #42 checking search results for 'kiwi banana fig blueberry fig kiwi pear orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking search results for 'tomato apricot coconut fig blueberry banana pear kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9963210104811757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9958062202413375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html', 'title': 'N-485', 'score': 0.9941975051004249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.991815511408744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html', 'title': 'N-539', 'score': 0.9916768470681812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'title': 'N-105', 'score': 0.9915757778367307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html', 'title': 'N-321', 'score': 0.9913676968311904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html', 'title': 'N-580', 'score': 0.989790913907491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9894265271263425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html', 'title': 'N-356', 'score': 0.9892812722775979}]
result = search.search('tomato apricot coconut fig blueberry banana pear kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #43 checking search results for 'tomato apricot coconut fig blueberry banana pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #43 checking search results for 'tomato apricot coconut fig blueberry banana pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking search results for 'blueberry orange kiwi blueberry tomato kiwi lime fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-16.html', 'title': 'N-16', 'score': 0.9984596533858736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html', 'title': 'N-894', 'score': 0.9957988451374619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html', 'title': 'N-230', 'score': 0.9938337652497586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html', 'title': 'N-185', 'score': 0.9936984346736437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.9934787074497535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html', 'title': 'N-932', 'score': 0.9934321022408787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html', 'title': 'N-423', 'score': 0.992766001889041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.9926489149531624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-441.html', 'title': 'N-441', 'score': 0.9920268932329868}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-753.html', 'title': 'N-753', 'score': 0.9906397918149085}]
result = search.search('blueberry orange kiwi blueberry tomato kiwi lime fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #44 checking search results for 'blueberry orange kiwi blueberry tomato kiwi lime fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #44 checking search results for 'blueberry orange kiwi blueberry tomato kiwi lime fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking search results for 'coconut tomato apricot cherry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-38.html', 'title': 'N-38', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html', 'title': 'N-356', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html', 'title': 'N-408', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html', 'title': 'N-558', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html', 'title': 'N-415', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-452.html', 'title': 'N-452', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html', 'title': 'N-685', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-397.html', 'title': 'N-397', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 0.9984087254887729}]
result = search.search('coconut tomato apricot cherry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #45 checking search results for 'coconut tomato apricot cherry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #45 checking search results for 'coconut tomato apricot cherry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking search results for 'coconut blueberry blueberry pear orange orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'title': 'N-217', 'score': 0.9997852342746865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-193.html', 'title': 'N-193', 'score': 0.9997199931814252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-577.html', 'title': 'N-577', 'score': 0.9983769650862867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html', 'title': 'N-597', 'score': 0.9981006038244696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.9975285042255543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 0.9968808929323404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'title': 'N-682', 'score': 0.9958247165493768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9957677579449065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html', 'title': 'N-353', 'score': 0.9954272699286989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-121.html', 'title': 'N-121', 'score': 0.9949506433354501}]
result = search.search('coconut blueberry blueberry pear orange orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #46 checking search results for 'coconut blueberry blueberry pear orange orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #46 checking search results for 'coconut blueberry blueberry pear orange orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking search results for 'kiwi tomato fig tomato blueberry lime blueberry apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 0.999931673145828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-950.html', 'title': 'N-950', 'score': 0.9999007097799161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html', 'title': 'N-67', 'score': 0.9973783903320212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9964263580454298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9948731332469591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9936562105437864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-568.html', 'title': 'N-568', 'score': 0.9929278842309103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-731.html', 'title': 'N-731', 'score': 0.9924609340103016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html', 'title': 'N-111', 'score': 0.9901224567949437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-906.html', 'title': 'N-906', 'score': 0.9898198047820891}]
result = search.search('kiwi tomato fig tomato blueberry lime blueberry apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #47 checking search results for 'kiwi tomato fig tomato blueberry lime blueberry apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #47 checking search results for 'kiwi tomato fig tomato blueberry lime blueberry apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking search results for 'coconut orange papaya cherry apricot lime cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-535.html', 'title': 'N-535', 'score': 0.9927810947477866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-473.html', 'title': 'N-473', 'score': 0.9896501619834788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-656.html', 'title': 'N-656', 'score': 0.9892253282249698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html', 'title': 'N-195', 'score': 0.9882027509173384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html', 'title': 'N-550', 'score': 0.9880214091482601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-64.html', 'title': 'N-64', 'score': 0.9868987700676797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'title': 'N-65', 'score': 0.9859570872380754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.984944896666082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html', 'title': 'N-69', 'score': 0.9840793397370841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-161.html', 'title': 'N-161', 'score': 0.9835938807623419}]
result = search.search('coconut orange papaya cherry apricot lime cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #48 checking search results for 'coconut orange papaya cherry apricot lime cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #48 checking search results for 'coconut orange papaya cherry apricot lime cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking search results for 'blueberry lime pear blueberry papaya papaya banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html', 'title': 'N-439', 'score': 0.9961315139886855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html', 'title': 'N-673', 'score': 0.9947141788855167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9927234845155325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-445.html', 'title': 'N-445', 'score': 0.9909871025695586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9890598619464307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0.9888550189428094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html', 'title': 'N-185', 'score': 0.9880528370725775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'title': 'N-149', 'score': 0.9860873926193487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9860572121307107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html', 'title': 'N-914', 'score': 0.9860138486313849}]
result = search.search('blueberry lime pear blueberry papaya papaya banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #49 checking search results for 'blueberry lime pear blueberry papaya papaya banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #49 checking search results for 'blueberry lime pear blueberry papaya papaya banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
