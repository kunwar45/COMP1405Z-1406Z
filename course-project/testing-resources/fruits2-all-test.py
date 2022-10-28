
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')


output = open('fruits2-all-outgoing-failed.txt', 'w')
success_output = open('fruits2-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-624.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-813.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-601.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-517.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-517.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-517.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-517.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-688.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-688.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-688.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-688.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-66.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-295.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-93.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-295.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-295.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-295.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-42.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-300.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-42.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-42.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-42.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-47.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-757.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-900.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-209.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-303.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-261.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-120.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-105.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-120.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-120.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-120.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-90.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-784.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-945.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-90.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-90.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-90.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-514.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-217.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-445.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-514.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-514.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-514.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-824.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-513.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-938.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-824.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-824.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-824.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-739.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-186.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-739.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-739.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-739.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-914.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-32.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-914.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-914.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-914.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-622.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-818.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-115.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-251.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-901.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-901.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-901.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-901.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-171.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-123.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-992.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-203.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-171.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-171.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-171.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-209.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-375.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-322.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-841.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-209.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-209.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-209.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-414.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-414.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-414.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-414.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-808.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-711.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-864.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-808.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-808.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-808.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-668.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-56.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-27.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-764.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-213.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-27.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-668.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-365.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-668.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-668.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-668.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-827.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-827.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-827.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-827.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-839.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-861.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-608.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-710.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-175.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-158.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-483.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-20.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-175.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-175.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-175.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-536.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-169.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-536.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-536.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-536.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-793.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-116.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-624.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-804.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-793.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-793.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-793.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-482.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-156.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-482.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-482.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-482.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-967.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-968.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-965.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-968.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-968.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-968.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-439.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-511.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-757.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-288.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-593.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-751.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-754.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-288.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-288.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-288.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-716.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-539.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-716.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-716.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-716.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-125.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-585.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-479.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-585.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-585.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-585.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-90.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-55.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-55.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-55.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-55.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-443.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-173.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-137.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-976.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-443.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-443.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-443.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-851.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-491.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-689.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-675.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-68.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-228.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-632.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-990.html\n\n')
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









