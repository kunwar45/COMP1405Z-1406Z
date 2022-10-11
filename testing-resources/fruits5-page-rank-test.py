
import testingtools
import crawler
import searchdata
import search
output = open('fruits5-page-rank-failed.txt', 'w')
success_output = open('fruits5-page-rank-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
#Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html
expected = 0.0003828400322230206
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-698.html
expected = 0.00036421229280495605
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-698.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-698.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-698.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html
expected = 0.0031253240176664213
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html
expected = 0.00035714372225053464
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-423.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-706.html
expected = 0.0006485136184979568
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-706.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-706.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-706.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-145.html
expected = 0.0003591615108148512
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-145.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-145.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-145.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html
expected = 0.00038520701546822527
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html
expected = 0.0006794491406872401
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-409.html
expected = 0.0006183444273504385
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-409.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-409.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-409.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html
expected = 0.0006347972697736509
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-275.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html
expected = 0.0008747605214653823
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-899.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html
expected = 0.0003487950042916212
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html
expected = 0.002080860004670832
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html
expected = 0.0003533747565611501
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-476.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html
expected = 0.0003831150087267887
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-771.html
expected = 0.00040420414156331074
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-771.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-771.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-771.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html
expected = 0.000957669746859253
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html
expected = 0.0003734007226755988
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-507.html
expected = 0.0006571029851061381
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-507.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-507.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-507.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-957.html
expected = 0.00046101204602160884
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-957.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-957.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-957.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html
expected = 0.0033233711995765565
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html
expected = 0.007500758212344802
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html
expected = 0.00043645708074579266
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html
expected = 0.001992261020904825
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html
expected = 0.0009525693348556205
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html
expected = 0.0008912192765218182
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html
expected = 0.0007095954069363871
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html
expected = 0.0003844873028720965
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html
expected = 0.0004862742995016652
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html
expected = 0.0006368775291515105
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-997.html
expected = 0.00037613064933729836
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-997.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-997.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-997.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-700.html
expected = 0.0006441959911832095
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-700.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-700.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-700.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html
expected = 0.001034420425479686
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-367.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html
expected = 0.00039520044376662535
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-580.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html
expected = 0.0010637749665610287
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html
expected = 0.0006324540946060254
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html
expected = 0.0003594694366714369
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-200.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-463.html
expected = 0.001002523954142696
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-463.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-463.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-463.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html
expected = 0.0005139878868442999
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-612.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-545.html
expected = 0.0003676170308978384
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-545.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-545.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-545.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-575.html
expected = 0.0008184113802276697
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-575.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-575.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-575.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-566.html
expected = 0.0004352366610068793
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-566.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-566.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-566.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html
expected = 0.0006511855068961516
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html
expected = 0.0003827997889854634
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-173.html
expected = 0.0018814914490981032
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-173.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-173.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-173.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-496.html
expected = 0.0008911334943320974
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-496.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-496.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-496.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-900.html
expected = 0.0005080790942499897
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-900.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-900.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-900.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html
expected = 0.00038520701546822527
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html
expected = 0.001171289719671711
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html
expected = 0.002145161240578274
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-79.html\n\n')
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
