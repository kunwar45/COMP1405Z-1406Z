
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')


output = open('tinyfruits-all-outgoing-failed.txt', 'w')
success_output = open('tinyfruits-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruits-all-incoming-failed.txt', 'w')
success_output = open('tinyfruits-all-incoming-passed.txt', 'w')

#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruits-all-pagerank-failed.txt', 'w')
success_output = open('tinyfruits-all-pagerank-passed.txt', 'w')

#Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html
expected = 0.12476521976591842
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html
expected = 0.0819555328928385
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html
expected = 0.11896585666418055
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html
expected = 0.11939323868209492
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html
expected = 0.32242792521306995
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html
expected = 0.047437705789256435
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html
expected = 0.04626363024816037
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruits-all-idf-failed.txt', 'w')
success_output = open('tinyfruits-all-idf-passed.txt', 'w')

#Test #33 checking IDF for word fig
expected = 0.7369655941662062
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking IDF for word kiwi
expected = 0.32192809488736235
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking IDF for word papaya
expected = 0.5145731728297582
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking IDF for word cherry
expected = 0.5145731728297582
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking IDF for word lime
expected = 0.32192809488736235
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking IDF for word pear
expected = 0.7369655941662062
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking IDF for word blueberry
expected = 0.32192809488736235
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking IDF for word peach
expected = 0.5145731728297582
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking IDF for word orange
expected = 0.32192809488736235
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking IDF for word apple
expected = 0.32192809488736235
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking IDF for word apricot
expected = 0.0
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking IDF for word coconut
expected = 0.32192809488736235
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking IDF for word banana
expected = 0.0
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruits-all-tf-failed.txt', 'w')
success_output = open('tinyfruits-all-tf-passed.txt', 'w')

#Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word cherry
expected = 0.08108108108108109
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apple
expected = 0.16216216216216217
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word papaya
expected = 0.05405405405405406
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime
expected = 0.05405405405405406
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word orange
expected = 0.05405405405405406
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi
expected = 0.02702702702702703
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot
expected = 0.16216216216216217
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word peach
expected = 0.10810810810810811
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #66 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear
expected = 0.13513513513513514
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #67 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #68 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #69 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #70 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #71 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #72 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word orange
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #73 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #74 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word fig
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #75 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #76 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word peach
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #77 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #78 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #79 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word cherry
expected = 0.15
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #80 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #81 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #82 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #83 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word orange
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #84 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi
expected = 0.05
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #85 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word fig
expected = 0.15
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #86 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #87 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word peach
expected = 0.05
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #88 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #89 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #90 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word cherry
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #91 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apple
expected = 0.18181818181818182
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #92 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word papaya
expected = 0.18181818181818182
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #93 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #94 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word orange
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #95 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #96 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #97 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot
expected = 0.18181818181818182
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #98 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #99 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #100 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #101 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #102 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word cherry
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apple
expected = 0.17391304347826086
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word papaya
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime
expected = 0.08695652173913043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi
expected = 0.08695652173913043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word fig
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word peach
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word cherry
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apple
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word papaya
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word orange
expected = 0.2857142857142857
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word cherry
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apple
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word papaya
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime
expected = 0.03125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word orange
expected = 0.09375
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word fig
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot
expected = 0.03125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apple
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word papaya
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime
expected = 0.26666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word peach
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apple
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word orange
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word fig
expected = 0.1875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #152 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #152 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #153 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word peach
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear
expected = 0.1875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruits-all-tfidf-failed.txt', 'w')
success_output = open('tinyfruits-all-tfidf-passed.txt', 'w')

