
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')


output = open('fruits-all-outgoing-failed.txt', 'w')
success_output = open('fruits-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-379.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-379.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-379.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-379.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-957.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-186.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-567.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-810.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-921.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-964.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-199.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-964.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-964.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-964.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-557.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-210.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-119.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-149.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-959.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-464.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-464.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-464.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-464.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-149.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-153.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-149.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-149.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-149.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-245.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-885.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-868.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-177.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-638.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-341.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-86.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-341.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-341.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-341.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-93.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-163.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-303.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-377.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-657.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-229.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-255.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-292.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-533.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-560.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-590.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-641.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-888.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-312.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-312.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-312.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-312.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-206.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-309.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-327.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-586.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-36.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-374.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-503.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-374.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-374.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-374.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-536.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-125.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-536.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-536.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-536.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-644.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-61.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-644.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-644.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-644.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-752.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-483.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-752.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-752.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-752.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-337.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-523.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-523.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-523.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-523.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-520.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-520.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-520.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-520.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-361.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-194.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-720.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-361.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-361.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-361.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-193.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-192.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-631.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-446.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-601.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-207.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-757.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-757.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-757.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-757.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-321.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-544.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-820.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-959.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-310.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-758.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-372.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-758.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-758.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-758.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-381.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-402.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-364.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-364.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-364.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-364.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-899.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-975.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-938.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-975.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-975.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-975.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-907.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-431.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-966.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-95.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-907.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-907.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-907.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-194.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-260.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-361.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-534.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-633.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-194.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-194.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-194.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-426.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-441.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-896.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-896.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-896.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-896.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-474.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-970.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-365.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-487.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-335.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-970.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-970.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-970.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-651.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-187.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-595.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-892.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-122.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-307.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-706.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-908.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-509.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-539.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-347.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-658.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html\n\n')
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









output = open('fruits-all-incoming-failed.txt', 'w')
success_output = open('fruits-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-190.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-190.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-190.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-190.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-916.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-903.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-916.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-916.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-916.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-99.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-640.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-28.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-71.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-261.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-464.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-933.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-888.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-158.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-158.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-158.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-158.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-897.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-661.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-897.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-897.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-897.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-488.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-272.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-488.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-488.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-488.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-695.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-552.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-695.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-695.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-695.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-347.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-625.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-258.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-963.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-310.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-451.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-939.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-451.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-451.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-451.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-693.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-693.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-693.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-693.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-862.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-862.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-862.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-862.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-730.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-856.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-730.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-730.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-730.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-988.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-499.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-973.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-565.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-189.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-332.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-448.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-310.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-448.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-448.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-448.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-98.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-154.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-358.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-98.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-98.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-98.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-926.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-544.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-926.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-926.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-926.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-515.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-401.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-281.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-519.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-143.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-250.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-673.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-300.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-98.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-372.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-203.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-721.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-762.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-232.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-718.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-624.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-991.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-641.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-204.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-148.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-979.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-181.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-514.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-757.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-73.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-117.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-886.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-886.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-886.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-886.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-673.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-761.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-787.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-673.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-673.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-673.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-386.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-272.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-666.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-900.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-825.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-162.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-163.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-704.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-216.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-909.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-366.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-80.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-366.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-366.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-366.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-993.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-865.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-993.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-993.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-993.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-71.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-908.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-480.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-71.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-71.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-71.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-365.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-786.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-955.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-709.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-17.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-888.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-163.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-657.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-533.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-590.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-292.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-560.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-93.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-303.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-377.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-229.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-255.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-641.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-789.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-812.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-983.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-789.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-789.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-789.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-619.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-445.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-619.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-619.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-619.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-554.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-399.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-554.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-554.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-554.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-883.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-883.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-883.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-883.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-264.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-330.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-192.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-32.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-584.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-584.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-584.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-584.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-115.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-598.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-498.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-490.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-693.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-131.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-582.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-27.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-950.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-295.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-258.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-797.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-551.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-220.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-148.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-566.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-613.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-676.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-714.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-131.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-431.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-131.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-131.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-131.html\n\n')
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