output = open('fruits2-all-incoming-failed.txt', 'w')
success_output = open('fruits2-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-240.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-291.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-441.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-317.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-615.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-441.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-441.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-441.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-452.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-668.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-573.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-249.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-661.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-623.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-984.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-512.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-315.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-513.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-106.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-520.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-315.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-315.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-315.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-49.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-49.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-49.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-49.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-814.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-814.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-814.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-814.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-410.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-926.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-410.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-410.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-410.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-126.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-411.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-652.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-54.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-652.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-652.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-652.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-31.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-77.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-92.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-167.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-171.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-179.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-219.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-264.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-268.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-339.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-355.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-364.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-486.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-522.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-570.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-578.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-581.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-641.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-681.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-857.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-78.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-131.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-194.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-216.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-262.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-263.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-359.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-372.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-469.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-479.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-531.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-550.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-603.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-637.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-654.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-711.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-774.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-889.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-928.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-984.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-676.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-676.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-676.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-676.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-280.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-70.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-280.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-280.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-280.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-505.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-494.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-505.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-505.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-505.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-685.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-265.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-685.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-685.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-685.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-767.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-767.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-767.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-767.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-675.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-817.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-323.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-954.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-758.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-323.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-323.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-323.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-382.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-69.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-382.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-382.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-382.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-313.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-112.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-172.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-370.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-736.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-289.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-397.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-426.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-490.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-804.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-793.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-804.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-804.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-804.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-406.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-556.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-977.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-406.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-406.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-406.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-32.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-350.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-601.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-350.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-350.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-350.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-812.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-812.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-812.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-812.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-539.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-29.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-716.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-539.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-539.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-539.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-592.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-674.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-71.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-119.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-506.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-471.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-396.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-506.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-506.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-506.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-842.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-226.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-842.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-842.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-842.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-697.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-453.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-359.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-246.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-453.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-453.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-453.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-410.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-743.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-955.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-527.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-609.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-287.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-883.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-323.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-425.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-235.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-108.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-425.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-425.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-425.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-726.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-439.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-726.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-715.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-483.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-589.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-590.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-191.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-742.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-130.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-742.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-742.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-742.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-835.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-545.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-835.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-835.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-835.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-792.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-167.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-792.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-792.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-792.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-647.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-298.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-647.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-647.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-647.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-371.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-146.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-371.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-371.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-371.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-991.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-390.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-147.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-390.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-390.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-390.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-516.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-83.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-516.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-516.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-516.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-111.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-699.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-496.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-349.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-215.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-235.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-404.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-915.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-81.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-85.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-116.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-136.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-182.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-332.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-421.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-768.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-849.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-710.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-522.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-419.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-710.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-710.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-710.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #101 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #101 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #101 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits2-all-pagerank-failed.txt', 'w')
success_output = open('fruits2-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-400.html
expected = 0.0003748366270339644
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-400.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-400.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-400.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-89.html
expected = 0.0010968544706070429
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-89.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-89.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-89.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html
expected = 0.0003786226087730779
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-491.html
expected = 0.0004266412974492515
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-491.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-491.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-491.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-502.html
expected = 0.00064393940289557
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-502.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-502.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-502.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html
expected = 0.0011868850274089665
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-497.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-257.html
expected = 0.0011096996318792093
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-257.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-257.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-257.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html
expected = 0.00037830071395642147
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-994.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-150.html
expected = 0.0011165369687464956
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-150.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-150.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-150.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-535.html
expected = 0.0014575226073128018
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-535.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-535.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-535.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html
expected = 0.0011165864028038171
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-529.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-472.html
expected = 0.0003749278535784899
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-472.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-472.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-472.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html
expected = 0.00039763345355417235
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-417.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-667.html
expected = 0.0006300901017780141
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-667.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-667.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-667.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-24.html
expected = 0.0006227037774053016
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-24.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html
expected = 0.0009238462333662126
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-344.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-652.html
expected = 0.0003829558728691483
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-652.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-652.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-652.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html
expected = 0.002571518197319439
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html
expected = 0.0011414987726504299
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html
expected = 0.002058502782891891
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-327.html
expected = 0.000871544920345315
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-327.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-327.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-327.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html
expected = 0.00034895412080068175
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-242.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-571.html
expected = 0.00035967504858809373
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-571.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-571.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-571.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html
expected = 0.012157553824837401
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html
expected = 0.0017761158566589523
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-866.html
expected = 0.0003761660569363582
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-866.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-866.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-866.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html
expected = 0.0006237444462155389
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-999.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-597.html
expected = 0.00042255834165817627
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-597.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-597.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-597.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html
expected = 0.000646290037530551
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-822.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-333.html
expected = 0.0006276418142137009
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-333.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-333.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-333.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-625.html
expected = 0.0006144458963882766
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-625.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-625.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-625.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-203.html
expected = 0.0006227154892000595
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-203.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-203.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-203.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html
expected = 0.0008746094766965241
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-841.html
expected = 0.0007070318929365689
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-841.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-841.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-841.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html
expected = 0.0003660688980857633
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html
expected = 0.0006299055779160687
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-989.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-302.html
expected = 0.00035261020331693165
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-302.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-302.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-302.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-394.html
expected = 0.0011948559443639723
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-394.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-394.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-394.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-318.html
expected = 0.0003650790245833138
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-318.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-318.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-318.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-427.html
expected = 0.0005863492442704736
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-427.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-427.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-427.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-951.html
expected = 0.0008495610978004413
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-951.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-951.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-951.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html
expected = 0.000881003938222159
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-655.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-392.html
expected = 0.0013089213071758113
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-392.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-392.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-392.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html
expected = 0.0006826800805480646
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-949.html
expected = 0.00044273201517214115
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-949.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-949.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-949.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-153.html
expected = 0.00038139587771821167
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-153.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-153.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-153.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html
expected = 0.000628483968658533
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html
expected = 0.0011371238625572295
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html
expected = 0.0014051467029994212
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-875.html
expected = 0.0003729195661541804
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-875.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-875.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-875.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #152 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = -1
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #152 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #152 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits2-all-idf-failed.txt', 'w')
success_output = open('fruits2-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word banana
expected = 0.052894948432125555
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word peach
expected = 0.05139915250664415
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word coconut
expected = 0.05739166388833648
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word apple
expected = 0.05439229681862769
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word pear
expected = 0.052894948432125555
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits2-all-tf-failed.txt', 'w')
success_output = open('fruits2-all-tf-passed.txt', 'w')

#Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word peach
expected = 0.15789473684210525
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word coconut
expected = 0.23157894736842105
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word apple
expected = 0.21052631578947367
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word banana
expected = 0.17894736842105263
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word pear
expected = 0.22105263157894736
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-13.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word peach
expected = 0.19753086419753085
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word coconut
expected = 0.2716049382716049
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word apple
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word banana
expected = 0.20987654320987653
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word pear
expected = 0.20987654320987653
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-76.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word peach
expected = 0.21176470588235294
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word coconut
expected = 0.2235294117647059
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word apple
expected = 0.21176470588235294
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word banana
expected = 0.17647058823529413
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word pear
expected = 0.17647058823529413
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-653.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word peach
expected = 0.1891891891891892
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word coconut
expected = 0.16216216216216217
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word apple
expected = 0.2702702702702703
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word banana
expected = 0.16216216216216217
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word pear
expected = 0.21621621621621623
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-696.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word peach
expected = 0.23076923076923078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word coconut
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word apple
expected = 0.23076923076923078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word banana
expected = 0.23076923076923078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word pear
expected = 0.23076923076923078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-340.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word peach
expected = 0.24390243902439024
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word coconut
expected = 0.10975609756097561
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word apple
expected = 0.2804878048780488
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word banana
expected = 0.15853658536585366
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word pear
expected = 0.2073170731707317
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word peach
expected = 0.2608695652173913
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word coconut
expected = 0.2826086956521739
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word apple
expected = 0.15217391304347827
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word banana
expected = 0.15217391304347827
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word pear
expected = 0.15217391304347827
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-878.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word peach
expected = 0.14516129032258066
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word coconut
expected = 0.12903225806451613
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word apple
expected = 0.25806451612903225
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word banana
expected = 0.24193548387096775
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word pear
expected = 0.22580645161290322
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-790.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word peach
expected = 0.19402985074626866
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word coconut
expected = 0.11940298507462686
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word apple
expected = 0.26865671641791045
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word banana
expected = 0.16417910447761194
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word pear
expected = 0.2537313432835821
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-285.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word peach
expected = 0.12987012987012986
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word coconut
expected = 0.2077922077922078
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word apple
expected = 0.23376623376623376
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word banana
expected = 0.18181818181818182
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word pear
expected = 0.24675324675324675
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-57.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits2-all-tfidf-failed.txt', 'w')
success_output = open('fruits2-all-tfidf-passed.txt', 'w')

#Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word banana
expected = 0.010765888384348554
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word peach
expected = 0.011751099119826433
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word apple
expected = 0.01954467885880517
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word pear
expected = 0.01594151750971492
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word coconut
expected = 0.012404257219223634
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-645.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word banana
expected = 0.01595606268840969
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word peach
expected = 0.015504847321659214
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word apple
expected = 0.014913005991610167
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word pear
expected = 0.008394309091972644
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word coconut
expected = 0.015735357348287696
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-828.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word banana
expected = 0.018039130182336903
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word peach
expected = 0.013519745539945695
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word apple
expected = 0.016457083993217488
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word pear
expected = 0.011763435658286957
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word coconut
expected = 0.010363341629437514
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-481.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word banana
expected = 0.021953387121752786
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word peach
expected = 0.011430781980593952
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word apple
expected = 0.008267797376012765
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word pear
expected = 0.018705608478038503
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word coconut
expected = 0.008723710448985716
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word banana
expected = 0.007273241797988364
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word peach
expected = 0.019455176649155893
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word apple
expected = 0.014307045475623087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word pear
expected = 0.020021352792966175
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word coconut
expected = 0.007891556018518164
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word banana
expected = 0.017591555410796707
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word peach
expected = 0.010244303829792372
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word apple
expected = 0.018089536558168837
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word pear
expected = 0.014148357249812348
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word coconut
expected = 0.010092314648062671
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-937.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word banana
expected = 0.012677354124084602
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word peach
expected = 0.01528538377351956
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word apple
expected = 0.016175502720369543
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word pear
expected = 0.014978371056479806
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word coconut
expected = 0.011180824549477728
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-221.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word banana
expected = 0.026579729599416683
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word peach
expected = 0.021332575721409498
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word apple
expected = 0.006281071085694357
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word pear
expected = 0.00610816146051286
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word coconut
expected = 0.006627429648925315
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-815.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word banana
expected = 0.015313437587287848
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word peach
expected = 0.014880394768887683
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word apple
expected = 0.017160868951812486
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word pear
expected = 0.011033178604346194
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word coconut
expected = 0.011971133290604417
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-778.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word banana
expected = 0.017591555410796707
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word peach
expected = 0.011430781980593952
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word apple
expected = 0.013332231736279853
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word pear
expected = 0.018705608478038503
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word coconut
expected = 0.008723710448985716
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-430.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits2-all-search-failed.txt', 'w')
success_output = open('fruits2-all-search-passed.txt', 'w')

#Test #291 checking search results for 'apple tomato tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple tomato tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #291 checking search results for 'apple tomato tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #291 checking search results for 'apple tomato tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #292 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #292 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking search results for 'tomato pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #293 checking search results for 'tomato pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #293 checking search results for 'tomato pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking search results for 'banana banana coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015362665178199635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01146914307980713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010746420407149923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.0100573419719032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009873754641891741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009154489598971652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00845356899823729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007636719996122505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007528981515842861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007398598737202903}]
result = search.search('banana banana coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #294 checking search results for 'banana banana coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #294 checking search results for 'banana banana coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking search results for 'apple tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #295 checking search results for 'apple tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #295 checking search results for 'apple tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking search results for 'apple banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015469688248481307}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01175101558301189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.011293518586939718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010799446051210047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010478821573120606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009232769545516419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008304121444387377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007779022748677028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0076001029823598515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007416838162734326}]
result = search.search('apple banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #296 checking search results for 'apple banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #296 checking search results for 'apple banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking search results for 'pear banana apple banana banana peach tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013335219227797934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010814963451442583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009910633105197316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.008975827370466635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.008874044207111189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.008480841859035079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.007662289637450225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007244468435873604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007156335663205789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.006669762846032216}]
result = search.search('pear banana apple banana banana peach tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #297 checking search results for 'pear banana apple banana banana peach tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #297 checking search results for 'pear banana apple banana banana peach tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking search results for 'pear banana apple banana banana peach tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 0.9999828769818828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-553.html', 'title': 'N-553', 'score': 0.9898597180625505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-258.html', 'title': 'N-258', 'score': 0.9853128842255409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.9788507530787768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html', 'title': 'N-987', 'score': 0.9786726745165403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-921.html', 'title': 'N-921', 'score': 0.9693057437032044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html', 'title': 'N-745', 'score': 0.9679174450680779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-579.html', 'title': 'N-579', 'score': 0.9676936991717747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html', 'title': 'N-52', 'score': 0.9668539114874298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html', 'title': 'N-848', 'score': 0.966312828257309}]
result = search.search('pear banana apple banana banana peach tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #298 checking search results for 'pear banana apple banana banana peach tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #298 checking search results for 'pear banana apple banana banana peach tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking search results for 'tomato pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #299 checking search results for 'tomato pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #299 checking search results for 'tomato pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #300 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #300 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking search results for 'apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01760043385328955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012113974494578992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012090788373318907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735556738228342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001729294882303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049859168975073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009027256499602359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007793463871817541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007253331382606732}]
result = search.search('apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #301 checking search results for 'apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #301 checking search results for 'apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #302 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #302 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #303 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #303 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking search results for 'peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016095350631103317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01173849251039794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01173717685922528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010985216997917413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010879474014584126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129116652445442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851592713703313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007840601893309988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074259064541596365}]
result = search.search('peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #304 checking search results for 'peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #304 checking search results for 'peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #305 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #305 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking search results for 'banana peach coconut banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014442063575175131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011380613796411154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010613450995047555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009998895767511494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009910883975866699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009212029767457474}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008469172560893653}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0077532272584716275}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.00742041998079044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074018910149271115}]
result = search.search('banana peach coconut banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #306 checking search results for 'banana peach coconut banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #306 checking search results for 'banana peach coconut banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking search results for 'banana banana coconut apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015362665178199635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01146914307980713}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010746420407149923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.0100573419719032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009873754641891741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009154489598971652}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00845356899823729}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007636719996122505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007528981515842861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007398598737202903}]
result = search.search('banana banana coconut apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #307 checking search results for 'banana banana coconut apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #307 checking search results for 'banana banana coconut apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #308 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #308 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking search results for 'tomato coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #309 checking search results for 'tomato coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #309 checking search results for 'tomato coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking search results for 'banana banana banana peach tomato apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016500783350252353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.0119643582211146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01129724413122731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010006895351866172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009610737768632248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009341038034480473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00814636042357743}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0076172928493209845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007486363136408518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007315165345137375}]
result = search.search('banana banana banana peach tomato apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #310 checking search results for 'banana banana banana peach tomato apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #310 checking search results for 'banana banana banana peach tomato apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking search results for 'banana coconut peach apple tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999853793572516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9988139564073509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9979335266663844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9975486973349208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9973792225348946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9966996028040428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9951978818597593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9947811452816204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9945441699689879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9930458995580927}]
result = search.search('banana coconut peach apple tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #311 checking search results for 'banana coconut peach apple tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #311 checking search results for 'banana coconut peach apple tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking search results for 'banana pear peach banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013659477198988298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01190398602483238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011148682752543618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009683667723976191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009378984336101005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009310223928645243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008209826859876814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007767992641824041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007336096415653684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0071796073325493}]
result = search.search('banana pear peach banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #312 checking search results for 'banana pear peach banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #312 checking search results for 'banana pear peach banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking search results for 'tomato banana apple peach banana coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014977572438480377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011426731053059807}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.01061642746270035}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010115424359019702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010105272707649004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009257201391139327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00837833673191208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007646898396919042}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007455988254653161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007394704644932692}]
result = search.search('tomato banana apple peach banana coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #313 checking search results for 'tomato banana apple peach banana coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #313 checking search results for 'tomato banana apple peach banana coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking search results for 'apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #314 checking search results for 'apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #314 checking search results for 'apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking search results for 'apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #315 checking search results for 'apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #315 checking search results for 'apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking search results for 'apple tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016095350631103317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01173849251039794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01173717685922528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010985216997917413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010879474014584126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129116652445442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851592713703313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007840601893309988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074259064541596365}]
result = search.search('apple tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #316 checking search results for 'apple tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #316 checking search results for 'apple tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking search results for 'tomato banana pear peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013659477198988298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01190398602483238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011148682752543618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009683667723976191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009378984336101005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009310223928645243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008209826859876814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007767992641824041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007336096415653684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0071796073325493}]
result = search.search('tomato banana pear peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #317 checking search results for 'tomato banana pear peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #317 checking search results for 'tomato banana pear peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #318 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #318 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #319 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #319 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking search results for 'pear banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014006752809758789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011913259691201767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011186445044977313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009237724172640403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009219595726754608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009098134469424913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.00821381467307448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007886367966105397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007316573562484619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.00708349220129616}]
result = search.search('pear banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #320 checking search results for 'pear banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #320 checking search results for 'pear banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking search results for 'apple apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('apple apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #321 checking search results for 'apple apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #321 checking search results for 'apple apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #322 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #322 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking search results for 'banana tomato banana coconut coconut banana banana banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013713295218368407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010986558884269958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010186453352140112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009424368646856893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.008797357021666811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008786382942531003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.008618805163773002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.0077365773766004875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007637061805225448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.00732343677510986}]
result = search.search('banana tomato banana coconut coconut banana banana banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #323 checking search results for 'banana tomato banana coconut coconut banana banana banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #323 checking search results for 'banana tomato banana coconut coconut banana banana banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking search results for 'banana apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01760043385328955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012113974494578992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012090788373318907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735556738228342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001729294882303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049859168975073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009027256499602359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007793463871817541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007253331382606732}]
result = search.search('banana apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #324 checking search results for 'banana apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #324 checking search results for 'banana apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking search results for 'peach apple tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01291057910988265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012154340137223904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.01074390744827247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.010407501807318321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009427531794778257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009090330273899093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008766525989888417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007678487729455372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007296955306020476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.00706539602236865}]
result = search.search('peach apple tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #325 checking search results for 'peach apple tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #325 checking search results for 'peach apple tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking search results for 'banana tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.017600433853289552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012113974494578994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012090788373318907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735556738228344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001729294882301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049859168975075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009027256499602359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007793463871817541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007253331382606733}]
result = search.search('banana tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #326 checking search results for 'banana tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #326 checking search results for 'banana tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking search results for 'apple apple banana peach peach peach banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html', 'title': 'N-44', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-330.html', 'title': 'N-330', 'score': 0.999102880847251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html', 'title': 'N-679', 'score': 0.9958510579504222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-723.html', 'title': 'N-723', 'score': 0.994445220779916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html', 'title': 'N-782', 'score': 0.9932480726513316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-956.html', 'title': 'N-956', 'score': 0.9930021825644498}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-880.html', 'title': 'N-880', 'score': 0.9929181935697585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-996.html', 'title': 'N-996', 'score': 0.9919985229904246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9915381254099687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html', 'title': 'N-41', 'score': 0.9913236791669888}]
result = search.search('apple apple banana peach peach peach banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #327 checking search results for 'apple apple banana peach peach peach banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #327 checking search results for 'apple apple banana peach peach peach banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking search results for 'apple coconut banana banana tomato apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.015931524917465332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011390467664864649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011055842948100442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010011499693946706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009593550191740262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009401716730844984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009000934307512797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007790924825321829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007700506539548128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.00719129840846925}]
result = search.search('apple coconut banana banana tomato apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #328 checking search results for 'apple coconut banana banana tomato apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #328 checking search results for 'apple coconut banana banana tomato apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking search results for 'tomato banana coconut apple peach banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.014944555990656475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011414074772749114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010599837342918132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010097797448384134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.010080019644220744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.009239842207333043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008364799656816312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.0076390693439347575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007453660119053009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007391825684105912}]
result = search.search('tomato banana coconut apple peach banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #329 checking search results for 'tomato banana coconut apple peach banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #329 checking search results for 'tomato banana coconut apple peach banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking search results for 'peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #330 checking search results for 'peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #330 checking search results for 'peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #331 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #331 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking search results for 'apple banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01760043385328955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012113974494578992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012090788373318907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011735556738228342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011001729294882303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010049859168975073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009027256499602359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007793463871817541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007253331382606732}]
result = search.search('apple banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #332 checking search results for 'apple banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #332 checking search results for 'apple banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking search results for 'tomato tomato apple apple peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.016095350631103317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.01173849251039794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01173717685922528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010985216997917413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.010879474014584126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010129116652445442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007851592713703313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007840601893309988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074259064541596365}]
result = search.search('tomato tomato apple apple peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #333 checking search results for 'tomato tomato apple apple peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #333 checking search results for 'tomato tomato apple apple peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking search results for 'banana pear banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013716873586519336}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.011914959976089995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011167035081936918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.009737275597155278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.009418037712933848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00934004734065954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008239589770669228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007772965346398517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007332479304237139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007200403401611276}]
result = search.search('banana pear banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #334 checking search results for 'banana pear banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #334 checking search results for 'banana pear banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking search results for 'banana banana banana banana coconut peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.9998867153185582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-641.html', 'title': 'N-641', 'score': 0.9971813076115306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-286.html', 'title': 'N-286', 'score': 0.9970883128093038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-163.html', 'title': 'N-163', 'score': 0.9965006880403894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-253.html', 'title': 'N-253', 'score': 0.9956911122373441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 0.9956911122373441}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-280.html', 'title': 'N-280', 'score': 0.9937891212797554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html', 'title': 'N-745', 'score': 0.9923462537504403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-797.html', 'title': 'N-797', 'score': 0.991555768951656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-840.html', 'title': 'N-840', 'score': 0.9908188232349776}]
result = search.search('banana banana banana banana coconut peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #335 checking search results for 'banana banana banana banana coconut peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #335 checking search results for 'banana banana banana banana coconut peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #336 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #336 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking search results for 'peach peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.013042341815209949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012156540074991342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.010767583152410715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.01046954852010882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.00946578862315247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.009166928207624428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.008792094194808036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.00769503912580903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.00732698053044691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.007088168390198852}]
result = search.search('peach peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #337 checking search results for 'peach peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #337 checking search results for 'peach peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #338 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #338 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking search results for 'pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #339 checking search results for 'pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #339 checking search results for 'pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking search results for 'tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #340 checking search results for 'tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #340 checking search results for 'tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #341 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #341 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking search results for 'coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #342 checking search results for 'coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #342 checking search results for 'coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking search results for 'peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #343 checking search results for 'peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #343 checking search results for 'peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking search results for 'pear pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.01841964185256249}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.012157553824837401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'title': 'N-3', 'score': 0.012118562425919624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html', 'title': 'N-8', 'score': 0.011877960885945333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html', 'title': 'N-7', 'score': 0.011009379917772845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'title': 'N-11', 'score': 0.010180760971221083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.009138545567141276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html', 'title': 'N-23', 'score': 0.007895564703744208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.007860301659144963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'title': 'N-34', 'score': 0.0074287663514917245}]
result = search.search('pear pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #344 checking search results for 'pear pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #344 checking search results for 'pear pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking search results for 'pear banana peach peach peach peach banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-466.html', 'title': 'N-466', 'score': 0.9988409803446983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-1.html', 'title': 'N-1', 'score': 0.9972529631635483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-260.html', 'title': 'N-260', 'score': 0.991649710844636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9910108623963821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-883.html', 'title': 'N-883', 'score': 0.9905080610126058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'title': 'N-360', 'score': 0.9900303154466177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-320.html', 'title': 'N-320', 'score': 0.9899450687626874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html', 'title': 'N-873', 'score': 0.9880759382336571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9872742685265873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-978.html', 'title': 'N-978', 'score': 0.9845056936821379}]
result = search.search('pear banana peach peach peach peach banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #345 checking search results for 'pear banana peach peach peach peach banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #345 checking search results for 'pear banana peach peach peach peach banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking search results for 'tomato peach coconut banana pear pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-747.html', 'title': 'N-747', 'score': 0.998025629028374}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9977194699358839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-515.html', 'title': 'N-515', 'score': 0.9971167279856291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html', 'title': 'N-357', 'score': 0.9968251778598058}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9965624406700269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9964802475151553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-717.html', 'title': 'N-717', 'score': 0.9962422936362276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'title': 'N-786', 'score': 0.9961073050894469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9955183393635708}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'title': 'N-12', 'score': 0.9947017476742858}]
result = search.search('tomato peach coconut banana pear pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #346 checking search results for 'tomato peach coconut banana pear pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #346 checking search results for 'tomato peach coconut banana pear pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking search results for 'peach peach apple tomato banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999853793572516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.998813956407351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9979335266663842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9975486973349206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9973792225348946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9966996028040428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9951978818597591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9947811452816204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9945441699689876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9930458995580927}]
result = search.search('peach peach apple tomato banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #347 checking search results for 'peach peach apple tomato banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #347 checking search results for 'peach peach apple tomato banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking search results for 'peach coconut banana banana banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-830.html', 'title': 'N-830', 'score': 0.9999746211478052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-258.html', 'title': 'N-258', 'score': 0.997895623975584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html', 'title': 'N-718', 'score': 0.9929780441687001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-553.html', 'title': 'N-553', 'score': 0.9896722042903426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-987.html', 'title': 'N-987', 'score': 0.9884876225681929}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-293.html', 'title': 'N-293', 'score': 0.9871186285966823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'title': 'N-863', 'score': 0.98384659613367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-212.html', 'title': 'N-212', 'score': 0.9833543077614106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-130.html', 'title': 'N-130', 'score': 0.9830468397753673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-871.html', 'title': 'N-871', 'score': 0.9824037254326065}]
result = search.search('peach coconut banana banana banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #348 checking search results for 'peach coconut banana banana banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #348 checking search results for 'peach coconut banana banana banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking search results for 'peach tomato peach peach peach coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-279.html', 'title': 'N-279', 'score': 0.9998800374039924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html', 'title': 'N-290', 'score': 0.9996628362536101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html', 'title': 'N-297', 'score': 0.9966075962132837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html', 'title': 'N-752', 'score': 0.996583225047213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-847.html', 'title': 'N-847', 'score': 0.9947220292396302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-431.html', 'title': 'N-431', 'score': 0.9926727265403378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html', 'title': 'N-145', 'score': 0.9919437636856782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-768.html', 'title': 'N-768', 'score': 0.989512020386878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-647.html', 'title': 'N-647', 'score': 0.9881579245846205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-970.html', 'title': 'N-970', 'score': 0.9881219618771659}]
result = search.search('peach tomato peach peach peach coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #349 checking search results for 'peach tomato peach peach peach coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #349 checking search results for 'peach tomato peach peach peach coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking search results for 'pear pear coconut tomato apple peach pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-745.html', 'title': 'N-745', 'score': 0.9999104395398599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9987187947945673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-718.html', 'title': 'N-718', 'score': 0.9963806543536095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-38.html', 'title': 'N-38', 'score': 0.9958163556517496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-26.html', 'title': 'N-26', 'score': 0.9957947221616903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-556.html', 'title': 'N-556', 'score': 0.9949285666126861}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html', 'title': 'N-159', 'score': 0.994618823207003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9939000098504975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9930514972591891}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'title': 'N-5', 'score': 0.9928554259113459}]
result = search.search('pear pear coconut tomato apple peach pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #350 checking search results for 'pear pear coconut tomato apple peach pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #350 checking search results for 'pear pear coconut tomato apple peach pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking search results for 'banana coconut banana coconut tomato pear apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-307.html', 'title': 'N-307', 'score': 0.9999976846755828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-248.html', 'title': 'N-248', 'score': 0.9996572993417292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'title': 'N-458', 'score': 0.9986951646134814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-453.html', 'title': 'N-453', 'score': 0.9979237715504982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-488.html', 'title': 'N-488', 'score': 0.9972250682755449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-252.html', 'title': 'N-252', 'score': 0.9969831928190231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-256.html', 'title': 'N-256', 'score': 0.9969367440321153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-532.html', 'title': 'N-532', 'score': 0.9965236020935934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-381.html', 'title': 'N-381', 'score': 0.9961773180235887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-89.html', 'title': 'N-89', 'score': 0.9949857178251043}]
result = search.search('banana coconut banana coconut tomato pear apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #351 checking search results for 'banana coconut banana coconut tomato pear apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #351 checking search results for 'banana coconut banana coconut tomato pear apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking search results for 'pear peach banana apple peach pear pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'title': 'N-16', 'score': 0.9978514306002156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-768.html', 'title': 'N-768', 'score': 0.9975717358736633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-627.html', 'title': 'N-627', 'score': 0.9972141084674074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-281.html', 'title': 'N-281', 'score': 0.996993827564937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html', 'title': 'N-159', 'score': 0.9963977485486718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-272.html', 'title': 'N-272', 'score': 0.9947425466703119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9939100983229081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9937454111932069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html', 'title': 'N-283', 'score': 0.9936995454160369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9934618266665095}]
result = search.search('pear peach banana apple peach pear pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #352 checking search results for 'pear peach banana apple peach pear pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #352 checking search results for 'pear peach banana apple peach pear pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking search results for 'tomato banana apple apple pear apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 0.9999517016050551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html', 'title': 'N-165', 'score': 0.9954560371569122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 0.9945029275771575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html', 'title': 'N-772', 'score': 0.9902273978609426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html', 'title': 'N-939', 'score': 0.9893852343846271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-249.html', 'title': 'N-249', 'score': 0.9860964323165067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 0.9844238063657569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-712.html', 'title': 'N-712', 'score': 0.9819576003158202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-896.html', 'title': 'N-896', 'score': 0.9793329650149457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html', 'title': 'N-470', 'score': 0.977244149104411}]
result = search.search('tomato banana apple apple pear apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #353 checking search results for 'tomato banana apple apple pear apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #353 checking search results for 'tomato banana apple apple pear apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking search results for 'peach banana peach peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'title': 'N-360', 'score': 0.9997939164209976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-768.html', 'title': 'N-768', 'score': 0.9988538385067431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9982371959103244}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-662.html', 'title': 'N-662', 'score': 0.9971999986972893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html', 'title': 'N-290', 'score': 0.9955572754837109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9955412793769478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-524.html', 'title': 'N-524', 'score': 0.9949807947781932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.9945746276227382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-37.html', 'title': 'N-37', 'score': 0.9945709786380342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-964.html', 'title': 'N-964', 'score': 0.9940086203231991}]
result = search.search('peach banana peach peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #354 checking search results for 'peach banana peach peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #354 checking search results for 'peach banana peach peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking search results for 'coconut peach peach tomato peach apple pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-964.html', 'title': 'N-964', 'score': 0.9818195271017318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-546.html', 'title': 'N-546', 'score': 0.9814494577346359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-970.html', 'title': 'N-970', 'score': 0.981074067533128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-105.html', 'title': 'N-105', 'score': 0.9797365981463646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.9794615452157054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9792783067264936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-279.html', 'title': 'N-279', 'score': 0.9780706921019445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-873.html', 'title': 'N-873', 'score': 0.976085664408944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9758804896736344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html', 'title': 'N-145', 'score': 0.9722196552274276}]
result = search.search('coconut peach peach tomato peach apple pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #355 checking search results for 'coconut peach peach tomato peach apple pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #355 checking search results for 'coconut peach peach tomato peach apple pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking search results for 'pear peach tomato banana peach coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9999822061228667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-428.html', 'title': 'N-428', 'score': 0.9988534612389155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-998.html', 'title': 'N-998', 'score': 0.9986649689159566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9982912322393562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-577.html', 'title': 'N-577', 'score': 0.9964370543355091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-419.html', 'title': 'N-419', 'score': 0.9962411741093308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-644.html', 'title': 'N-644', 'score': 0.9953467799017665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9952402161014384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-540.html', 'title': 'N-540', 'score': 0.9946911812404837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-558.html', 'title': 'N-558', 'score': 0.9946898489219974}]
result = search.search('pear peach tomato banana peach coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #356 checking search results for 'pear peach tomato banana peach coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #356 checking search results for 'pear peach tomato banana peach coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking search results for 'banana peach tomato apple apple apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-762.html', 'title': 'N-762', 'score': 0.9999517016050551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-165.html', 'title': 'N-165', 'score': 0.9954560371569122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 0.9945029275771575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-772.html', 'title': 'N-772', 'score': 0.9902273978609426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html', 'title': 'N-939', 'score': 0.9893852343846272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-249.html', 'title': 'N-249', 'score': 0.9860964323165067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-932.html', 'title': 'N-932', 'score': 0.9844238063657571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-712.html', 'title': 'N-712', 'score': 0.9819576003158204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-896.html', 'title': 'N-896', 'score': 0.9793329650149457}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-470.html', 'title': 'N-470', 'score': 0.977244149104411}]
result = search.search('banana peach tomato apple apple apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #357 checking search results for 'banana peach tomato apple apple apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #357 checking search results for 'banana peach tomato apple apple apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking search results for 'pear peach peach banana apple apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.997128199160326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html', 'title': 'N-395', 'score': 0.9967395344948317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9918658522822792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-960.html', 'title': 'N-960', 'score': 0.9911272120038693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-117.html', 'title': 'N-117', 'score': 0.9902825098724867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html', 'title': 'N-560', 'score': 0.9896895466205874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-567.html', 'title': 'N-567', 'score': 0.9890401256901149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-260.html', 'title': 'N-260', 'score': 0.9888253889380539}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html', 'title': 'N-583', 'score': 0.9877163362877026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-805.html', 'title': 'N-805', 'score': 0.9857892452743334}]
result = search.search('pear peach peach banana apple apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #358 checking search results for 'pear peach peach banana apple apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #358 checking search results for 'pear peach peach banana apple apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking search results for 'peach coconut banana apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999395191314641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9989215172522741}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9980620077490977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9978835810356514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9976482473570288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9962892926678883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.995528970963184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9949772431926911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9948581986819995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9936019352659154}]
result = search.search('peach coconut banana apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #359 checking search results for 'peach coconut banana apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #359 checking search results for 'peach coconut banana apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking search results for 'peach coconut peach banana peach tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-279.html', 'title': 'N-279', 'score': 0.9998800374039924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html', 'title': 'N-290', 'score': 0.9996628362536101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html', 'title': 'N-297', 'score': 0.9966075962132837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html', 'title': 'N-752', 'score': 0.996583225047213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-847.html', 'title': 'N-847', 'score': 0.9947220292396302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-431.html', 'title': 'N-431', 'score': 0.9926727265403378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-145.html', 'title': 'N-145', 'score': 0.9919437636856782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-768.html', 'title': 'N-768', 'score': 0.989512020386878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-647.html', 'title': 'N-647', 'score': 0.9881579245846205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-970.html', 'title': 'N-970', 'score': 0.9881219618771659}]
result = search.search('peach coconut peach banana peach tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #360 checking search results for 'peach coconut peach banana peach tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #360 checking search results for 'peach coconut peach banana peach tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking search results for 'coconut apple banana peach apple coconut coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-229.html', 'title': 'N-229', 'score': 0.9999812199726815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-502.html', 'title': 'N-502', 'score': 0.996296499127303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-886.html', 'title': 'N-886', 'score': 0.9951192845200962}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html', 'title': 'N-691', 'score': 0.9946031625737867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-195.html', 'title': 'N-195', 'score': 0.9930819385910946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'title': 'N-0', 'score': 0.9910231541441676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-559.html', 'title': 'N-559', 'score': 0.9909789841186204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-961.html', 'title': 'N-961', 'score': 0.9904599313317503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-803.html', 'title': 'N-803', 'score': 0.9902504841377968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-151.html', 'title': 'N-151', 'score': 0.988612017349353}]
result = search.search('coconut apple banana peach apple coconut coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #361 checking search results for 'coconut apple banana peach apple coconut coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #361 checking search results for 'coconut apple banana peach apple coconut coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking search results for 'banana peach coconut apple peach tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999853793572516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9988139564073508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9979335266663842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9975486973349206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9973792225348945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9966996028040429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9951978818597592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9947811452816204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9945441699689878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9930458995580926}]
result = search.search('banana peach coconut apple peach tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #362 checking search results for 'banana peach coconut apple peach tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #362 checking search results for 'banana peach coconut apple peach tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking search results for 'pear coconut apple apple apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-865.html', 'title': 'N-865', 'score': 0.9998791320985776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-163.html', 'title': 'N-163', 'score': 0.9998791320985776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-695.html', 'title': 'N-695', 'score': 0.9998446710176259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9998344052909537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-551.html', 'title': 'N-551', 'score': 0.9996594409742987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-797.html', 'title': 'N-797', 'score': 0.9995362515602148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-867.html', 'title': 'N-867', 'score': 0.9984945955565531}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-605.html', 'title': 'N-605', 'score': 0.9984828005609768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.998278347036516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-939.html', 'title': 'N-939', 'score': 0.9976016602059341}]
result = search.search('pear coconut apple apple apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #363 checking search results for 'pear coconut apple apple apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #363 checking search results for 'pear coconut apple apple apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking search results for 'coconut pear pear peach peach peach banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html', 'title': 'N-297', 'score': 0.9999816568424429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html', 'title': 'N-290', 'score': 0.9987430635496255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html', 'title': 'N-357', 'score': 0.9965600796239974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9960382040089991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-747.html', 'title': 'N-747', 'score': 0.994114432384364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9923973658916996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-717.html', 'title': 'N-717', 'score': 0.9923810825881212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-847.html', 'title': 'N-847', 'score': 0.9905380699148119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-122.html', 'title': 'N-122', 'score': 0.9901147045058963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-647.html', 'title': 'N-647', 'score': 0.9896537545276896}]
result = search.search('coconut pear pear peach peach peach banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #364 checking search results for 'coconut pear pear peach peach peach banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #364 checking search results for 'coconut pear pear peach peach peach banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking search results for 'apple peach tomato tomato coconut banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999992961835997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9987120630744258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9978158565804276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9972751992112093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.997155452021919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9969887509409239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9949272973759633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9946124891058862}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9942864797851001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9926055227393175}]
result = search.search('apple peach tomato tomato coconut banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #365 checking search results for 'apple peach tomato tomato coconut banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #365 checking search results for 'apple peach tomato tomato coconut banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking search results for 'apple apple peach coconut apple banana tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-885.html', 'title': 'N-885', 'score': 0.9968103461382818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-747.html', 'title': 'N-747', 'score': 0.9954745361612486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-395.html', 'title': 'N-395', 'score': 0.9918200417564869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-729.html', 'title': 'N-729', 'score': 0.9915707173335121}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-438.html', 'title': 'N-438', 'score': 0.9896714191830228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html', 'title': 'N-560', 'score': 0.9892850183770545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-735.html', 'title': 'N-735', 'score': 0.9890981951156502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-410.html', 'title': 'N-410', 'score': 0.9884000418840402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-902.html', 'title': 'N-902', 'score': 0.9878188726995066}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-826.html', 'title': 'N-826', 'score': 0.9877893925934971}]
result = search.search('apple apple peach coconut apple banana tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #366 checking search results for 'apple apple peach coconut apple banana tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #366 checking search results for 'apple apple peach coconut apple banana tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking search results for 'apple peach apple apple peach peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-846.html', 'title': 'N-846', 'score': 0.9999204662518519}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-714.html', 'title': 'N-714', 'score': 0.9995417165459316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-199.html', 'title': 'N-199', 'score': 0.9982560698562349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-548.html', 'title': 'N-548', 'score': 0.9980296212592517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-416.html', 'title': 'N-416', 'score': 0.9977930755130534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-365.html', 'title': 'N-365', 'score': 0.9974454743232564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-826.html', 'title': 'N-826', 'score': 0.9973963661303965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-382.html', 'title': 'N-382', 'score': 0.9973436355615564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-747.html', 'title': 'N-747', 'score': 0.996949213780122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-377.html', 'title': 'N-377', 'score': 0.9968023408911978}]
result = search.search('apple peach apple apple peach peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #367 checking search results for 'apple peach apple apple peach peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #367 checking search results for 'apple peach apple apple peach peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking search results for 'pear banana pear coconut tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-464.html', 'title': 'N-464', 'score': 0.9999939443537381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-462.html', 'title': 'N-462', 'score': 0.9999649016681676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html', 'title': 'N-297', 'score': 0.9998160948447093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-752.html', 'title': 'N-752', 'score': 0.9997576029528696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-357.html', 'title': 'N-357', 'score': 0.9984999329372296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html', 'title': 'N-159', 'score': 0.9982488190001412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.997904553164366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html', 'title': 'N-290', 'score': 0.9972144237073152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9961433955095754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-542.html', 'title': 'N-542', 'score': 0.9956294522166755}]
result = search.search('pear banana pear coconut tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #368 checking search results for 'pear banana pear coconut tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #368 checking search results for 'pear banana pear coconut tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking search results for 'peach coconut apple peach banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999853793572516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.9988139564073508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9979335266663842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9975486973349206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9973792225348945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9966996028040429}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9951978818597591}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9947811452816204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9945441699689876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9930458995580926}]
result = search.search('peach coconut apple peach banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #369 checking search results for 'peach coconut apple peach banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #369 checking search results for 'peach coconut apple peach banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking search results for 'apple peach peach peach coconut apple apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-326.html', 'title': 'N-326', 'score': 0.9998839709160358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html', 'title': 'N-782', 'score': 0.9996983967338475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'title': 'N-9', 'score': 0.9988499355339409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html', 'title': 'N-679', 'score': 0.9968256398320046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-847.html', 'title': 'N-847', 'score': 0.996566256905793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-917.html', 'title': 'N-917', 'score': 0.9958622387596205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-297.html', 'title': 'N-297', 'score': 0.9958288212856632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-44.html', 'title': 'N-44', 'score': 0.9957121812775993}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-866.html', 'title': 'N-866', 'score': 0.9954521406142073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-841.html', 'title': 'N-841', 'score': 0.9948836783679502}]
result = search.search('apple peach peach peach coconut apple apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #370 checking search results for 'apple peach peach peach coconut apple apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #370 checking search results for 'apple peach peach peach coconut apple apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking search results for 'apple coconut banana peach tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-595.html', 'title': 'N-595', 'score': 0.9999853793572517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-868.html', 'title': 'N-868', 'score': 0.998813956407351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-442.html', 'title': 'N-442', 'score': 0.9979335266663842}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-963.html', 'title': 'N-963', 'score': 0.9975486973349206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-533.html', 'title': 'N-533', 'score': 0.9973792225348945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-399.html', 'title': 'N-399', 'score': 0.9966996028040427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-152.html', 'title': 'N-152', 'score': 0.9951978818597592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'title': 'N-201', 'score': 0.9947811452816203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-276.html', 'title': 'N-276', 'score': 0.9945441699689876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-75.html', 'title': 'N-75', 'score': 0.9930458995580926}]
result = search.search('apple coconut banana peach tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #371 checking search results for 'apple coconut banana peach tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #371 checking search results for 'apple coconut banana peach tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking search results for 'apple apple banana apple tomato peach peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-128.html', 'title': 'N-128', 'score': 0.9998843657252979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html', 'title': 'N-919', 'score': 0.998842907781433}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-457.html', 'title': 'N-457', 'score': 0.9981977145770896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-314.html', 'title': 'N-314', 'score': 0.9977732768471508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html', 'title': 'N-50', 'score': 0.9970854226492691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-962.html', 'title': 'N-962', 'score': 0.9965083024253856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-323.html', 'title': 'N-323', 'score': 0.9944534375740501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-521.html', 'title': 'N-521', 'score': 0.9941676006029091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-209.html', 'title': 'N-209', 'score': 0.9936979809075556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-480.html', 'title': 'N-480', 'score': 0.9935847068268103}]
result = search.search('apple apple banana apple tomato peach peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #372 checking search results for 'apple apple banana apple tomato peach peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #372 checking search results for 'apple apple banana apple tomato peach peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
