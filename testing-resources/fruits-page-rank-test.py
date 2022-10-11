
import testingtools
import crawler
import searchdata
import search
output = open('fruits-page-rank-failed.txt', 'w')
success_output = open('fruits-page-rank-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')
#Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-491.html
expected = 0.0006846574381268377
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-491.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-491.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-491.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-688.html
expected = 0.0003924681569743304
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-688.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-688.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-688.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-228.html
expected = 0.0011616229013485305
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-228.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-228.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-228.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-573.html
expected = 0.0006311343629434316
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-573.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-573.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-573.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html
expected = 0.0004062860028498095
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-770.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html
expected = 0.00036729490832166744
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-649.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html
expected = 0.0011909855842089775
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-112.html
expected = 0.0017967720969154753
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-112.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-112.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-112.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-75.html
expected = 0.0018231659536325636
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-75.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-75.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-75.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-192.html
expected = 0.0009050389132269149
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-192.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-192.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-192.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html
expected = 0.0003686572604238432
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html
expected = 0.00037522635102962105
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html
expected = 0.0008944126975590715
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html
expected = 0.001584211027949492
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-563.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html
expected = 0.0006299080616626142
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html
expected = 0.001172240900170708
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-801.html
expected = 0.0006887034328591783
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-801.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-801.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-801.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-708.html
expected = 0.0006423402317285988
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-708.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-708.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-708.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-987.html
expected = 0.0004253709096453197
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-987.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-987.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-987.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-536.html
expected = 0.0003825605461173355
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-536.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-536.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-536.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-684.html
expected = 0.0004134707781453321
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-684.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-684.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-684.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-967.html
expected = 0.00039898919206508637
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-967.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-967.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-967.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html
expected = 0.0019852203199706964
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html
expected = 0.0014532933976395298
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-766.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html
expected = 0.001472432411256313
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html
expected = 0.0018146288291091884
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html
expected = 0.0006412670165577172
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-713.html
expected = 0.0007952447178212694
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-713.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-713.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-713.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html
expected = 0.0015598805959350262
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html
expected = 0.0006568941019237634
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-215.html
expected = 0.0009591044786276534
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-215.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-215.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-215.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-968.html
expected = 0.0006740512236715427
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-968.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-968.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-968.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html
expected = 0.0009119469775946435
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-611.html
expected = 0.0007034995744286002
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-611.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-611.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-611.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html
expected = 0.0006139497257560401
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html
expected = 0.0006597432792956402
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html
expected = 0.0003556173546590424
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html
expected = 0.0018444373319700977
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-637.html
expected = 0.0014798151902330025
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-637.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-637.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-637.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-814.html
expected = 0.000644553286496165
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-814.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-814.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-814.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html
expected = 0.0009703191274896862
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-235.html
expected = 0.0003644259449494321
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-235.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-235.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-235.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html
expected = 0.0006853515189090121
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-997.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-289.html
expected = 0.00035862732370814203
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-289.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-289.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-289.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-260.html
expected = 0.0009286633484794791
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-260.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-260.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-260.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-999.html
expected = 0.000659199588528232
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-999.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-999.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-999.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html
expected = 0.0009123807647675068
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-263.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-651.html
expected = 0.00039209013850986134
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-651.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-651.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-651.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-712.html
expected = 0.0006319347204956278
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-712.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-712.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-712.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-751.html
expected = 0.0003927092902694676
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-751.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-751.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-751.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
