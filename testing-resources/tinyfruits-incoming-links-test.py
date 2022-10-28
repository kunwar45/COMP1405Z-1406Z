
import testingtools
import crawler
import searchdata
import search
output = open('tinyfruits-incoming-links-failed.txt', 'w')
success_output = open('tinyfruits-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