output = open('fruits-all-pagerank-failed.txt', 'w')
success_output = open('fruits-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-56.html
expected = 0.001455568622482555
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-56.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-56.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-56.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html
expected = 0.00035427335811540094
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-798.html
expected = 0.0004072100129885606
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-798.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-798.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-798.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html
expected = 0.0012287486952225768
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-102.html
expected = 0.0009408248466443155
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-102.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-102.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-102.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html
expected = 0.0006412670165577172
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-831.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html
expected = 0.0006366649653155891
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html
expected = 0.002617545453233247
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-377.html
expected = 0.000372061791611334
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-377.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-377.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-377.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html
expected = 0.0006597432792956402
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-866.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-546.html
expected = 0.0006688631484327515
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-546.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-546.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-546.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html
expected = 0.0015598805959350262
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-543.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html
expected = 0.0003616945323313568
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-191.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html
expected = 0.00046649425338761126
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-929.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html
expected = 0.0009676453231083677
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-657.html
expected = 0.0006286718458739306
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-657.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-657.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-657.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html
expected = 0.0003636005891138167
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html
expected = 0.002594812053228595
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-52.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html
expected = 0.0011841739251080676
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html
expected = 0.001678594539690731
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-236.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-680.html
expected = 0.0003556173546590424
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-680.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-680.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-680.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html
expected = 0.0006865291066885293
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-404.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-50.html
expected = 0.0011659816403004415
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-50.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-50.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-50.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html
expected = 0.00036505998371693207
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html
expected = 0.0024831472173457003
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html
expected = 0.0004183116518067711
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-736.html
expected = 0.00045475217525026834
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-736.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-736.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-736.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html
expected = 0.00036513600954070954
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-961.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-639.html
expected = 0.00037920264995288256
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-639.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-639.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-639.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html
expected = 0.0009170179975270252
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-84.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html
expected = 0.0008665613000852091
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-834.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html
expected = 0.0014702879942616568
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-516.html
expected = 0.0004076035124938494
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-516.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-516.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-516.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-182.html
expected = 0.0003968176028593136
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-182.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-182.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-182.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-807.html
expected = 0.0012188835212663558
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-807.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-807.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-807.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html
expected = 0.0006517395416778356
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-587.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-352.html
expected = 0.0003599577981968599
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-352.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-352.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-352.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-411.html
expected = 0.00035862732370814203
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-411.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-411.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-411.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-507.html
expected = 0.00036505998371693207
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-507.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-507.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-507.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html
expected = 0.0009918170388501532
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-526.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-820.html
expected = 0.0011619515193739772
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-820.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-820.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-820.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html
expected = 0.0025327025973879663
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-802.html
expected = 0.000673865383454555
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-802.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-802.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-802.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-130.html
expected = 0.0024754861998717644
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-130.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-130.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-130.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-125.html
expected = 0.0031324318438871205
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-125.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-125.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-125.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html
expected = 0.0012507893842195104
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-79.html
expected = 0.0007491205452923778
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-79.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-79.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-79.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html
expected = 0.0003681382706602032
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-902.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html
expected = 0.0034782775379432825
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html
expected = 0.0003616945323313568
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html\n\n')
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









output = open('fruits-all-idf-failed.txt', 'w')
success_output = open('fruits-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word peach
expected = 0.05439229681862769
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word pear
expected = 0.06039727964395631
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word apple
expected = 0.06039727964395631
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word banana
expected = 0.066427361738976
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word coconut
expected = 0.05889368905356862
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word coconut\n\n')
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









output = open('fruits-all-tf-failed.txt', 'w')
success_output = open('fruits-all-tf-passed.txt', 'w')

#Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word pear
expected = 0.3
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word apple
expected = 0.4
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word banana
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word coconut
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-890.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word pear
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word apple
expected = 0.275
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word banana
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word coconut
expected = 0.325
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word peach
expected = 0.175
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word pear
expected = 0.15384615384615385
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word apple
expected = 0.2692307692307692
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word banana
expected = 0.15384615384615385
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word coconut
expected = 0.11538461538461539
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word peach
expected = 0.3076923076923077
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word pear
expected = 0.2777777777777778
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word apple
expected = 0.2222222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word banana
expected = 0.2222222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word coconut
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word peach
expected = 0.2222222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-370.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word pear
expected = 0.19791666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word apple
expected = 0.1875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word banana
expected = 0.22916666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word coconut
expected = 0.1875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word peach
expected = 0.19791666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-54.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word pear
expected = 0.17857142857142858
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word apple
expected = 0.32142857142857145
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word banana
expected = 0.17857142857142858
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word coconut
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word peach
expected = 0.17857142857142858
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word apple
expected = 0.4
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word banana
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word peach
expected = 0.4
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-147.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word pear
expected = 0.375
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word apple
expected = 0.1875
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word banana
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word coconut
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word peach
expected = 0.25
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word pear
expected = 0.22857142857142856
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word apple
expected = 0.3142857142857143
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word banana
expected = 0.08571428571428572
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word coconut
expected = 0.17142857142857143
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word peach
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word pear
expected = 0.20430107526881722
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word apple
expected = 0.11827956989247312
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word banana
expected = 0.3333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word coconut
expected = 0.13978494623655913
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word peach
expected = 0.20430107526881722
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
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









output = open('fruits-all-tfidf-failed.txt', 'w')
success_output = open('fruits-all-tfidf-passed.txt', 'w')

#Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word apple
expected = 0.01271767313358255
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word pear
expected = 0.01163523864451864
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word banana
expected = 0.02193090059223356
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word peach
expected = 0.016153518829797753
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word coconut
expected = 0.01649658869437907
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-432.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word apple
expected = 0.012388353581959543
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word pear
expected = 0.01548222376149403
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word banana
expected = 0.024527227840924936
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word peach
expected = 0.013942907945720043
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word coconut
expected = 0.01309751011005899
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word apple
expected = 0.01548222376149403
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word pear
expected = 0.025067135906672637
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word banana
expected = 0.012463566811956957
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word peach
expected = 0.013942907945720043
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word coconut
expected = 0.011050046383086806
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word apple
expected = 0.017034168976319288
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word pear
expected = 0.01200576304051094
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word banana
expected = 0.015083588527654358
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word peach
expected = 0.01822056263115979
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word coconut
expected = 0.015812298017374674
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-705.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word apple
expected = 0.011207056673184517
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word pear
expected = 0.01269657765936608
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word banana
expected = 0.018717302046470013
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word peach
expected = 0.02141228089362885
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word coconut
expected = 0.01380852374156493
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word apple
expected = 0.0179790953408178
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word pear
expected = 0.014974147360882971
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word banana
expected = 0.01977413348721163
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word peach
expected = 0.01348534690072781
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word coconut
expected = 0.01309751011005899
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-686.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word apple
expected = 0.0166475705100292
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word pear
expected = 0.0166475705100292
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word banana
expected = 0.022388345018578358
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word peach
expected = 0.01833210706626403
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word coconut
expected = 0.0043581672333330695
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-685.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word apple
expected = 0.01026300783061102
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word pear
expected = 0.035330143737283666
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word peach
expected = 0.009242611115355993
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word coconut
expected = 0.018959533117904052
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word apple
expected = 0.015886562565125537
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word pear
expected = 0.01217813669875404
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word banana
expected = 0.023906938132643787
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word peach
expected = 0.01209643459154539
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word coconut
expected = 0.015491066507565628
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word apple
expected = 0.023813375343272693
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word pear
expected = 0.017936889064465576
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word banana
expected = 0.00788124088725243
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word peach
expected = 0.014307045475623087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word coconut
expected = 0.013443602780593462
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-237.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
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









output = open('fruits-all-search-failed.txt', 'w')
success_output = open('fruits-all-search-passed.txt', 'w')

#Test #291 checking search results for 'peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #291 checking search results for 'peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #291 checking search results for 'peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking search results for 'pear banana tomato tomato peach apple banana peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.017895243595845423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01393917652903197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012904704531775961}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010105674565088586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00860657573594684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007818580473401983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0077601673431134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007606137752193702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006623837178897532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006394063481214497}]
result = search.search('pear banana tomato tomato peach apple banana peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #292 checking search results for 'pear banana tomato tomato peach apple banana peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #292 checking search results for 'pear banana tomato tomato peach apple banana peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking search results for 'apple apple banana peach pear tomato tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9999980650161844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9989400211212546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.9986532265478112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.9977382351341291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 0.9970922893653976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9967380196032567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9967137961192949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9962169438919931}]
result = search.search('apple apple banana peach pear tomato tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #293 checking search results for 'apple apple banana peach pear tomato tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #293 checking search results for 'apple apple banana peach pear tomato tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking search results for 'banana peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02084623916649196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015625883074666478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012643869829430191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009449574521113812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008419899703797177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007774936676926263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0076399872387705485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007321853566747798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007061425110590793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006644539952636676}]
result = search.search('banana peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #294 checking search results for 'banana peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #294 checking search results for 'banana peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking search results for 'banana peach peach coconut tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019263232561998363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014971025362353865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011319940651870376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.008768567457716488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00795541834702167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007201808020460346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007151297769155847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006725902760355549}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0065817568367193425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006288441263830484}]
result = search.search('banana peach peach coconut tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #295 checking search results for 'banana peach peach coconut tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #295 checking search results for 'banana peach peach coconut tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking search results for 'banana peach peach coconut tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html', 'title': 'N-31', 'score': 0.9999764120760435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-931.html', 'title': 'N-931', 'score': 0.9999589495904073}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.999924885974288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html', 'title': 'N-59', 'score': 0.9938167991652156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html', 'title': 'N-853', 'score': 0.9932205095217291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-990.html', 'title': 'N-990', 'score': 0.9912732995057555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html', 'title': 'N-227', 'score': 0.9910586659482239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'title': 'N-266', 'score': 0.9894737707765816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html', 'title': 'N-934', 'score': 0.9888911408520543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html', 'title': 'N-481', 'score': 0.9886222122273766}]
result = search.search('banana peach peach coconut tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #296 checking search results for 'banana peach peach coconut tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #296 checking search results for 'banana peach peach coconut tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking search results for 'tomato coconut peach pear tomato coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9995047751742977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9987875472392461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9985359223669154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.9984365382655309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9980988265865693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9975009002772312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 0.9971830957606921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9965822312652086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html', 'title': 'N-92', 'score': 0.9965018343494766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html', 'title': 'N-296', 'score': 0.995385735808629}]
result = search.search('tomato coconut peach pear tomato coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #297 checking search results for 'tomato coconut peach pear tomato coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #297 checking search results for 'tomato coconut peach pear tomato coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking search results for 'peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010417067314545846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008507193563889777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008227390811338423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00787315571136734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007248519972589282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006744943947177922}]
result = search.search('peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #298 checking search results for 'peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #298 checking search results for 'peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking search results for 'peach coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0201915323381759}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015568621717957296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012128604159223611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010456425114702638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008875080909091627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008134158943291617}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00797684967170918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0075904713204281785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007265482055577727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006650922470212738}]
result = search.search('peach coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #299 checking search results for 'peach coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #299 checking search results for 'peach coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking search results for 'banana peach coconut tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019929098689925193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015548139406075231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012338295072619063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00943260311695852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008392737953394633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007725627337417748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0076283953847429194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00716139339644426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007104332540543943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006616463130220537}]
result = search.search('banana peach coconut tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #300 checking search results for 'banana peach coconut tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #300 checking search results for 'banana peach coconut tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking search results for 'peach peach coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019191205129280565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015135189796897148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.01121952006932456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010301801869511313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008800836803515365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008030895319060745}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00781141667413937}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007214424824154684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006905536150323476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006415828581772962}]
result = search.search('peach peach coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #301 checking search results for 'peach peach coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #301 checking search results for 'peach peach coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking search results for 'banana apple pear coconut apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 0.9979087300308276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 0.9923639821311339}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9897326068347375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html', 'title': 'N-172', 'score': 0.9891998801191023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-795.html', 'title': 'N-795', 'score': 0.9888294826380608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9881447489757941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9873445503442467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-305.html', 'title': 'N-305', 'score': 0.9865419172826172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.9843796050986671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9838795503055123}]
result = search.search('banana apple pear coconut apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #302 checking search results for 'banana apple pear coconut apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #302 checking search results for 'banana apple pear coconut apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking search results for 'peach peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02084623916649196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015625883074666478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012643869829430191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009449574521113812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008419899703797177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007774936676926263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0076399872387705485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007321853566747798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007061425110590793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006644539952636676}]
result = search.search('peach peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #303 checking search results for 'peach peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #303 checking search results for 'peach peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking search results for 'apple pear peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019178513309742618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014720462919386786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0128228785868486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00987180736666412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008482622488578007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007738243476914324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007694959288013001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007621763880118829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006617085377757683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006523509573146742}]
result = search.search('apple pear peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #304 checking search results for 'apple pear peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #304 checking search results for 'apple pear peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking search results for 'apple peach peach banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019913795422719482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01518054121634502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012680615206329153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009565836205192815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008394209783791264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007711668466722501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007617428122574796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007422301836681493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006631490119138914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0065988595666396505}]
result = search.search('apple peach peach banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #305 checking search results for 'apple peach peach banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #305 checking search results for 'apple peach peach banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking search results for 'peach coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('peach coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #306 checking search results for 'peach coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #306 checking search results for 'peach coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking search results for 'peach peach apple coconut peach peach peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-694.html', 'title': 'N-694', 'score': 0.9955029377675804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html', 'title': 'N-537', 'score': 0.9944349280361986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-255.html', 'title': 'N-255', 'score': 0.9828211603056004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-408.html', 'title': 'N-408', 'score': 0.9819979223125823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9819608567396557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-545.html', 'title': 'N-545', 'score': 0.9808455639665976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-851.html', 'title': 'N-851', 'score': 0.9784528074197316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html', 'title': 'N-346', 'score': 0.9681027695070002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9653660643510003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-419.html', 'title': 'N-419', 'score': 0.9637662444159119}]
result = search.search('peach peach apple coconut peach peach peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #307 checking search results for 'peach peach apple coconut peach peach peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #307 checking search results for 'peach peach apple coconut peach peach peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking search results for 'banana pear apple banana banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html', 'title': 'N-378', 'score': 0.9999923938902627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9999798203324569}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 0.9999371619676191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-419.html', 'title': 'N-419', 'score': 0.9998239728691435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 0.9998239728691435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html', 'title': 'N-504', 'score': 0.9993034438355489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-638.html', 'title': 'N-638', 'score': 0.998651916614329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'title': 'N-877', 'score': 0.998030442026512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9964852503402707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html', 'title': 'N-485', 'score': 0.9964031291270531}]
result = search.search('banana pear apple banana banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #308 checking search results for 'banana pear apple banana banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #308 checking search results for 'banana pear apple banana banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking search results for 'apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010417067314545846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008507193563889777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008227390811338423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00787315571136734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007248519972589282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006744943947177922}]
result = search.search('apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #309 checking search results for 'apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #309 checking search results for 'apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking search results for 'peach peach banana pear tomato banana pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016676753915358732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01518682559833941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012548961455819907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.01021859044692909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008871167159582888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008239072806242214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007918811949842383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007487789600351893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007426400568641423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006637032181786938}]
result = search.search('peach peach banana pear tomato banana pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #310 checking search results for 'peach peach banana pear tomato banana pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #310 checking search results for 'peach peach banana pear tomato banana pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking search results for 'tomato peach coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02013186977839246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015547289199447291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012070261581087148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010452063178239563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.0088755402631478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00811598274558078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007986081230316378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007568042762686509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007244013786095432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006638163346603311}]
result = search.search('tomato peach coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #311 checking search results for 'tomato peach coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #311 checking search results for 'tomato peach coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking search results for 'banana peach coconut peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01980960407975694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015263544149348473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012521309510177995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009560950687388003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008423796291291124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007714896818881797}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007658453957749874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007309335618708798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006764141937409491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006613954698047577}]
result = search.search('banana peach coconut peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #312 checking search results for 'banana peach coconut peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #312 checking search results for 'banana peach coconut peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking search results for 'coconut banana peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01994607735513016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01556403108786007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012376632176457953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00945665552716443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008407091337731298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007746725522498257}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00764277729198535}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007176502495456641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007123478471415808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00662701012806181}]
result = search.search('coconut banana peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #313 checking search results for 'coconut banana peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #313 checking search results for 'coconut banana peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking search results for 'apple pear tomato banana peach tomato peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020561043673030358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014770004556331602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012621430124485224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009732842888441964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007793961993014412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00778488890390411}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007696672592600446}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007367707118291827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007189016765152486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006447385284825337}]
result = search.search('apple pear tomato banana peach tomato peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #314 checking search results for 'apple pear tomato banana peach tomato peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #314 checking search results for 'apple pear tomato banana peach tomato peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking search results for 'peach coconut tomato banana pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9999997735308108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999911122299763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999911122299763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9984408235572477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9978838759671222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9968537839795928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-935.html', 'title': 'N-935', 'score': 0.9967801905024776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9961522319260571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'title': 'N-683', 'score': 0.996129070653888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9960927424862462}]
result = search.search('peach coconut tomato banana pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #315 checking search results for 'peach coconut tomato banana pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #315 checking search results for 'peach coconut tomato banana pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking search results for 'tomato peach tomato pear banana tomato peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0202989823449972}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014633508204579402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012624340752545957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009523347034923621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008374424847295989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007747994301451238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007601009061884632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007384085354856829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006921775182723887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006507054851355943}]
result = search.search('tomato peach tomato pear banana tomato peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #316 checking search results for 'tomato peach tomato pear banana tomato peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #316 checking search results for 'tomato peach tomato pear banana tomato peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking search results for 'banana peach pear banana coconut apple peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016480018488994913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01492103781097902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012534694638650553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00994529020262707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008871498358358248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007992252161381086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007817441967241478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0074217398764181465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006863820061878064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0065630372295199715}]
result = search.search('banana peach pear banana coconut apple peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #317 checking search results for 'banana peach pear banana coconut apple peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #317 checking search results for 'banana peach pear banana coconut apple peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking search results for 'apple peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010417067314545846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008507193563889777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008227390811338423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00787315571136734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007248519972589282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006744943947177922}]
result = search.search('apple peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #318 checking search results for 'apple peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #318 checking search results for 'apple peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking search results for 'banana banana banana pear banana banana coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 0.9869632583557562}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9865824050164348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 0.9855725067805196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.98533788591605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9846401802845892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-944.html', 'title': 'N-944', 'score': 0.977762518713738}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-489.html', 'title': 'N-489', 'score': 0.9744721988796584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-419.html', 'title': 'N-419', 'score': 0.9697681526760809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-212.html', 'title': 'N-212', 'score': 0.9674836632623921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-638.html', 'title': 'N-638', 'score': 0.961209204070931}]
result = search.search('banana banana banana pear banana banana coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #319 checking search results for 'banana banana banana pear banana banana coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #319 checking search results for 'banana banana banana pear banana banana coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking search results for 'peach tomato pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01735781777758059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach tomato pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #320 checking search results for 'peach tomato pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #320 checking search results for 'peach tomato pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking search results for 'apple coconut apple apple tomato pear peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9979158173561157}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9961778000641596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 0.9917156683361443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9916964845958847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-795.html', 'title': 'N-795', 'score': 0.9915123473849354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.9904636727420999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9889410666646409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-64.html', 'title': 'N-64', 'score': 0.9888468168094845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9887243051178297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 0.9872512719107531}]
result = search.search('apple coconut apple apple tomato pear peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #321 checking search results for 'apple coconut apple apple tomato pear peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #321 checking search results for 'apple coconut apple apple tomato pear peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking search results for 'peach coconut peach apple apple pear pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.018103893734594194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015572145851558026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012429651781445382}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010344715924782137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008598305396802838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008231092645953153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008019076082376952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007511417797740448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007339515451633777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006656813551930731}]
result = search.search('peach coconut peach apple apple pear pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #322 checking search results for 'peach coconut peach apple apple pear pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #322 checking search results for 'peach coconut peach apple apple pear pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking search results for 'coconut tomato peach tomato pear peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.0191897635605327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014773832828788351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012472834545792849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009867303831618872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008491912240188162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00767560101999541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0076337892594222695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007573835369089038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006697183783763757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006533377603048385}]
result = search.search('coconut tomato peach tomato pear peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #323 checking search results for 'coconut tomato peach tomato pear peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #323 checking search results for 'coconut tomato peach tomato pear peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking search results for 'coconut tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('coconut tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #324 checking search results for 'coconut tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #324 checking search results for 'coconut tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking search results for 'banana banana coconut peach apple banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-638.html', 'title': 'N-638', 'score': 0.9924030881920995}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-887.html', 'title': 'N-887', 'score': 0.9915452048198747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html', 'title': 'N-313', 'score': 0.9895675646995399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'title': 'N-90', 'score': 0.9892366083352108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 0.9886099876243117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-212.html', 'title': 'N-212', 'score': 0.9883997724545991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html', 'title': 'N-915', 'score': 0.9856337444346667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html', 'title': 'N-240', 'score': 0.9854068336275925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.9851113043275028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-535.html', 'title': 'N-535', 'score': 0.9830643626318121}]
result = search.search('banana banana coconut peach apple banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #325 checking search results for 'banana banana coconut peach apple banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #325 checking search results for 'banana banana coconut peach apple banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking search results for 'peach apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020994924567287326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015698376531429147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010417067314545846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008507193563889777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008227390811338423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00787315571136734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007248519972589282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006744943947177922}]
result = search.search('peach apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #326 checking search results for 'peach apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #326 checking search results for 'peach apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking search results for 'pear apple pear banana apple peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-310.html', 'title': 'N-310', 'score': 0.9981134671676664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-657.html', 'title': 'N-657', 'score': 0.9973159562111288}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-158.html', 'title': 'N-158', 'score': 0.9946899077312469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-102.html', 'title': 'N-102', 'score': 0.9946506903292601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 0.9939836976686375}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-205.html', 'title': 'N-205', 'score': 0.9926607119819444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-859.html', 'title': 'N-859', 'score': 0.9916116943158698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-544.html', 'title': 'N-544', 'score': 0.9906977080599635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html', 'title': 'N-934', 'score': 0.9906781995963926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-189.html', 'title': 'N-189', 'score': 0.9902547976285484}]
result = search.search('pear apple pear banana apple peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #327 checking search results for 'pear apple pear banana apple peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #327 checking search results for 'pear apple pear banana apple peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking search results for 'coconut apple coconut coconut banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html', 'title': 'N-647', 'score': 0.999723187608747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9988275322696596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-473.html', 'title': 'N-473', 'score': 0.9975214795321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.9964155825850566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 0.9961787734631828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-86.html', 'title': 'N-86', 'score': 0.9957270343824534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-916.html', 'title': 'N-916', 'score': 0.9938936935288144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-750.html', 'title': 'N-750', 'score': 0.991785778285083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9915855821457372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9907532121231901}]
result = search.search('coconut apple coconut coconut banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #328 checking search results for 'coconut apple coconut coconut banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #328 checking search results for 'coconut apple coconut coconut banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking search results for 'coconut pear banana apple peach peach pear banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016480018488994913}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01492103781097902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012534694638650557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00994529020262707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008871498358358248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007992252161381087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007817441967241478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.0074217398764181465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006863820061878065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006563037229519969}]
result = search.search('coconut pear banana apple peach peach pear banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #329 checking search results for 'coconut pear banana apple peach peach pear banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #329 checking search results for 'coconut pear banana apple peach peach pear banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking search results for 'tomato pear banana tomato peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020265917722930637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014664712225896133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012656863112068274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009550661772807514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00839609343073485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007758808725598633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007626010498045943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007406146949837069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006943873273638172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006519973687301995}]
result = search.search('tomato pear banana tomato peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #330 checking search results for 'tomato pear banana tomato peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #330 checking search results for 'tomato pear banana tomato peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking search results for 'banana tomato apple peach pear peach pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01712454643049361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015361090390081286}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012621430124485224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009220464246703393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008489578213513746}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0077264673729491645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007507317034257534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007367707118291826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006771038776786627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006593344383491017}]
result = search.search('banana tomato apple peach pear peach pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #331 checking search results for 'banana tomato apple peach pear peach pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #331 checking search results for 'banana tomato apple peach pear peach pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking search results for 'peach peach banana tomato tomato tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020898121186926345}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015587063157889077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012539375529035132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00934367792817346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008353062480868338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007741644560171998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0075622220466543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007243873235448062}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006997767032953412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006613951664367636}]
result = search.search('peach peach banana tomato tomato tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #332 checking search results for 'peach peach banana tomato tomato tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #332 checking search results for 'peach peach banana tomato tomato tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking search results for 'peach peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02084623916649196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015625883074666478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012643869829430191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009449574521113812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008419899703797177}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007774936676926263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0076399872387705485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007321853566747798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007061425110590793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006644539952636676}]
result = search.search('peach peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #333 checking search results for 'peach peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #333 checking search results for 'peach peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking search results for 'peach pear apple tomato apple apple tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9999957846057485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9997550911156046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9996668466785874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9987854110989463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'title': 'N-781', 'score': 0.9980792489481389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 0.9978369231293158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 0.9966218934019153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.996384977729776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'title': 'N-74', 'score': 0.9960542431570496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-663.html', 'title': 'N-663', 'score': 0.9958611178813179}]
result = search.search('peach pear apple tomato apple apple tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #334 checking search results for 'peach pear apple tomato apple apple tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #334 checking search results for 'peach pear apple tomato apple apple tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking search results for 'apple peach coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020108874318977968}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015182736411680768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012362877989198098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009786946584125237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00887554026285679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0076995653955578645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007628748088830883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007615561561707664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006606300661107939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006570919988620426}]
result = search.search('apple peach coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #335 checking search results for 'apple peach coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #335 checking search results for 'apple peach coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking search results for 'apple apple coconut banana tomato peach peach pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019864392417071934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01486295493336122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012330703044182571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009766668503940928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007878344837289789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007838259610866467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007570730437400947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007336301958112876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007225815350107827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006459179119213989}]
result = search.search('apple apple coconut banana tomato peach peach pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #336 checking search results for 'apple apple coconut banana tomato peach peach pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #336 checking search results for 'apple apple coconut banana tomato peach peach pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking search results for 'peach tomato pear banana apple pear tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-535.html', 'title': 'N-535', 'score': 0.9989799728275869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-966.html', 'title': 'N-966', 'score': 0.9986125958195095}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html', 'title': 'N-690', 'score': 0.9983587850907406}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-351.html', 'title': 'N-351', 'score': 0.9982101369183451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.9977864434905772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-609.html', 'title': 'N-609', 'score': 0.996401080068423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-948.html', 'title': 'N-948', 'score': 0.9960920421902402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-699.html', 'title': 'N-699', 'score': 0.99590684256902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-345.html', 'title': 'N-345', 'score': 0.9950208133612236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html', 'title': 'N-394', 'score': 0.9949423054363845}]
result = search.search('peach tomato pear banana apple pear tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #337 checking search results for 'peach tomato pear banana apple pear tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #337 checking search results for 'peach tomato pear banana apple pear tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking search results for 'peach coconut apple coconut pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9995969329171027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9989968972862464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.9986610713300162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9983592106328126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9983260627527692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 0.9978689749912247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9975720694247544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html', 'title': 'N-92', 'score': 0.996511954883613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9963236074788717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html', 'title': 'N-296', 'score': 0.9960932470196479}]
result = search.search('peach coconut apple coconut pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #338 checking search results for 'peach coconut apple coconut pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #338 checking search results for 'peach coconut apple coconut pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking search results for 'coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02099492456728733}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015524735848489709}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013216295889852698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010158987971029421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008510726413291102}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.008300270253703926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007892485331647896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007554565208180449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007412250626492393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006730205640271726}]
result = search.search('coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #339 checking search results for 'coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #339 checking search results for 'coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking search results for 'peach pear tomato peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020004747184698784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014479904652107195}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012830296506182757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010255212123151234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008452875003805163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007819833176572918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0076994107523929755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007606010897836154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006839598180405214}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006480933555005995}]
result = search.search('peach pear tomato peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #340 checking search results for 'peach pear tomato peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #340 checking search results for 'peach pear tomato peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking search results for 'pear apple peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019178513309742618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014720462919386786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.0128228785868486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00987180736666412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008482622488578007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007738243476914324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007694959288013001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007621763880118829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006617085377757683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006523509573146742}]
result = search.search('pear apple peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #341 checking search results for 'pear apple peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #341 checking search results for 'pear apple peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking search results for 'banana peach peach banana banana coconut peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01709598324305794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014761711201912593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011862129680201007}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010311501780493698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.0088281698040057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00806434179396728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007955920812405133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007202819388922532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007188767024628172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006407509820051279}]
result = search.search('banana peach peach banana banana coconut peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #342 checking search results for 'banana peach peach banana banana coconut peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #342 checking search results for 'banana peach peach banana banana coconut peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking search results for 'tomato pear peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01735781777758059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('tomato pear peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #343 checking search results for 'tomato pear peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #343 checking search results for 'tomato pear peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking search results for 'banana peach coconut apple banana apple apple pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9929764042867817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html', 'title': 'N-294', 'score': 0.9894509786265963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-949.html', 'title': 'N-949', 'score': 0.9890065618710074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9888746310638502}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9886747969503082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9885213649216982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-271.html', 'title': 'N-271', 'score': 0.9845792740288246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-603.html', 'title': 'N-603', 'score': 0.9839960582872329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-652.html', 'title': 'N-652', 'score': 0.9834796082181069}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html', 'title': 'N-140', 'score': 0.9803105257154069}]
result = search.search('banana peach coconut apple banana apple apple pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #344 checking search results for 'banana peach coconut apple banana apple apple pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #344 checking search results for 'banana peach coconut apple banana apple apple pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking search results for 'peach pear tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01735781777758059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015607807888514185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013385889918798154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010421326325841602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008873633543065484}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.0082508053526444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.008032820186304992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007799885382063103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007470358888222108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0067615789780501355}]
result = search.search('peach pear tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #345 checking search results for 'peach pear tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #345 checking search results for 'peach pear tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking search results for 'tomato peach tomato peach tomato apple banana tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019881127694071053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015137152100452573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012624340752545957}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00951068399858362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008369310098560135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007689412089860333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007573340493278918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007384085354856829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.0065885421991189715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006579207693047792}]
result = search.search('tomato peach tomato peach tomato apple banana tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #346 checking search results for 'tomato peach tomato peach tomato apple banana tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #346 checking search results for 'tomato peach tomato peach tomato apple banana tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking search results for 'peach peach coconut tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02013186977839246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015547289199447291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012070261581087148}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010452063178239563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.0088755402631478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.00811598274558078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007986081230316378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007568042762686509}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007244013786095432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006638163346603311}]
result = search.search('peach peach coconut tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #347 checking search results for 'peach peach coconut tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #347 checking search results for 'peach peach coconut tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking search results for 'banana banana peach peach peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.02041769321332317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015695295563845506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.013067418062178126}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009905874726749813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008688136060936253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007969433357186959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.00787973349031283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007654941023042055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007324610994237839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006744840464271905}]
result = search.search('banana banana peach peach peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #348 checking search results for 'banana banana peach peach peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #348 checking search results for 'banana banana peach peach peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking search results for 'peach tomato peach banana apple apple pear' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020550599585527584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.01478201196540524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012634113157543704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009742180499979701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007805455065996239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007792979813850965}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007701484261531662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007376485251085901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007193779796854369}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006452981967525513}]
result = search.search('peach tomato peach banana apple apple pear',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #349 checking search results for 'peach tomato peach banana apple apple pear' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #349 checking search results for 'peach tomato peach banana apple apple pear' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking search results for 'apple peach peach peach banana apple apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019716104050318088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015098018479525565}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011372230438267798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009202631231994461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007523643976406805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.007422256801584987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007161063022035459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.007031699459630415}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.006931815010802461}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006254547931501422}]
result = search.search('apple peach peach peach banana apple apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #350 checking search results for 'apple peach peach peach banana apple apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #350 checking search results for 'apple peach peach peach banana apple apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking search results for 'pear peach peach banana' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.020204296066447348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014718217220692251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012712990138140453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009597950024997432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008433494088456893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007776983787319279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007669447399455294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007444383114249996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00698223797987841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.0065420636686474845}]
result = search.search('pear peach peach banana',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #351 checking search results for 'pear peach peach banana' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #351 checking search results for 'pear peach peach banana' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking search results for 'peach peach banana pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01926967855314052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014812496203846892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012778192297096081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00968420027316346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008397579482082217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007741119894975234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007711489721441988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007527562527734298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006790725229491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006558209052423909}]
result = search.search('peach peach banana pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #352 checking search results for 'peach peach banana pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #352 checking search results for 'peach peach banana pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking search results for 'banana peach peach pear apple' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01926967855314052}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014812496203846892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012778192297096081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00968420027316346}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008397579482082217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007741119894975234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007711489721441988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007527562527734298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006790725229491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006558209052423909}]
result = search.search('banana peach peach pear apple',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #353 checking search results for 'banana peach peach pear apple' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #353 checking search results for 'banana peach peach pear apple' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking search results for 'banana coconut apple apple tomato apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html', 'title': 'N-934', 'score': 0.9998277296468217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 0.9991536635859016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-795.html', 'title': 'N-795', 'score': 0.9970811384783727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html', 'title': 'N-481', 'score': 0.9967397706382043}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-849.html', 'title': 'N-849', 'score': 0.9964609223078084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'title': 'N-266', 'score': 0.9960370532425886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-274.html', 'title': 'N-274', 'score': 0.9958911151645455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-704.html', 'title': 'N-704', 'score': 0.9921272628939728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.9858876885873906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-430.html', 'title': 'N-430', 'score': 0.9846510668422694}]
result = search.search('banana coconut apple apple tomato apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #354 checking search results for 'banana coconut apple apple tomato apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #354 checking search results for 'banana coconut apple apple tomato apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking search results for 'peach tomato peach pear pear peach apple coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.016868308596256508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.014716060360687627}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011749406883446563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.009425401046128646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008707594551530029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.0075413814734327025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007463944036667154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007203993602139388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006394449124864601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006346801014914379}]
result = search.search('peach tomato peach pear pear peach apple coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #355 checking search results for 'peach tomato peach pear pear peach apple coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #355 checking search results for 'peach tomato peach pear pear peach apple coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking search results for 'peach tomato apple apple peach coconut peach' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.019698403728020158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015235626288320587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.011737483735963039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.010110124218535604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.008710133071423974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.007922113738668999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007833501958353613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007374412128196229}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.006816086649784637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.00650181146347917}]
result = search.search('peach tomato apple apple peach coconut peach',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #356 checking search results for 'peach tomato apple apple peach coconut peach' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #356 checking search results for 'peach tomato apple apple peach coconut peach' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking search results for 'pear coconut peach banana peach banana banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.9952859013184676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9938605200762609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.989665784368448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html', 'title': 'N-575', 'score': 0.9894543701511022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-212.html', 'title': 'N-212', 'score': 0.988957376189587}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html', 'title': 'N-378', 'score': 0.9884812376474816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-79.html', 'title': 'N-79', 'score': 0.9880879108811514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html', 'title': 'N-144', 'score': 0.9873967756879894}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html', 'title': 'N-485', 'score': 0.9872420850236195}]
result = search.search('pear coconut peach banana peach banana banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #357 checking search results for 'pear coconut peach banana peach banana banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #357 checking search results for 'pear coconut peach banana peach banana banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking search results for 'apple peach banana coconut tomato peach tomato' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'title': 'N-1', 'score': 0.01977398413708179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'title': 'N-4', 'score': 0.015234252461753129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'title': 'N-3', 'score': 0.012477270016542323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'title': 'N-0', 'score': 0.00952913704709155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'title': 'N-9', 'score': 0.00841001043307151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'title': 'N-12', 'score': 0.007686953303701851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'title': 'N-20', 'score': 0.007640450330258488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'title': 'N-15', 'score': 0.00728941866833947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'title': 'N-6', 'score': 0.00673640939583809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'title': 'N-42', 'score': 0.006599943708842697}]
result = search.search('apple peach banana coconut tomato peach tomato',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #358 checking search results for 'apple peach banana coconut tomato peach tomato' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #358 checking search results for 'apple peach banana coconut tomato peach tomato' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking search results for 'banana apple tomato peach apple tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9999980650161844}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9989400211212546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.9986532265478112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.9977382351341291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 0.9970922893653976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9967380196032567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9967137961192949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9962169438919931}]
result = search.search('banana apple tomato peach apple tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #359 checking search results for 'banana apple tomato peach apple tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #359 checking search results for 'banana apple tomato peach apple tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking search results for 'banana banana peach banana pear peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-759.html', 'title': 'N-759', 'score': 0.9999902943127925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-378.html', 'title': 'N-378', 'score': 0.9996611497713115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9983220209117216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html', 'title': 'N-485', 'score': 0.9969501364562561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-69.html', 'title': 'N-69', 'score': 0.9948146348135776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9921366926312987}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-212.html', 'title': 'N-212', 'score': 0.9918738674617217}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-575.html', 'title': 'N-575', 'score': 0.9918583814382997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'title': 'N-877', 'score': 0.9916181570569501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-144.html', 'title': 'N-144', 'score': 0.9909462061622465}]
result = search.search('banana banana peach banana pear peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #360 checking search results for 'banana banana peach banana pear peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #360 checking search results for 'banana banana peach banana pear peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking search results for 'coconut pear coconut apple coconut banana pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9986066884907351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-750.html', 'title': 'N-750', 'score': 0.9984568890498711}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-553.html', 'title': 'N-553', 'score': 0.9969331715293914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-841.html', 'title': 'N-841', 'score': 0.9960796990123975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-953.html', 'title': 'N-953', 'score': 0.9945358594125793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.9940607904500033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html', 'title': 'N-96', 'score': 0.992144443205887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'title': 'N-406', 'score': 0.9916491988348078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-505.html', 'title': 'N-505', 'score': 0.9890603612825981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-295.html', 'title': 'N-295', 'score': 0.9883139256615674}]
result = search.search('coconut pear coconut apple coconut banana pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #361 checking search results for 'coconut pear coconut apple coconut banana pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #361 checking search results for 'coconut pear coconut apple coconut banana pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking search results for 'pear apple pear peach banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html', 'title': 'N-396', 'score': 0.9890806360794886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9885047264300872}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.988366600164914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-776.html', 'title': 'N-776', 'score': 0.9875207957747634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-672.html', 'title': 'N-672', 'score': 0.9869511937757316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.986264647737246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-473.html', 'title': 'N-473', 'score': 0.9844371577597826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-803.html', 'title': 'N-803', 'score': 0.9838896382782824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9831125929187717}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-857.html', 'title': 'N-857', 'score': 0.9820353884366378}]
result = search.search('pear apple pear peach banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #362 checking search results for 'pear apple pear peach banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #362 checking search results for 'pear apple pear peach banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking search results for 'peach pear banana apple coconut apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.996675374948493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9932636919243405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-910.html', 'title': 'N-910', 'score': 0.9930227666356}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9928409476216575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-35.html', 'title': 'N-35', 'score': 0.9922674743795924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-568.html', 'title': 'N-568', 'score': 0.9918864758328625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-152.html', 'title': 'N-152', 'score': 0.991202782948773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-615.html', 'title': 'N-615', 'score': 0.9908142968895922}]
result = search.search('peach pear banana apple coconut apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #363 checking search results for 'peach pear banana apple coconut apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #363 checking search results for 'peach pear banana apple coconut apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking search results for 'peach pear peach peach peach pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-694.html', 'title': 'N-694', 'score': 0.9998493931460103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-348.html', 'title': 'N-348', 'score': 0.9983678331333925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-80.html', 'title': 'N-80', 'score': 0.9967445819568951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-227.html', 'title': 'N-227', 'score': 0.9951746762552424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-681.html', 'title': 'N-681', 'score': 0.9949362781369919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-864.html', 'title': 'N-864', 'score': 0.9938273299537139}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html', 'title': 'N-31', 'score': 0.9934279787373661}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9928783977076031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-253.html', 'title': 'N-253', 'score': 0.9914761411906137}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-2.html', 'title': 'N-2', 'score': 0.9913648733389263}]
result = search.search('peach pear peach peach peach pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #364 checking search results for 'peach pear peach peach peach pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #364 checking search results for 'peach pear peach peach peach pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking search results for 'coconut coconut coconut apple coconut peach tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9976484887093227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.99420387762008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 0.9938817789640704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9907833009514324}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.989865400705026}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'title': 'N-937', 'score': 0.9883029125480636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'title': 'N-406', 'score': 0.9865610599574517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-750.html', 'title': 'N-750', 'score': 0.978544702268064}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html', 'title': 'N-647', 'score': 0.9711634178298849}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'title': 'N-13', 'score': 0.9701517849462036}]
result = search.search('coconut coconut coconut apple coconut peach tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #365 checking search results for 'coconut coconut coconut apple coconut peach tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #365 checking search results for 'coconut coconut coconut apple coconut peach tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking search results for 'coconut peach peach banana banana peach pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html', 'title': 'N-259', 'score': 0.9999685151065197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-441.html', 'title': 'N-441', 'score': 0.9999685151065197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-631.html', 'title': 'N-631', 'score': 0.9986608025596514}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-864.html', 'title': 'N-864', 'score': 0.9984039554963696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html', 'title': 'N-346', 'score': 0.9956653078504992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-426.html', 'title': 'N-426', 'score': 0.9947261209564278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-749.html', 'title': 'N-749', 'score': 0.9942419595124747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-161.html', 'title': 'N-161', 'score': 0.9930203624448342}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-27.html', 'title': 'N-27', 'score': 0.9925764806741882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-80.html', 'title': 'N-80', 'score': 0.9923491411984194}]
result = search.search('coconut peach peach banana banana peach pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #366 checking search results for 'coconut peach peach banana banana peach pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #366 checking search results for 'coconut peach peach banana banana peach pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking search results for 'pear tomato peach apple banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9999974862171608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999911402889735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999911402889735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9990053005161372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.9988627723210646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.9978521062566298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 0.9969892912186983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9968461258891129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9965171043285547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9964087208352386}]
result = search.search('pear tomato peach apple banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #367 checking search results for 'pear tomato peach apple banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #367 checking search results for 'pear tomato peach apple banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking search results for 'peach peach apple pear peach tomato peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-87.html', 'title': 'N-87', 'score': 0.9999794674898789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-504.html', 'title': 'N-504', 'score': 0.9996888218085658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'title': 'N-877', 'score': 0.9967127833705414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-419.html', 'title': 'N-419', 'score': 0.9957886146098942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'title': 'N-462', 'score': 0.9921638675130225}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html', 'title': 'N-537', 'score': 0.9898668322002918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html', 'title': 'N-346', 'score': 0.9888020691176551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html', 'title': 'N-466', 'score': 0.9886935183106896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-901.html', 'title': 'N-901', 'score': 0.9867593579782541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-27.html', 'title': 'N-27', 'score': 0.983915375565325}]
result = search.search('peach peach apple pear peach tomato peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #368 checking search results for 'peach peach apple pear peach tomato peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #368 checking search results for 'peach peach apple pear peach tomato peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking search results for 'pear pear pear apple peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html', 'title': 'N-833', 'score': 0.9998140517572579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html', 'title': 'N-811', 'score': 0.9996512195155354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'title': 'N-406', 'score': 0.9995074656750155}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-857.html', 'title': 'N-857', 'score': 0.9989934385524702}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html', 'title': 'N-72', 'score': 0.9978369558436115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.9972209227562014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html', 'title': 'N-394', 'score': 0.9945005976843668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html', 'title': 'N-37', 'score': 0.9941237286509459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-580.html', 'title': 'N-580', 'score': 0.9932422192889235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.993089477521124}]
result = search.search('pear pear pear apple peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #369 checking search results for 'pear pear pear apple peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #369 checking search results for 'pear pear pear apple peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking search results for 'pear tomato pear coconut apple tomato pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html', 'title': 'N-915', 'score': 0.9998495775252108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-408.html', 'title': 'N-408', 'score': 0.9998127098535567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-545.html', 'title': 'N-545', 'score': 0.9984942453792386}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-799.html', 'title': 'N-799', 'score': 0.9983905363690481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html', 'title': 'N-283', 'score': 0.9979370156742194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-990.html', 'title': 'N-990', 'score': 0.9962946523859478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-752.html', 'title': 'N-752', 'score': 0.9948123878366122}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-776.html', 'title': 'N-776', 'score': 0.9945872012968785}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-323.html', 'title': 'N-323', 'score': 0.9941105986774409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html', 'title': 'N-457', 'score': 0.9913510030899801}]
result = search.search('pear tomato pear coconut apple tomato pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #370 checking search results for 'pear tomato pear coconut apple tomato pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #370 checking search results for 'pear tomato pear coconut apple tomato pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking search results for 'tomato coconut pear pear peach peach banana pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html', 'title': 'N-481', 'score': 0.9999768319726393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html', 'title': 'N-934', 'score': 0.9999559313616946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-767.html', 'title': 'N-767', 'score': 0.9975700682468367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-707.html', 'title': 'N-707', 'score': 0.9952781820002321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html', 'title': 'N-495', 'score': 0.9942726117144203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html', 'title': 'N-173', 'score': 0.9938502516121059}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-414.html', 'title': 'N-414', 'score': 0.9935217192426341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-331.html', 'title': 'N-331', 'score': 0.9933111503835559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html', 'title': 'N-275', 'score': 0.992968863579922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-990.html', 'title': 'N-990', 'score': 0.9922592879699924}]
result = search.search('tomato coconut pear pear peach peach banana pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #371 checking search results for 'tomato coconut pear pear peach peach banana pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #371 checking search results for 'tomato coconut pear pear peach peach banana pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking search results for 'apple tomato pear coconut coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9995561228928083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9988892828640841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.998544798942508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9984716365394537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9982082457219192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9975431987597079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 0.9974897348595453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html', 'title': 'N-92', 'score': 0.9965178683287363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9964826978198248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html', 'title': 'N-296', 'score': 0.9957016562577593}]
result = search.search('apple tomato pear coconut coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #372 checking search results for 'apple tomato pear coconut coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #372 checking search results for 'apple tomato pear coconut coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking search results for 'peach apple apple apple pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-188.html', 'title': 'N-188', 'score': 0.9999945342732718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-570.html', 'title': 'N-570', 'score': 0.9995983884868404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-433.html', 'title': 'N-433', 'score': 0.9994872917882923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.9989393514240835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-781.html', 'title': 'N-781', 'score': 0.9984447037019377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-375.html', 'title': 'N-375', 'score': 0.9974094630704675}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-113.html', 'title': 'N-113', 'score': 0.9969069844919712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9968419415692983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-74.html', 'title': 'N-74', 'score': 0.996476683548252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-663.html', 'title': 'N-663', 'score': 0.9960056358567778}]
result = search.search('peach apple apple apple pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #373 checking search results for 'peach apple apple apple pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #373 checking search results for 'peach apple apple apple pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking search results for 'apple banana coconut peach pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-284.html', 'title': 'N-284', 'score': 0.997212987696787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-843.html', 'title': 'N-843', 'score': 0.9953035305484536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-313.html', 'title': 'N-313', 'score': 0.9947717205018723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-578.html', 'title': 'N-578', 'score': 0.9939714310517246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-801.html', 'title': 'N-801', 'score': 0.9938180823861388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-371.html', 'title': 'N-371', 'score': 0.9935689301516948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-558.html', 'title': 'N-558', 'score': 0.9932007882282236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-637.html', 'title': 'N-637', 'score': 0.993141120733607}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-599.html', 'title': 'N-599', 'score': 0.9927184689122273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-302.html', 'title': 'N-302', 'score': 0.9923366710923358}]
result = search.search('apple banana coconut peach pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #374 checking search results for 'apple banana coconut peach pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #374 checking search results for 'apple banana coconut peach pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking search results for 'peach pear apple pear banana pear pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-473.html', 'title': 'N-473', 'score': 0.9827014229205581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html', 'title': 'N-647', 'score': 0.978180579356188}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html', 'title': 'N-37', 'score': 0.9677265150499967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-693.html', 'title': 'N-693', 'score': 0.966745007718239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-776.html', 'title': 'N-776', 'score': 0.9643262196537744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9630479823183261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html', 'title': 'N-396', 'score': 0.954497778479551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.951277439875455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9503337329574731}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-579.html', 'title': 'N-579', 'score': 0.9480113648326042}]
result = search.search('peach pear apple pear banana pear pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #375 checking search results for 'peach pear apple pear banana pear pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #375 checking search results for 'peach pear apple pear banana pear pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking search results for 'peach apple coconut tomato pear pear pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-776.html', 'title': 'N-776', 'score': 0.9880166239372222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html', 'title': 'N-875', 'score': 0.9839284145779256}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-428.html', 'title': 'N-428', 'score': 0.9832988916377579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-48.html', 'title': 'N-48', 'score': 0.9798181941260377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'title': 'N-400', 'score': 0.9785848775932728}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html', 'title': 'N-495', 'score': 0.9784274733755718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html', 'title': 'N-275', 'score': 0.9765067864552949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-803.html', 'title': 'N-803', 'score': 0.974893756286378}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-735.html', 'title': 'N-735', 'score': 0.9746437488024118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-283.html', 'title': 'N-283', 'score': 0.974370529372957}]
result = search.search('peach apple coconut tomato pear pear pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #376 checking search results for 'peach apple coconut tomato pear pear pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #376 checking search results for 'peach apple coconut tomato pear pear pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking search results for 'coconut coconut coconut coconut banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-647.html', 'title': 'N-647', 'score': 0.999723187608747}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9988275322696596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-473.html', 'title': 'N-473', 'score': 0.9975214795320999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.9964155825850566}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 0.9961787734631828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-86.html', 'title': 'N-86', 'score': 0.9957270343824534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-916.html', 'title': 'N-916', 'score': 0.9938936935288144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-750.html', 'title': 'N-750', 'score': 0.991785778285083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9915855821457372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9907532121231901}]
result = search.search('coconut coconut coconut coconut banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #377 checking search results for 'coconut coconut coconut coconut banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #377 checking search results for 'coconut coconut coconut coconut banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking search results for 'coconut apple coconut pear banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 0.9999740603930147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9987596426690505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-86.html', 'title': 'N-86', 'score': 0.9966824378339574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9922435993126397}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.992169423338505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9921306282529503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9876319225897252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'title': 'N-176', 'score': 0.9867869732487595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-279.html', 'title': 'N-279', 'score': 0.9858958422286578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-841.html', 'title': 'N-841', 'score': 0.9838874434370635}]
result = search.search('coconut apple coconut pear banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #378 checking search results for 'coconut apple coconut pear banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #378 checking search results for 'coconut apple coconut pear banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking search results for 'pear pear peach tomato pear apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-833.html', 'title': 'N-833', 'score': 0.9999387037593074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html', 'title': 'N-811', 'score': 0.9998343948353516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-406.html', 'title': 'N-406', 'score': 0.9997314860627989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-857.html', 'title': 'N-857', 'score': 0.9985913586561219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-72.html', 'title': 'N-72', 'score': 0.9973549911672658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-214.html', 'title': 'N-214', 'score': 0.9965754422583784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-37.html', 'title': 'N-37', 'score': 0.9949792167853136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-394.html', 'title': 'N-394', 'score': 0.9937438283214644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-248.html', 'title': 'N-248', 'score': 0.9925039096730667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-580.html', 'title': 'N-580', 'score': 0.9923232269113246}]
result = search.search('pear pear peach tomato pear apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #379 checking search results for 'pear pear peach tomato pear apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #379 checking search results for 'pear pear peach tomato pear apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking search results for 'tomato coconut peach coconut banana pear coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-107.html', 'title': 'N-107', 'score': 0.9999828234269146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-634.html', 'title': 'N-634', 'score': 0.9992607840285794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-353.html', 'title': 'N-353', 'score': 0.991938022345541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9880426172513057}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9868620971341494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9861556168025143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-628.html', 'title': 'N-628', 'score': 0.9831656574862688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'title': 'N-937', 'score': 0.9813483683360322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9794519244483613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-750.html', 'title': 'N-750', 'score': 0.978222273661371}]
result = search.search('tomato coconut peach coconut banana pear coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #380 checking search results for 'tomato coconut peach coconut banana pear coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #380 checking search results for 'tomato coconut peach coconut banana pear coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking search results for 'apple pear coconut apple apple apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html', 'title': 'N-424', 'score': 0.9994805663306926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-631.html', 'title': 'N-631', 'score': 0.9976363619686609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-864.html', 'title': 'N-864', 'score': 0.9939240963007305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-426.html', 'title': 'N-426', 'score': 0.9931680666340694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-795.html', 'title': 'N-795', 'score': 0.9928049219001845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-748.html', 'title': 'N-748', 'score': 0.992599003114779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-294.html', 'title': 'N-294', 'score': 0.9901833627217341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-70.html', 'title': 'N-70', 'score': 0.9901661324340367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9890605565796662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-556.html', 'title': 'N-556', 'score': 0.9865525231919418}]
result = search.search('apple pear coconut apple apple apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #381 checking search results for 'apple pear coconut apple apple apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #381 checking search results for 'apple pear coconut apple apple apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking search results for 'pear peach peach pear pear coconut tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-481.html', 'title': 'N-481', 'score': 0.9999768319726393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-934.html', 'title': 'N-934', 'score': 0.9999559313616946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-767.html', 'title': 'N-767', 'score': 0.9975700682468367}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-707.html', 'title': 'N-707', 'score': 0.9952781820002321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-495.html', 'title': 'N-495', 'score': 0.9942726117144203}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-173.html', 'title': 'N-173', 'score': 0.993850251612106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-414.html', 'title': 'N-414', 'score': 0.9935217192426341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-331.html', 'title': 'N-331', 'score': 0.9933111503835559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-275.html', 'title': 'N-275', 'score': 0.992968863579922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-990.html', 'title': 'N-990', 'score': 0.9922592879699925}]
result = search.search('pear peach peach pear pear coconut tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #382 checking search results for 'pear peach peach pear pear coconut tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #382 checking search results for 'pear peach peach pear pear coconut tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking search results for 'banana pear peach banana pear coconut peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html', 'title': 'N-142', 'score': 0.997821573482241}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-737.html', 'title': 'N-737', 'score': 0.9977776750198905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-600.html', 'title': 'N-600', 'score': 0.9965700198063463}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-636.html', 'title': 'N-636', 'score': 0.9958427661229757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-713.html', 'title': 'N-713', 'score': 0.9956789219225559}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-116.html', 'title': 'N-116', 'score': 0.9955362770469948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-361.html', 'title': 'N-361', 'score': 0.9951005082379116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-340.html', 'title': 'N-340', 'score': 0.9944460873357251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-2.html', 'title': 'N-2', 'score': 0.9939229409026595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html', 'title': 'N-827', 'score': 0.9932161651048859}]
result = search.search('banana pear peach banana pear coconut peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #383 checking search results for 'banana pear peach banana pear coconut peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #383 checking search results for 'banana pear peach banana pear coconut peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking search results for 'pear coconut coconut peach banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9999997735308108}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999911122299762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999911122299762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9984408235572477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-127.html', 'title': 'N-127', 'score': 0.9978838759671222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9968537839795927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-935.html', 'title': 'N-935', 'score': 0.9967801905024777}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html', 'title': 'N-508', 'score': 0.9961522319260571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html', 'title': 'N-683', 'score': 0.9961290706538883}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9960927424862465}]
result = search.search('pear coconut coconut peach banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #384 checking search results for 'pear coconut coconut peach banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #384 checking search results for 'pear coconut coconut peach banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking search results for 'peach peach coconut tomato peach peach banana tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html', 'title': 'N-679', 'score': 0.9949662768906693}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-31.html', 'title': 'N-31', 'score': 0.9944118670929765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-931.html', 'title': 'N-931', 'score': 0.9926041016054887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-537.html', 'title': 'N-537', 'score': 0.988670834977421}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-462.html', 'title': 'N-462', 'score': 0.9850022029591863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-59.html', 'title': 'N-59', 'score': 0.9813074565424516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-853.html', 'title': 'N-853', 'score': 0.9785268691325684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html', 'title': 'N-457', 'score': 0.9780936020746295}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-863.html', 'title': 'N-863', 'score': 0.9770812439247676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-255.html', 'title': 'N-255', 'score': 0.976070544189624}]
result = search.search('peach peach coconut tomato peach peach banana tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #385 checking search results for 'peach peach coconut tomato peach peach banana tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #385 checking search results for 'peach peach coconut tomato peach peach banana tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking search results for 'apple tomato pear apple peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-524.html', 'title': 'N-524', 'score': 0.9999974862171608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'title': 'N-527', 'score': 0.9999911402889735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html', 'title': 'N-716', 'score': 0.9999911402889735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-133.html', 'title': 'N-133', 'score': 0.9990053005161372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-951.html', 'title': 'N-951', 'score': 0.9988627723210648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html', 'title': 'N-273', 'score': 0.9978521062566298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-715.html', 'title': 'N-715', 'score': 0.9969892912186983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-610.html', 'title': 'N-610', 'score': 0.9968461258891129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-518.html', 'title': 'N-518', 'score': 0.9965171043285547}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-217.html', 'title': 'N-217', 'score': 0.9964087208352386}]
result = search.search('apple tomato pear apple peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #386 checking search results for 'apple tomato pear apple peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #386 checking search results for 'apple tomato pear apple peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking search results for 'peach tomato apple coconut pear coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-76.html', 'title': 'N-76', 'score': 0.9995561228928082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-329.html', 'title': 'N-329', 'score': 0.9988892828640841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-105.html', 'title': 'N-105', 'score': 0.998544798942508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html', 'title': 'N-796', 'score': 0.9984716365394537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-233.html', 'title': 'N-233', 'score': 0.9982082457219194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-532.html', 'title': 'N-532', 'score': 0.9975431987597079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-354.html', 'title': 'N-354', 'score': 0.9974897348595452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-92.html', 'title': 'N-92', 'score': 0.9965178683287363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-569.html', 'title': 'N-569', 'score': 0.9964826978198248}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html', 'title': 'N-296', 'score': 0.9957016562577593}]
result = search.search('peach tomato apple coconut pear coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #387 checking search results for 'peach tomato apple coconut pear coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #387 checking search results for 'peach tomato apple coconut pear coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
