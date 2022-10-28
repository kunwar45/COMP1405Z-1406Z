
import testingtools
import crawler
import searchdata
import search
output = open('fruits5-outgoing-links-failed.txt', 'w')
success_output = open('fruits5-outgoing-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-832.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-808.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-653.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-629.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-147.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-748.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-577.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-587.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-590.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-775.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-75.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-638.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-804.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-62.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-770.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-618.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-618.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-618.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-618.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-766.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-170.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-267.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-766.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-766.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-766.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-257.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-652.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-586.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-73.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-564.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-265.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-438.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-118.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-223.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-355.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-569.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-570.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-843.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-424.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-987.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-932.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-771.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-771.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-771.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-771.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-691.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-198.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-769.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-457.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-691.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-691.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-691.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-241.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-177.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-599.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-241.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-241.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-241.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-587.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-360.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-587.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-587.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-587.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-246.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-470.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-459.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-341.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-459.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-459.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-459.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-395.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-785.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-929.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-802.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-729.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-49.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-729.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-729.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-729.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-357.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-109.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-978.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-828.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-492.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-81.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-534.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-806.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-177.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-120.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-530.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-598.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-98.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-139.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-410.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-483.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-747.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-830.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-728.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-830.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-830.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-830.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-214.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-177.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-228.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-314.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-738.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-214.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-214.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-214.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-126.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-537.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-512.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-73.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-321.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-720.html\n\n')
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
