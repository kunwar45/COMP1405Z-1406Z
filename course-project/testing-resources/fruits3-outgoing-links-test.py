
import testingtools
import crawler
import searchdata
import search
output = open('fruits3-outgoing-links-failed.txt', 'w')
success_output = open('fruits3-outgoing-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')
#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-845.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-984.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-321.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-321.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-321.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-321.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-203.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-395.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-378.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-582.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-288.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-724.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-95.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-617.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-916.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-81.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-19.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-37.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-477.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-19.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-407.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-212.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-731.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-941.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-859.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-705.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-859.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-859.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-859.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-791.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-995.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-791.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-791.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-791.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-340.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-340.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-340.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-340.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-848.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-941.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-458.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-234.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-543.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-755.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-865.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-234.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-234.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-234.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-105.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-136.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-271.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-960.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-164.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-723.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-874.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-183.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-149.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-183.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-183.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-183.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-800.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-691.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-800.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-800.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-800.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-461.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-236.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-681.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-725.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-855.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-870.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-316.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-611.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-621.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-456.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-946.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-563.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-946.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-946.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-946.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-998.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-168.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-998.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-998.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-998.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-830.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-830.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-830.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-830.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-876.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-295.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-948.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-194.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-295.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-295.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-295.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-297.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-563.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-789.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-515.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-789.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-789.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-789.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-258.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-754.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-918.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-123.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-390.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-395.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-749.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-173.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-765.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-987.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-448.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-448.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-448.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-448.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-111.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-531.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-904.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-839.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-709.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-526.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-414.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-357.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-363.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-414.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-414.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-414.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-314.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-960.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-314.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-314.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-314.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-206.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-242.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-813.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-17.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-988.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-564.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-597.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-208.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-208.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-208.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-208.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-834.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-554.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-145.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-270.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-274.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-502.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-574.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-589.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-807.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-937.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-586.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-672.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-923.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-819.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-494.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-217.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-819.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-819.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-819.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #50 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