#Test #168 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word fig
expected = 0.06445710476952095
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear
expected = 0.06445710476952095
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word orange
expected = 0.10363769827780657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word blueberry
expected = 0.054703631988055924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word coconut
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi
expected = 0.10363769827780657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word blueberry
expected = 0.10363769827780657
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word fig
expected = 0.18271404725510207
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear
expected = 0.18271404725510207
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word orange
expected = 0.054703631988055924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apple
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word blueberry
expected = 0.02815674585715757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word fig
expected = 0.14859721830091777
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime
expected = 0.044266247441115764
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word orange
expected = 0.044266247441115764
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi
expected = 0.02266030222847964
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word cherry
expected = 0.10375537569198201
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word blueberry
expected = 0.08467816515990254
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word coconut
expected = 0.02266030222847964
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word orange
expected = 0.0404119177187868
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apple
expected = 0.07758727832568058
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word cherry
expected = 0.06459482428200948
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word coconut
expected = 0.0404119177187868
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word orange
expected = 0.11672149491947882
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apple
expected = 0.06201786293142292
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word cherry
expected = 0.0991299889868547
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word coconut
expected = 0.11672149491947882
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime
expected = 0.02445006963027565
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear
expected = 0.13476451852905313
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word orange
expected = 0.02445006963027565
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apple
expected = 0.06979767743420133
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi
expected = 0.012385909108380427
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word cherry
expected = 0.05787647829766945
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word coconut
expected = 0.02445006963027565
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word fig
expected = 0.06445710476952095
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime
expected = 0.014291714269269087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear
expected = 0.06445710476952095
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word orange
expected = 0.04161983534638364
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apple
expected = 0.054703631988055924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word cherry
expected = 0.1656555612092295
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word blueberry
expected = 0.054703631988055924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word coconut
expected = 0.014291714269269087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word fig
expected = 0.04525008888053903
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime
expected = 0.03872609348667805
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear
expected = 0.04525008888053903
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apple
expected = 0.07447019235682993
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi
expected = 0.03872609348667805
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word cherry
expected = 0.031595073081303486
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word blueberry
expected = 0.019766560368774045
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word coconut
expected = 0.05694192097566775
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime
expected = 0.10978936524490102
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apple
expected = 0.02997453317184664
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi
expected = 0.02997453317184664
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word blueberry
expected = 0.02997453317184664
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('tinyfruits-all-search-failed.txt', 'w')
success_output = open('tinyfruits-all-search-passed.txt', 'w')

#Test #289 checking search results for 'orange blueberry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.23690638923989912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10821792163398258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10666440428093199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07203323321735582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04731704897725953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04123605518358694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038732724583983275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03777409591892746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03777409591892746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.035972981087681835}]
result = search.search('orange blueberry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #289 checking search results for 'orange blueberry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #289 checking search results for 'orange blueberry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking search results for 'orange blueberry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9096552966408045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8933873095187941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8913277008828475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.816496580927726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7775650309913211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7347576643162789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5773502691896257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5773502691896257}]
result = search.search('orange blueberry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #290 checking search results for 'orange blueberry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #290 checking search results for 'orange blueberry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking search results for 'tomato banana blueberry blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('tomato banana blueberry blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #291 checking search results for 'tomato banana blueberry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #291 checking search results for 'tomato banana blueberry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking search results for 'tomato banana blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('tomato banana blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #292 checking search results for 'tomato banana blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #292 checking search results for 'tomato banana blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking search results for 'coconut fig peach papaya kiwi kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2981320630899179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10560293048493272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09037746446825236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06045650771251683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05061312355749261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03559147762797576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03426555906757586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.031756352634028276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02197728730479755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021584817575881148}]
result = search.search('coconut fig peach papaya kiwi kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #293 checking search results for 'coconut fig peach papaya kiwi kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #293 checking search results for 'coconut fig peach papaya kiwi kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking search results for 'coconut fig peach papaya kiwi kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9246471529812542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8844967407754029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7693187377873578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7596924613704238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7406586747251293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.669432724573716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6175681100588064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.4845621866890782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4750445909002452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4665612590300228}]
result = search.search('coconut fig peach papaya kiwi kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #294 checking search results for 'coconut fig peach papaya kiwi kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #294 checking search results for 'coconut fig peach papaya kiwi kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #295 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #295 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking search results for 'apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #296 checking search results for 'apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #296 checking search results for 'apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking search results for 'apple peach tomato kiwi cherry blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2727481837133017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08549975572344212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08513758965838167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06782832720612224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06195874860884399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04147388254241103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03828886884694373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03826123152979871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03063010224108815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02909938664772536}]
result = search.search('apple peach tomato kiwi cherry blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #297 checking search results for 'apple peach tomato kiwi cherry blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #297 checking search results for 'apple peach tomato kiwi cherry blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking search results for 'apple peach tomato kiwi cherry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8742809512470969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8459198549041977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8276235271975063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8276235271975063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8270261396384936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7186915483220763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7130855197342889}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.662077361348143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6289905589257659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.49660272891026475}]
result = search.search('apple peach tomato kiwi cherry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #298 checking search results for 'apple peach tomato kiwi cherry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #298 checking search results for 'apple peach tomato kiwi cherry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking search results for 'fig cherry lime cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2922109426592516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11196833647908971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07785479778206164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04439121035366098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.037948431094494986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0350744940784197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0350744940784197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02916212333725857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.021393043669721664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig cherry lime cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #299 checking search results for 'fig cherry lime cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #299 checking search results for 'fig cherry lime cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking search results for 'fig cherry lime cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9595271731929459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9411804329300667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9062829854645809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7999634565609504}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7581440083771724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7581440083771724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6520871587156075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6303466282440768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.26103232954014566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig cherry lime cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #300 checking search results for 'fig cherry lime cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #300 checking search results for 'fig cherry lime cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking search results for 'coconut orange apricot orange lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.1926563675429247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11655226437767871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.1145087967644323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04529846465857546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04441812342402381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04175654153094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04003597773195697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04003597773195697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.035249036934803454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('coconut orange apricot orange lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #301 checking search results for 'coconut orange apricot orange lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #301 checking search results for 'coconut orange apricot orange lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking search results for 'coconut orange apricot orange lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9797118908384362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9601089059756625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9590894595742705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9549042034160627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9025781441481328}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8653877250272413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8653877250272413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.5975176232505657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.43009953923298344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('coconut orange apricot orange lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #302 checking search results for 'coconut orange apricot orange lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #302 checking search results for 'coconut orange apricot orange lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #303 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #303 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking search results for 'peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #304 checking search results for 'peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #304 checking search results for 'peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking search results for 'banana peach peach fig apple apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.24344738844511746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10999826390024692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07315051934907466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06443881783340302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03628782668097415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03505462039131962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03484483768999256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.011890279670362306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.011890279670362306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('banana peach peach fig apple apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #305 checking search results for 'banana peach peach fig apple apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #305 checking search results for 'banana peach peach fig apple apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking search results for 'banana peach peach fig apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9213106631032622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7862656194019314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7843704976527885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7550443662230565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7531799277982111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.7389611240276021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6148866691689999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.25701138467911544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.25701138467911544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('banana peach peach fig apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #306 checking search results for 'banana peach peach fig apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #306 checking search results for 'banana peach peach fig apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking search results for 'apricot orange kiwi pear papaya peach blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3013619831861302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09846930366359327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09219342230940754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0528703891119306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.048290504994691556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.042442117863217645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03806864622952793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02534337650457667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02316568426044392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02275199217480263}]
result = search.search('apricot orange kiwi pear papaya peach blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #307 checking search results for 'apricot orange kiwi pear papaya peach blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #307 checking search results for 'apricot orange kiwi pear papaya peach blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking search results for 'apricot orange kiwi pear papaya peach blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9346646478805496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8946916204541625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8277106257600834}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.822863359950913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7721829420750401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.645110674602795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5478034552981157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.500732089898308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.49179003145148437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.38705101538147463}]
result = search.search('apricot orange kiwi pear papaya peach blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #308 checking search results for 'apricot orange kiwi pear papaya peach blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #308 checking search results for 'apricot orange kiwi pear papaya peach blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #309 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #309 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #310 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #310 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking search results for 'apricot peach blueberry fig fig' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.310814059872851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10750149660221621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09946842254866808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04583017745361949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044064647565836064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.03340046155405911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.026968270239430783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.01638971847809375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('apricot peach blueberry fig fig',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #311 checking search results for 'apricot peach blueberry fig fig' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #311 checking search results for 'apricot peach blueberry fig fig' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking search results for 'apricot peach blueberry fig fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9906308088618249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9639799644136153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9524684364255711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9003985300076957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8361089924267073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4075437054107391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.3454998129737895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.21615214793055323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('apricot peach blueberry fig fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #312 checking search results for 'apricot peach blueberry fig fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #312 checking search results for 'apricot peach blueberry fig fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking search results for 'orange tomato orange blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.15545773165434593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11937508858315511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10875699779976389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.060155205357440344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.046245812937820686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.041559709373331644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04053111329225092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04053111329225092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.039514633329679576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.038544879872009434}]
result = search.search('orange tomato orange blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #313 checking search results for 'orange tomato orange blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #313 checking search results for 'orange tomato orange blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking search results for 'orange tomato orange blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9998479805126307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9996148743571547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9141866485841021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8760902046562289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8760902046562289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8760902046562289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8331572698738258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.48214723197941006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.48214723197941006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.48214723197941006}]
result = search.search('orange tomato orange blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #314 checking search results for 'orange tomato orange blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #314 checking search results for 'orange tomato orange blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking search results for 'banana apricot pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('banana apricot pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #315 checking search results for 'banana apricot pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #315 checking search results for 'banana apricot pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking search results for 'banana apricot pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('banana apricot pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #316 checking search results for 'banana apricot pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #316 checking search results for 'banana apricot pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #317 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #317 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking search results for 'pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #318 checking search results for 'pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #318 checking search results for 'pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking search results for 'orange papaya banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.27334194193079353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11688561155666563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06947873543551684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04743770578925645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0448928611656317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04409116581499072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('orange papaya banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #319 checking search results for 'orange papaya banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #319 checking search results for 'orange papaya banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking search results for 'orange papaya banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9825139315947845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9703704816250737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.9530416350486021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('orange papaya banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #320 checking search results for 'orange papaya banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #320 checking search results for 'orange papaya banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking search results for 'cherry blueberry banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11555335018456396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06617270707751717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04590003855922454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.043467398059126916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04021585479175915}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}]
result = search.search('cherry blueberry banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #321 checking search results for 'cherry blueberry banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #321 checking search results for 'cherry blueberry banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking search results for 'cherry blueberry banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9921408742248392}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9713152447659879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}]
result = search.search('cherry blueberry banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #322 checking search results for 'cherry blueberry banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #322 checking search results for 'cherry blueberry banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking search results for 'blueberry apricot banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry apricot banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #323 checking search results for 'blueberry apricot banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #323 checking search results for 'blueberry apricot banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking search results for 'blueberry apricot banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry apricot banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #324 checking search results for 'blueberry apricot banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #324 checking search results for 'blueberry apricot banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking search results for 'papaya papaya apple apricot fig kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.24850012316258155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10404913386359324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07424268464147814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06669622488608432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03523053341048398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03523053341048398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.031056758275424205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.029226046170973796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.028994827066514964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02779752404486204}]
result = search.search('papaya papaya apple apricot fig kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #325 checking search results for 'papaya papaya apple apricot fig kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #325 checking search results for 'papaya papaya apple apricot fig kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking search results for 'papaya papaya apple apricot fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8746134124625811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8138099104705159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7707152629486583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7615168377731208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7615168377731207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6317283363671173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6218332416558536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6112189994036692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6008504714341432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2489216011777334}]
result = search.search('papaya papaya apple apricot fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #326 checking search results for 'papaya papaya apple apricot fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #326 checking search results for 'papaya papaya apple apricot fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking search results for 'peach tomato kiwi pear cherry kiwi banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3223775885680922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10452589935139084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07404062514402843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.06299945452947532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.051744014377588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04193622023829836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03543571598967436}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029467194343621137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.019839794906965368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.019839794906965368}]
result = search.search('peach tomato kiwi pear cherry kiwi banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #327 checking search results for 'peach tomato kiwi pear cherry kiwi banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #327 checking search results for 'peach tomato kiwi pear cherry kiwi banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking search results for 'peach tomato kiwi pear cherry kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9998438824895688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8840271581556114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8754758686939472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7659519108119155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6369408147514077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.6313669443800242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6223686965330897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5049440432812399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4288421552857772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4288421552857772}]
result = search.search('peach tomato kiwi pear cherry kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #328 checking search results for 'peach tomato kiwi pear cherry kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #328 checking search results for 'peach tomato kiwi pear cherry kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking search results for 'cherry apricot papaya pear cherry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.299333717946633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11360344254852388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.05841861176025208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04167014239387922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03449263786159874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.034418920807387766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03259233601120401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.031142637055771662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.027274432387110033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry apricot papaya pear cherry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #329 checking search results for 'cherry apricot papaya pear cherry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #329 checking search results for 'cherry apricot papaya pear cherry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking search results for 'cherry apricot papaya pear cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9549247635748649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9283740474675832}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.878418163369877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7455670399529513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7439736272913084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7044915376587858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5895437137295246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.489295812770451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3799943207799335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry apricot papaya pear cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #330 checking search results for 'cherry apricot papaya pear cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #330 checking search results for 'cherry apricot papaya pear cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #331 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #331 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #332 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #332 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking search results for 'papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #333 checking search results for 'papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #333 checking search results for 'papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking search results for 'papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #334 checking search results for 'papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #334 checking search results for 'papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking search results for 'lime papaya orange apple pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2348528096777693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10593206576571414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07954565863240269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04585395159791451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04338982496855238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.033824592580286986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.019756658230924918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01935110070717558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.013409197610821483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('lime papaya orange apple pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #335 checking search results for 'lime papaya orange apple pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #335 checking search results for 'lime papaya orange apple pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking search results for 'lime papaya orange apple pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9666140222215255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.937881976312867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8904409108299158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.7283885523332745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6662492743345938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4270451351298902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4182789072836553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.4127188413809054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.2898431778676661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('lime papaya orange apple pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #336 checking search results for 'lime papaya orange apple pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #336 checking search results for 'lime papaya orange apple pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking search results for 'cherry apple peach lime blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2727481837133017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08849532405772903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08513758965838168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.055787735875699414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.04381145129514615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.042500640457480456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0393440514970231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03828886884694372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03063010224108815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.029099386647725357}]
result = search.search('cherry apple peach lime blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #337 checking search results for 'cherry apple peach lime blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #337 checking search results for 'cherry apple peach lime blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking search results for 'cherry apple peach lime blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.895925292978774}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8504315654863159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8459198549041977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8276235271975062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7438716161018836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.713085519734289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.680707377604939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.662077361348143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6289905589257658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.35115115716819295}]
result = search.search('cherry apple peach lime blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #338 checking search results for 'cherry apple peach lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #338 checking search results for 'cherry apple peach lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking search results for 'pear tomato peach kiwi cherry apricot apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3127503855662967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10510029036651272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08191354076874838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.04586567018404988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.045467288550657875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037411236382729744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.03703295495584969}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.030154397790428073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021949407447519186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021949407447519186}]
result = search.search('pear tomato peach kiwi cherry apricot apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #339 checking search results for 'pear tomato peach kiwi cherry apricot apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #339 checking search results for 'pear tomato peach kiwi cherry apricot apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking search results for 'pear tomato peach kiwi cherry apricot apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9699854172358735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9584630579026692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8802867861417208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8086532808180864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6885466390577569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6517948900395065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5596409243537205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.4744419607752676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.4744419607752676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2968211415435331}]
result = search.search('pear tomato peach kiwi cherry apricot apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #340 checking search results for 'pear tomato peach kiwi cherry apricot apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #340 checking search results for 'pear tomato peach kiwi cherry apricot apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking search results for 'orange tomato papaya blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2848440328131797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11415829675686469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07558698914880897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06823094668999653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.041908117652922176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039659913484510936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.03895166795455801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029252921906004283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02919422156595541}]
result = search.search('orange tomato papaya blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #341 checking search results for 'orange tomato papaya blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #341 checking search results for 'orange tomato papaya blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking search results for 'orange tomato papaya blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9595887421641761}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8834347478585992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8572590017638743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8419500965579089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8325361849481518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6330927109706134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6323092621372379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.6310404395279009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}]
result = search.search('orange tomato papaya blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #342 checking search results for 'orange tomato papaya blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #342 checking search results for 'orange tomato papaya blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking search results for 'papaya banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('papaya banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #343 checking search results for 'papaya banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #343 checking search results for 'papaya banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking search results for 'papaya banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('papaya banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #344 checking search results for 'papaya banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #344 checking search results for 'papaya banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking search results for 'apricot lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('apricot lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #345 checking search results for 'apricot lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #345 checking search results for 'apricot lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking search results for 'apricot lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('apricot lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #346 checking search results for 'apricot lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #346 checking search results for 'apricot lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking search results for 'cherry papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10323393269715217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.05795131306428325}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04657076288956151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.046263630248160374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.044125586250235015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03271332667078128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #347 checking search results for 'cherry papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #347 checking search results for 'cherry papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking search results for 'cherry papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9817246031343432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.9537856414108279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8677610164113153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7071067811865476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #348 checking search results for 'cherry papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #348 checking search results for 'cherry papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking search results for 'fig apple orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2448445026231632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11442502635135396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0913222666296729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04469028223388571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04262928335067211}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.030457382201234822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02325017460443226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.023191016289590638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.02246644078237389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig apple orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #349 checking search results for 'fig apple orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #349 checking search results for 'fig apple orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking search results for 'fig apple orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9659916870804314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9618308106195163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9214426780174094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.7648864176708882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.75937747160505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.502558369927245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5012796480776129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.47359880518214326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3716330200800424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig apple orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #350 checking search results for 'fig apple orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #350 checking search results for 'fig apple orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking search results for 'papaya banana banana kiwi lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3057336113016535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10179046107995554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07911422423869517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07732934512654413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04624015746212293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03065593376937129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.02917338414622766}]
result = search.search('papaya banana banana kiwi lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #351 checking search results for 'papaya banana banana kiwi lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #351 checking search results for 'papaya banana banana kiwi lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking search results for 'papaya banana banana kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9747553489948765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9482231140482502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9435524655505154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.855627521493767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6305900334612784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}]
result = search.search('papaya banana banana kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #352 checking search results for 'papaya banana banana kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #352 checking search results for 'papaya banana banana kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking search results for 'fig cherry banana orange fig papaya cherry orange' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29721053691931265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10094383004019648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07969554781648377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.044255882645926614}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037208190420459954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03117507437613772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.029511970073533397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.025595002529124163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.022425214979129124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig cherry banana orange fig papaya cherry orange',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #353 checking search results for 'fig cherry banana orange fig papaya cherry orange' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #353 checking search results for 'fig cherry banana orange fig papaya cherry orange' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking search results for 'fig cherry banana orange fig papaya cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9566020307644667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9217890687443003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8485109330582383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8042643912912456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6675046987265912}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.6571792176171843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6379086534115406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5532424150857017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.2736266141841987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig cherry banana orange fig papaya cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #354 checking search results for 'fig cherry banana orange fig papaya cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #354 checking search results for 'fig cherry banana orange fig papaya cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking search results for 'cherry cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #355 checking search results for 'cherry cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #355 checking search results for 'cherry cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking search results for 'cherry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #356 checking search results for 'cherry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #356 checking search results for 'cherry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking search results for 'kiwi apricot blueberry blueberry banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26484077451699106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.11943013421263399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11937687857095088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.10486066583558598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0784510323568025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04504084256208881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04428535115850275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.022405085093549857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('kiwi apricot blueberry blueberry banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #357 checking search results for 'kiwi apricot blueberry blueberry banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #357 checking search results for 'kiwi apricot blueberry blueberry banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking search results for 'kiwi apricot blueberry blueberry banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9998629728841881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9735691367168451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9572390000731454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.9572390000731454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9572390000731453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8814349660977854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8213952756789797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.47230541023811695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('kiwi apricot blueberry blueberry banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #358 checking search results for 'kiwi apricot blueberry blueberry banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #358 checking search results for 'kiwi apricot blueberry blueberry banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking search results for 'blueberry banana coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.28239779793678677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11360229097697762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0724023655368019}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.06802182654871261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04087089852330702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04061991701772503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.037764002267142126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021677018651928115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.021677018651928115}]
result = search.search('blueberry banana coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #359 checking search results for 'blueberry banana coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #359 checking search results for 'blueberry banana coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking search results for 'blueberry banana coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9514968538500183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8834347478585992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8834347478585991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8758478278522864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8562791210473024}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.8162784041065125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.5717760410932535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.46855420847113666}]
result = search.search('blueberry banana coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #360 checking search results for 'blueberry banana coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #360 checking search results for 'blueberry banana coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking search results for 'cherry tomato tomato lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.30529974367124346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1059048539675116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.06332352738342649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04683681160418475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.045703366332529576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.043467398059126916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.039220518894086606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02453720402607222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('cherry tomato tomato lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #361 checking search results for 'cherry tomato tomato lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #361 checking search results for 'cherry tomato tomato lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking search results for 'cherry tomato tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9878897545950133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9873329838558977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9468774873314472}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.8902121746280713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.8477613772137169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.5303778344771792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('cherry tomato tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #362 checking search results for 'cherry tomato tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #362 checking search results for 'cherry tomato tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking search results for 'apricot apple papaya kiwi kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26767414350879837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.08727241778408883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.08351475376237455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.08061294902529417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06606294528459009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.035282042523112685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03445650623770964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.033061808030047456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03306180803004745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03236109289753344}]
result = search.search('apricot apple papaya kiwi kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #363 checking search results for 'apricot apple papaya kiwi kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #363 checking search results for 'apricot apple papaya kiwi kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking search results for 'apricot apple papaya kiwi kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8301828798852064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.8060827982287802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7626302201936617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.726352711718054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7146392933866691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.714639293386669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.6994931596147331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6994931596147331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6994931596147331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6776141599421268}]
result = search.search('apricot apple papaya kiwi kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #364 checking search results for 'apricot apple papaya kiwi kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #364 checking search results for 'apricot apple papaya kiwi kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking search results for 'blueberry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.12476521976591842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.0}]
result = search.search('blueberry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #365 checking search results for 'blueberry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #365 checking search results for 'blueberry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking search results for 'blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0}]
result = search.search('blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #366 checking search results for 'blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #366 checking search results for 'blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking search results for 'cherry banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.0}]
result = search.search('cherry banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #367 checking search results for 'cherry banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #367 checking search results for 'cherry banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking search results for 'cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0}]
result = search.search('cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #368 checking search results for 'cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #368 checking search results for 'cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking search results for 'blueberry lime papaya' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.3063711312724565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.1087091363959708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.07732934512654413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07534196181460875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.05845926879214732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.041908117652922176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.034648769220080824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03065593376937129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029252921906004283}]
result = search.search('blueberry lime papaya',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #369 checking search results for 'blueberry lime papaya' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #369 checking search results for 'blueberry lime papaya' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking search results for 'blueberry lime papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.950200362049898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.9435524655505154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9137843364826712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8834347478585993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.7489418585230587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.662635716326872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6323092621372379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6310404395279009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.46855420847113666}]
result = search.search('blueberry lime papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #370 checking search results for 'blueberry lime papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #370 checking search results for 'blueberry lime papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking search results for 'pear tomato fig peach apricot cherry coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2991573297850459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10981616258976475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.0884424690292897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.03934102082949171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.03814741085972875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03577977643018998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0321611246859116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.021415046942167025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.02040943135240543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('pear tomato fig peach apricot cherry coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #371 checking search results for 'pear tomato fig peach apricot cherry coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #371 checking search results for 'pear tomato fig peach apricot cherry coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking search results for 'pear tomato fig peach apricot cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9278269851699533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9197854401300664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8503660568456163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8041580052205703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.7733888637416804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7434273287246361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.46289162409641593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.44115499027915117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.39242164074467173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('pear tomato fig peach apricot cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #372 checking search results for 'pear tomato fig peach apricot cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #372 checking search results for 'pear tomato fig peach apricot cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking search results for 'pear cherry kiwi coconut pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26039542763877244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10941067536063764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07771551767963322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.046931761669429445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04230055899671953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.02635951813990416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.01900673154088819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01842885163086421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017563462890346927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.017314988584217688}]
result = search.search('pear cherry kiwi coconut pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #373 checking search results for 'pear cherry kiwi coconut pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #373 checking search results for 'pear cherry kiwi coconut pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking search results for 'pear cherry kiwi coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.9893345575758941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9163892073651041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.914337218454697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8076081731031685}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6532590094232692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.41083528116870976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.39834426161567854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3796386664024344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.2112729668521345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.2112729668521345}]
result = search.search('pear cherry kiwi coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #374 checking search results for 'pear cherry kiwi coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #374 checking search results for 'pear cherry kiwi coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking search results for 'fig cherry banana coconut cherry' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2668916789598399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11226626512978578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.07715864977623256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.043830815907776585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038122799628685276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.03627770701012459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.031976240674879745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.02739817145270039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig cherry banana coconut cherry',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #375 checking search results for 'fig cherry banana coconut cherry' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #375 checking search results for 'fig cherry banana coconut cherry' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking search results for 'fig cherry banana coconut cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9474141063437078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9436847535734011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.827756090864245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8036391936415953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.7841517584229598}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.6911744820576688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.6462564432285882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.5922183647442983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig cherry banana coconut cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #376 checking search results for 'fig cherry banana coconut cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #376 checking search results for 'fig cherry banana coconut cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking search results for 'lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #377 checking search results for 'lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #377 checking search results for 'lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking search results for 'lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #378 checking search results for 'lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #378 checking search results for 'lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking search results for 'tomato peach lime coconut kiwi papaya blueberry kiwi' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.29409235834022646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.09590795067990154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.07465877756048754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07329043687397245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.06317454070218485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.038196259200240334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.037012429694139454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.03188209857564109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02474663362491892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.024304708993563465}]
result = search.search('tomato peach lime coconut kiwi papaya blueberry kiwi',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #379 checking search results for 'tomato peach lime coconut kiwi papaya blueberry kiwi' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #379 checking search results for 'tomato peach lime coconut kiwi papaya blueberry kiwi' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking search results for 'tomato peach lime coconut kiwi papaya blueberry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9121181366219488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.8051877417919086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.803294656703911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.8000329739711945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.7708392401619686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6891395769122302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6160627841386316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.5983941494317133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.5349047079136845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.525352395892666}]
result = search.search('tomato peach lime coconut kiwi papaya blueberry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #380 checking search results for 'tomato peach lime coconut kiwi papaya blueberry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #380 checking search results for 'tomato peach lime coconut kiwi papaya blueberry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking search results for 'fig banana cherry apricot fig coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.26187644055913295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11033018083995978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.07920842655763134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04465945247506257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04232509033636845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.018910562832313127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.018679138410450023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.017801996611994435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('fig banana cherry apricot fig coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #381 checking search results for 'fig banana cherry apricot fig coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #381 checking search results for 'fig banana cherry apricot fig coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking search results for 'fig banana cherry apricot fig coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.965325294091862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9240906943962958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.9148674695291874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8122014877777016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.6658080627387288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.40375427328668795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.3986399113887152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.3847946327710052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('fig banana cherry apricot fig coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #382 checking search results for 'fig banana cherry apricot fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #382 checking search results for 'fig banana cherry apricot fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking search results for 'banana fig apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2637331451968811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11393409412947837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10940992436469393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.0447212047461541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04239520044987674}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.032807031059864405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.01898944747600852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.01851946172417734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('banana fig apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #383 checking search results for 'banana fig apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #383 checking search results for 'banana fig apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking search results for 'banana fig apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.966660084958041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.9577041457457331}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.9163829172606391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.8179599984170056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.40030282156497543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('banana fig apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #384 checking search results for 'banana fig apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #384 checking search results for 'banana fig apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking search results for 'lime apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.32242792521306995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.11939323868209492}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.11896585666418055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.0819555328928385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.047437705789256435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.04626363024816037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.0}]
result = search.search('lime apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #385 checking search results for 'lime apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #385 checking search results for 'lime apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking search results for 'lime apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0}]
result = search.search('lime apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #386 checking search results for 'lime apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #386 checking search results for 'lime apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking search results for 'apricot cherry apricot pear lime coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.2915601708310885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.10264858221954679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.09368422435998658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.04525489757501423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.035695408801573104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.029904784420136686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.02787031385110578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.026561569481975557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.026185796914347973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0.0}]
result = search.search('apricot cherry apricot pear lime coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #387 checking search results for 'apricot cherry apricot pear lime coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #387 checking search results for 'apricot cherry apricot pear lime coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking search results for 'apricot cherry apricot pear lime coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-9.html', 'title': 'N-9', 'score': 0.953985797206564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-0.html', 'title': 'N-0', 'score': 0.9042646372469657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-7.html', 'title': 'N-7', 'score': 0.8597520542420859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-4.html', 'title': 'N-4', 'score': 0.7874883347786119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-6.html', 'title': 'N-6', 'score': 0.7715652362363522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-1.html', 'title': 'N-1', 'score': 0.6463994342797131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-5.html', 'title': 'N-5', 'score': 0.6024238413978337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-2.html', 'title': 'N-2', 'score': 0.5741350027980512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-3.html', 'title': 'N-3', 'score': 0.3195122524380067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N-8.html', 'title': 'N-8', 'score': 0}]
result = search.search('apricot cherry apricot pear lime coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #388 checking search results for 'apricot cherry apricot pear lime coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #388 checking search results for 'apricot cherry apricot pear lime coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
