
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')


output = open('fruits3-all-outgoing-failed.txt', 'w')
success_output = open('fruits3-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-290.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-312.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-313.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-367.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-431.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-638.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-361.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-393.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-462.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-644.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-663.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-741.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-925.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-928.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-914.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-938.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-381.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-914.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-914.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-914.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-401.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-364.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-634.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-401.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-401.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-401.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-342.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-435.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-468.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-38.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-468.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-468.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-468.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-797.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-797.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-797.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-797.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-499.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-499.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-499.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-499.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-666.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-666.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-666.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-666.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-712.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-580.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-537.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-372.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-740.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-956.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-474.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-956.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-956.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-956.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-134.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-532.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-692.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-845.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-878.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-220.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-988.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-988.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-988.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-988.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-606.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-693.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-98.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-754.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-606.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-606.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-606.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-510.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-807.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-754.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-537.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-606.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-877.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-754.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-754.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-754.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-848.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-263.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-848.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-848.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-848.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-403.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-683.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-835.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-683.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-683.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-683.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-37.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-732.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-161.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-350.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-852.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-271.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-780.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-161.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-161.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-161.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-132.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-239.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-722.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-175.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-665.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-701.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-290.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-701.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-701.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-701.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-206.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-931.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-350.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-765.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-988.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-400.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-611.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-684.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-808.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-24.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-116.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-138.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-192.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-271.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-374.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-411.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-562.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-907.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-622.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-317.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-549.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-549.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-549.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-549.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-759.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-305.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-756.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-694.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-366.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-797.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-194.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-802.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-869.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-370.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-370.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-370.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-370.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-538.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-150.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-538.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-538.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-538.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-469.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-350.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-825.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-341.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-469.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-469.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-469.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-14.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-14.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-14.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-14.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-329.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-596.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-885.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-766.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html\n\n')
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









output = open('fruits3-all-incoming-failed.txt', 'w')
success_output = open('fruits3-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-852.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-161.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-852.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-852.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-852.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-378.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-172.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-118.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-576.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-378.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-378.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-378.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-235.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-942.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-654.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-170.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-654.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-654.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-654.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-786.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-593.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-873.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-630.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-452.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-630.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-630.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-630.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-902.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-862.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-711.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-807.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-692.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-807.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-807.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-807.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-629.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-425.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-608.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-250.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-826.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-177.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-161.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-752.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-431.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-433.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-872.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-267.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-872.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-872.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-872.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-913.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-129.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-982.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-644.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-324.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-206.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-85.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-82.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-136.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-692.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-948.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-849.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-813.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-902.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-103.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-159.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-364.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-119.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-655.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-829.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-745.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-23.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-304.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-275.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-637.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-865.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-501.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-642.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-730.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-315.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-340.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-426.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-463.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-479.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-626.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-647.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-758.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-687.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-904.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-904.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-904.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-904.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-991.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-31.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-991.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-991.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-991.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-260.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-179.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-436.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-260.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-260.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-260.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-611.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-691.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-692.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-444.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-686.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-158.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-66.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-460.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-372.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-309.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-226.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-264.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-135.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-135.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-135.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-135.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-716.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-79.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-337.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-444.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-417.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-55.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-55.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-55.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-55.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-246.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-871.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-367.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-600.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-876.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-76.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-362.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-76.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-76.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-76.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-175.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-665.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-722.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-171.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-831.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-171.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-171.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-171.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-962.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-962.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-962.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-962.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-299.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-221.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-361.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-361.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-361.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-361.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-813.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-661.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-339.html\n\n')
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









output = open('fruits3-all-pagerank-failed.txt', 'w')
success_output = open('fruits3-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html
expected = 0.00037893100807835346
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-447.html
expected = 0.0006863668112428478
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-447.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-447.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-447.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-956.html
expected = 0.00037494959743370994
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-956.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-956.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-956.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html
expected = 0.0034661029235745844
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html
expected = 0.0009044154961455318
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-708.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-976.html
expected = 0.000621541107658296
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-976.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-976.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-976.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-631.html
expected = 0.001260528465897047
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-631.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-631.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-631.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-427.html
expected = 0.00038146125152760407
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-427.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-427.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-427.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-829.html
expected = 0.0009243386697290604
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-829.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-829.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-829.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html
expected = 0.0016169509524121889
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-247.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-304.html
expected = 0.000601345646285051
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-304.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-304.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-304.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html
expected = 0.0009256590108483346
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html
expected = 0.0006130484573423927
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html
expected = 0.001404807191313819
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-336.html
expected = 0.0011719893270150706
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-336.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-336.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-336.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-270.html
expected = 0.0006878141587590144
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-270.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-270.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-270.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html
expected = 0.007789147788928366
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-831.html
expected = 0.000934205008793536
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-831.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-831.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-831.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-545.html
expected = 0.00036433256450857295
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-545.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-545.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-545.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-599.html
expected = 0.0003572779895338757
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-599.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-599.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-599.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html
expected = 0.0006266525939568709
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-167.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html
expected = 0.0011669565360956748
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html
expected = 0.0008800856853953072
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html
expected = 0.0009041675735686978
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html
expected = 0.0009285858790353008
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-181.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-476.html
expected = 0.00037868825184347014
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-476.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-476.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-476.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html
expected = 0.00036154881565245985
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html
expected = 0.0009267558572206176
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html
expected = 0.00037893100807835346
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-165.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html
expected = 0.00039412951658697963
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html
expected = 0.0012416361772056223
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html
expected = 0.0007555388807594921
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html
expected = 0.00035403699436723136
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-767.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-782.html
expected = 0.0003650058299508677
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-782.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-782.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-782.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html
expected = 0.0006828198065451603
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-975.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html
expected = 0.0035020438468089795
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html
expected = 0.0006505739330362479
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-109.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-72.html
expected = 0.000871846259575672
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-72.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-72.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-72.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-790.html
expected = 0.00037868825184347014
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-790.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-790.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-790.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-641.html
expected = 0.0009630001141903188
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-641.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-641.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-641.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html
expected = 0.0003626687511863686
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-897.html
expected = 0.0006310882750023343
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-897.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-897.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-897.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html
expected = 0.00128697149153761
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html
expected = 0.0003875298668373854
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-348.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-903.html
expected = 0.0003527449742692324
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-903.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-903.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-903.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-26.html
expected = 0.002206770271072067
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-26.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-26.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-26.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-435.html
expected = 0.0017639750290319542
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-435.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-435.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-435.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-518.html
expected = 0.0006204384807875251
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-518.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-518.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-518.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-260.html
expected = 0.0006804529252609849
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-260.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-260.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-260.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-256.html
expected = 0.0007259866079278029
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-256.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-256.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-256.html\n\n')
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









output = open('fruits3-all-idf-failed.txt', 'w')
success_output = open('fruits3-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word banana
expected = 0.15842936260448298
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
expected = 0.1600404125104682
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word lime
expected = 0.20922796213800016
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word coconut
expected = 0.18114943910456646
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word pear
expected = 0.17462139610706884
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word orange
expected = 0.16812275880832706
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word fig
expected = 0.16650266314016507
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word apricot
expected = 0.16650266314016507
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word cherry
expected = 0.1600404125104682
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word kiwi
expected = 0.15842936260448298
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word blueberry
expected = 0.17136841831198113
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word apple
expected = 0.1729939903610231
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word papaya
expected = 0.1762506396917273
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #166 checking IDF for word tomato
expected = 0
result = searchdata.get_idf('tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #166 checking IDF for word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #166 checking IDF for word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits3-all-tf-failed.txt', 'w')
success_output = open('fruits3-all-tf-passed.txt', 'w')

#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apple
expected = 0.3333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word kiwi
expected = 0.3333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word papaya
expected = 0.06557377049180328
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word apricot
expected = 0.01639344262295082
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word kiwi
expected = 0.13114754098360656
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word pear
expected = 0.11475409836065574
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word blueberry
expected = 0.08196721311475409
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word fig
expected = 0.06557377049180328
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word peach
expected = 0.04918032786885246
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word cherry
expected = 0.11475409836065574
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word lime
expected = 0.08196721311475409
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-74.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word blueberry
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word fig
expected = 0.4
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word lime
expected = 0.2
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-287.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word papaya
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apricot
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apple
expected = 0.06
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word kiwi
expected = 0.14
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word pear
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word blueberry
expected = 0.06
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word fig
expected = 0.02
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word peach
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word cherry
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word lime
expected = 0.06
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-604.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word papaya
expected = 0.061224489795918366
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word apricot
expected = 0.04081632653061224
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word apple
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word kiwi
expected = 0.030612244897959183
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word pear
expected = 0.10204081632653061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word blueberry
expected = 0.10204081632653061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word fig
expected = 0.14285714285714285
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word peach
expected = 0.07142857142857142
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word cherry
expected = 0.08163265306122448
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word lime
expected = 0.04081632653061224
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-781.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word papaya
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word apricot
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word apple
expected = 0.12121212121212122
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word kiwi
expected = 0.06060606060606061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word pear
expected = 0.045454545454545456
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word blueberry
expected = 0.045454545454545456
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word fig
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word peach
expected = 0.045454545454545456
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word cherry
expected = 0.06060606060606061
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word lime
expected = 0.030303030303030304
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word papaya
expected = 0.039473684210526314
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word apricot
expected = 0.09210526315789473
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word apple
expected = 0.07894736842105263
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word kiwi
expected = 0.039473684210526314
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word pear
expected = 0.14473684210526316
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word blueberry
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word fig
expected = 0.02631578947368421
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word peach
expected = 0.07894736842105263
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word cherry
expected = 0.06578947368421052
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word lime
expected = 0.02631578947368421
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word papaya
expected = 0.06349206349206349
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word apricot
expected = 0.12698412698412698
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word apple
expected = 0.015873015873015872
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word kiwi
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word pear
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word blueberry
expected = 0.07936507936507936
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word fig
expected = 0.031746031746031744
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word peach
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word cherry
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word lime
expected = 0.031746031746031744
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-977.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word papaya
expected = 0.13157894736842105
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word apricot
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word apple
expected = 0.07894736842105263
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word pear
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word blueberry
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word fig
expected = 0.02631578947368421
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word peach
expected = 0.07894736842105263
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word cherry
expected = 0.13157894736842105
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word lime
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-689.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word apricot
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word apple
expected = 0.3076923076923077
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word kiwi
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word pear
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word peach
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word cherry
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word lime
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #282 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #287 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #287 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #287 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits3-all-tfidf-failed.txt', 'w')
success_output = open('fruits3-all-tfidf-passed.txt', 'w')

#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word lime
expected = 0.031803297480179835
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word pear
expected = 0.020164792924428732
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word coconut
expected = 0.014130111297777848
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word papaya
expected = 0.03306937933317144
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word apple
expected = 0.013493965809283838
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word fig
expected = 0.019227264232435187
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word apricot
expected = 0.01298762597983467
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word banana
expected = 0.01829498195117974
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word blueberry
expected = 0.01336716710601951
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word lime
expected = 0.021830146709322887
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word pear
expected = 0.02401105728685515
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word coconut
expected = 0.0189005274034833
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word papaya
expected = 0.006278736878359964
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word apple
expected = 0.05569162574388689
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word fig
expected = 0.01172001055056407
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word apricot
expected = 0.005931475841629924
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word banana
expected = 0.01652999051072932
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word blueberry
expected = 0.006104813064642489
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word cherry
expected = 0.02200612066258256
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-302.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word lime
expected = 0.009433647243159258
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word pear
expected = 0.011719574579420997
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word coconut
expected = 0.02753527511972982
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word papaya
expected = 0.01182891995246303
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word apple
expected = 0.01536346947207686
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word fig
expected = 0.014786979460008884
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word apricot
expected = 0.011174692344957056
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word banana
expected = 0.010632859271580456
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word blueberry
expected = 0.007726640313530874
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word cherry
expected = 0.030830997742012325
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-887.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word papaya
expected = 0.10310001494777626
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word apricot
expected = 0.09739781420720324
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word lime
expected = 0.03833512886639603
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word pear
expected = 0.01028409820442975
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word coconut
expected = 0.010668558738852701
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word papaya
expected = 0.02994939020382524
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word apple
expected = 0.007679915856382402
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word fig
expected = 0.026058413659100273
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word apricot
expected = 0.021525966620132005
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word banana
expected = 0.011604789534541278
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word blueberry
expected = 0.007607750016811468
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word cherry
expected = 0.01848102151144756
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word lime
expected = 0.0059774654941407495
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word pear
expected = 0.028550376892972316
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word coconut
expected = 0.020113259962264866
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word papaya
expected = 0.03331733247211416
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word apple
expected = 0.019207749785150115
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word fig
expected = 0.01848700920467347
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word apricot
expected = 0.004756839924419055
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word banana
expected = 0.008964492332996288
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word blueberry
expected = 0.023563761377350296
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word cherry
expected = 0.01776949703627324
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-61.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word lime
expected = 0.05042563351793139
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word coconut
expected = 0.022739848879792496
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word apple
expected = 0.0217160882052258
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word apricot
expected = 0.02090122617329653
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word banana
expected = 0.03818275958690405
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word cherry
expected = 0.020090014151503705
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-434.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word lime
expected = 0.0198006803190199
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word pear
expected = 0.01652562308519966
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word coconut
expected = 0.025311062567225092
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word papaya
expected = 0.008476649060952456
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word apple
expected = 0.0041946797816761385
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word fig
expected = 0.01191380851703155
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word apricot
expected = 0.008007827067304593
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word banana
expected = 0.01859278688680926
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word blueberry
expected = 0.03143687504504627
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word cherry
expected = 0.025886707966267408
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-200.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word lime
expected = 0.023686825316432167
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word pear
expected = 0.01976899485056172
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word coconut
expected = 0.015529918594294036
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word papaya
expected = 0.024706401901494063
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word apple
expected = 0.014830753000885507
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word apricot
expected = 0.014274252335980557
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word banana
expected = 0.022208257015975036
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word blueberry
expected = 0.014691392913901142
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word cherry
expected = 0.009236812085167285
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word lime
expected = 0.016320306627671286
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word pear
expected = 0.01800232967094602
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word coconut
expected = 0.009504443685086414
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word papaya
expected = 0.05102572647560413
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word apple
expected = 0.01783455472811631
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word fig
expected = 0.008735965140466836
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word apricot
expected = 0.008735965140466836
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word banana
expected = 0.012357888257910243
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word blueberry
expected = 0.026048529702206495
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word cherry
expected = 0.016499125141120164
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #408 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #408 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #408 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()









output = open('fruits3-all-search-failed.txt', 'w')
success_output = open('fruits3-all-search-passed.txt', 'w')

#Test #409 checking search results for 'tomato pear coconut tomato apricot orange orange kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-166.html', 'title': 'N-166', 'score': 0.9999547656038615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-990.html', 'title': 'N-990', 'score': 0.9961714921158243}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html', 'title': 'N-369', 'score': 0.9955667050538505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-483.html', 'title': 'N-483', 'score': 0.9935304355282182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.9917683853575866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-354.html', 'title': 'N-354', 'score': 0.9905920272659199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-513.html', 'title': 'N-513', 'score': 0.9901600659876848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html', 'title': 'N-704', 'score': 0.989015656104505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-894.html', 'title': 'N-894', 'score': 0.9867448769678067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-690.html', 'title': 'N-690', 'score': 0.9866234657842906}]
result = search.search('tomato pear coconut tomato apricot orange orange kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'tomato pear coconut tomato apricot orange orange kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'tomato pear coconut tomato apricot orange orange kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'papaya fig fig lime fig coconut papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-496.html', 'title': 'N-496', 'score': 0.9983965562789789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-106.html', 'title': 'N-106', 'score': 0.9979740452041481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-195.html', 'title': 'N-195', 'score': 0.9978868976073696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-328.html', 'title': 'N-328', 'score': 0.9955340686531792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-149.html', 'title': 'N-149', 'score': 0.9954187134841971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-277.html', 'title': 'N-277', 'score': 0.9952404779089357}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.994105831151501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-325.html', 'title': 'N-325', 'score': 0.9939601710757758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-422.html', 'title': 'N-422', 'score': 0.9938792955152251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-93.html', 'title': 'N-93', 'score': 0.9921344865068042}]
result = search.search('papaya fig fig lime fig coconut papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'papaya fig fig lime fig coconut papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'papaya fig fig lime fig coconut papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'blueberry fig kiwi peach apple coconut pear tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9962889288877796}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-842.html', 'title': 'N-842', 'score': 0.9962040008802802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9941023174543204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-567.html', 'title': 'N-567', 'score': 0.9917449934934163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-843.html', 'title': 'N-843', 'score': 0.9901515963761262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9895223641653489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'title': 'N-333', 'score': 0.9894137168492858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html', 'title': 'N-536', 'score': 0.9892748144069038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-360.html', 'title': 'N-360', 'score': 0.9891414934172543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.987341413668025}]
result = search.search('blueberry fig kiwi peach apple coconut pear tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'blueberry fig kiwi peach apple coconut pear tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'blueberry fig kiwi peach apple coconut pear tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'orange papaya apricot pear pear pear cherry coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-623.html', 'title': 'N-623', 'score': 0.9871402895519835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-811.html', 'title': 'N-811', 'score': 0.9801291433553527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 0.9780723049322291}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-856.html', 'title': 'N-856', 'score': 0.977526351948672}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-667.html', 'title': 'N-667', 'score': 0.976676091551023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html', 'title': 'N-303', 'score': 0.9753152640341015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 0.9749670600416982}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-895.html', 'title': 'N-895', 'score': 0.9736757172266859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 0.9719522647496189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 0.9716416849388384}]
result = search.search('orange papaya apricot pear pear pear cherry coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'orange papaya apricot pear pear pear cherry coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'orange papaya apricot pear pear pear cherry coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'fig tomato fig cherry fig tomato apple kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-722.html', 'title': 'N-722', 'score': 0.9996389566894235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-323.html', 'title': 'N-323', 'score': 0.9954054809229703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.9946602535985671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html', 'title': 'N-71', 'score': 0.9933471268604372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-788.html', 'title': 'N-788', 'score': 0.9928533594525207}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-192.html', 'title': 'N-192', 'score': 0.9902950217197678}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-76.html', 'title': 'N-76', 'score': 0.9901434452572646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-744.html', 'title': 'N-744', 'score': 0.9900670661841027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'title': 'N-677', 'score': 0.9900346243807079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-160.html', 'title': 'N-160', 'score': 0.9899961398001954}]
result = search.search('fig tomato fig cherry fig tomato apple kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'fig tomato fig cherry fig tomato apple kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'fig tomato fig cherry fig tomato apple kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'fig apricot banana fig lime peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-748.html', 'title': 'N-748', 'score': 0.9998359626682449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-677.html', 'title': 'N-677', 'score': 0.9966178236114561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html', 'title': 'N-858', 'score': 0.9961560173853488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-565.html', 'title': 'N-565', 'score': 0.9961017762682516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9938075619108858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-9.html', 'title': 'N-9', 'score': 0.9933018269520586}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-134.html', 'title': 'N-134', 'score': 0.9912859682584431}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-364.html', 'title': 'N-364', 'score': 0.9911513312317944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-746.html', 'title': 'N-746', 'score': 0.9911288981913362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-869.html', 'title': 'N-869', 'score': 0.9905802866675906}]
result = search.search('fig apricot banana fig lime peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'fig apricot banana fig lime peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'fig apricot banana fig lime peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'lime pear apricot banana coconut kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-676.html', 'title': 'N-676', 'score': 0.9999340909432677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9993736951892065}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9912007215676012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-128.html', 'title': 'N-128', 'score': 0.9909823869422107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-227.html', 'title': 'N-227', 'score': 0.990355942276633}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-170.html', 'title': 'N-170', 'score': 0.990164496022624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-208.html', 'title': 'N-208', 'score': 0.9897413080578712}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'title': 'N-16', 'score': 0.9896801302392648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'title': 'N-198', 'score': 0.9890671262790377}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html', 'title': 'N-298', 'score': 0.9877259608042962}]
result = search.search('lime pear apricot banana coconut kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'lime pear apricot banana coconut kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'lime pear apricot banana coconut kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'lime orange lime papaya lime fig kiwi apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-222.html', 'title': 'N-222', 'score': 0.9865205519372542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 0.9836181881965246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-984.html', 'title': 'N-984', 'score': 0.9834432321289223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-907.html', 'title': 'N-907', 'score': 0.9834432321289223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-393.html', 'title': 'N-393', 'score': 0.9827137915034322}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html', 'title': 'N-517', 'score': 0.982613715134885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-535.html', 'title': 'N-535', 'score': 0.9814857045365326}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9813959443887935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-327.html', 'title': 'N-327', 'score': 0.9810071740534575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-31.html', 'title': 'N-31', 'score': 0.9807268972179787}]
result = search.search('lime orange lime papaya lime fig kiwi apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'lime orange lime papaya lime fig kiwi apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'lime orange lime papaya lime fig kiwi apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'cherry cherry pear cherry cherry coconut apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-89.html', 'title': 'N-89', 'score': 0.997108900361939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.9881204272822773}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-607.html', 'title': 'N-607', 'score': 0.9825322859949434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-985.html', 'title': 'N-985', 'score': 0.9814606494009632}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-644.html', 'title': 'N-644', 'score': 0.9813082509422105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-211.html', 'title': 'N-211', 'score': 0.9812836889221954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-473.html', 'title': 'N-473', 'score': 0.9804842566608304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-149.html', 'title': 'N-149', 'score': 0.9794821736325884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-276.html', 'title': 'N-276', 'score': 0.9787864623299545}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-760.html', 'title': 'N-760', 'score': 0.9775023306467511}]
result = search.search('cherry cherry pear cherry cherry coconut apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'cherry cherry pear cherry cherry coconut apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'cherry cherry pear cherry cherry coconut apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'pear orange orange pear kiwi apricot kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'title': 'N-333', 'score': 0.9971311712600442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-293.html', 'title': 'N-293', 'score': 0.996111262392816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html', 'title': 'N-265', 'score': 0.9952843245775049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html', 'title': 'N-202', 'score': 0.9926870014385376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-186.html', 'title': 'N-186', 'score': 0.9913089219711344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-933.html', 'title': 'N-933', 'score': 0.9911848905490563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-491.html', 'title': 'N-491', 'score': 0.9907969631750381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-361.html', 'title': 'N-361', 'score': 0.988560755010518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html', 'title': 'N-281', 'score': 0.9884809382568358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html', 'title': 'N-126', 'score': 0.9875594133646179}]
result = search.search('pear orange orange pear kiwi apricot kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'pear orange orange pear kiwi apricot kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'pear orange orange pear kiwi apricot kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'orange peach coconut fig tomato peach fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.9999241261475162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-814.html', 'title': 'N-814', 'score': 0.9999080803257753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.9948929709053111}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-595.html', 'title': 'N-595', 'score': 0.9944699591535907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-455.html', 'title': 'N-455', 'score': 0.99420597857485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-729.html', 'title': 'N-729', 'score': 0.9934421173015857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-172.html', 'title': 'N-172', 'score': 0.993316167733501}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9930234189542515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html', 'title': 'N-389', 'score': 0.9869300033874456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-735.html', 'title': 'N-735', 'score': 0.9868642051539911}]
result = search.search('orange peach coconut fig tomato peach fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'orange peach coconut fig tomato peach fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'orange peach coconut fig tomato peach fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'apple kiwi blueberry papaya papaya apricot papaya cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9895837292912227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-784.html', 'title': 'N-784', 'score': 0.9885005361506595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html', 'title': 'N-566', 'score': 0.982952969095168}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-765.html', 'title': 'N-765', 'score': 0.9828462723863783}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-357.html', 'title': 'N-357', 'score': 0.9821170017922491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-175.html', 'title': 'N-175', 'score': 0.9802969045045542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 0.9793574385230278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-946.html', 'title': 'N-946', 'score': 0.9788400472400646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9783613451437246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 0.9776668714770287}]
result = search.search('apple kiwi blueberry papaya papaya apricot papaya cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'apple kiwi blueberry papaya papaya apricot papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'apple kiwi blueberry papaya papaya apricot papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'apricot pear cherry papaya pear orange banana kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-555.html', 'title': 'N-555', 'score': 0.9899687483280765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 0.9873373692584975}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-698.html', 'title': 'N-698', 'score': 0.9870576923312268}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-930.html', 'title': 'N-930', 'score': 0.9865325460198575}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-647.html', 'title': 'N-647', 'score': 0.9855404712774134}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-142.html', 'title': 'N-142', 'score': 0.9849111932324276}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9840436500136903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-126.html', 'title': 'N-126', 'score': 0.983734494340682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-506.html', 'title': 'N-506', 'score': 0.9821764668084179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.9820813091262733}]
result = search.search('apricot pear cherry papaya pear orange banana kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'apricot pear cherry papaya pear orange banana kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'apricot pear cherry papaya pear orange banana kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'apple peach banana peach cherry fig lime apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9913762659453926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-577.html', 'title': 'N-577', 'score': 0.9901845559625877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 0.9862470517182527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9860923469058526}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-840.html', 'title': 'N-840', 'score': 0.9857006628248458}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-28.html', 'title': 'N-28', 'score': 0.9856588889727856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-39.html', 'title': 'N-39', 'score': 0.9843925811802355}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 0.9827848508441533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-294.html', 'title': 'N-294', 'score': 0.9809796604939234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9802074321203355}]
result = search.search('apple peach banana peach cherry fig lime apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'apple peach banana peach cherry fig lime apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'apple peach banana peach cherry fig lime apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'blueberry cherry cherry papaya fig kiwi tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-557.html', 'title': 'N-557', 'score': 0.9998500270691216}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-817.html', 'title': 'N-817', 'score': 0.9997028673482143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html', 'title': 'N-972', 'score': 0.9947631910625103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-117.html', 'title': 'N-117', 'score': 0.9946949219519071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-408.html', 'title': 'N-408', 'score': 0.9901628003876768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-334.html', 'title': 'N-334', 'score': 0.9899835750256558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-597.html', 'title': 'N-597', 'score': 0.989920411068403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-42.html', 'title': 'N-42', 'score': 0.9898678476098376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-372.html', 'title': 'N-372', 'score': 0.9896067069937075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-147.html', 'title': 'N-147', 'score': 0.9895560203013397}]
result = search.search('blueberry cherry cherry papaya fig kiwi tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'blueberry cherry cherry papaya fig kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'blueberry cherry cherry papaya fig kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'papaya pear kiwi papaya orange kiwi papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-60.html', 'title': 'N-60', 'score': 0.9996343024346686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-468.html', 'title': 'N-468', 'score': 0.99957178342236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-947.html', 'title': 'N-947', 'score': 0.99957178342236}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-691.html', 'title': 'N-691', 'score': 0.9976901965467784}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-550.html', 'title': 'N-550', 'score': 0.9972550686050383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-304.html', 'title': 'N-304', 'score': 0.9966982320779546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html', 'title': 'N-824', 'score': 0.9965842133465644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-917.html', 'title': 'N-917', 'score': 0.9954425983325945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 0.9940874642889098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-729.html', 'title': 'N-729', 'score': 0.9940260621548492}]
result = search.search('papaya pear kiwi papaya orange kiwi papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'papaya pear kiwi papaya orange kiwi papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'papaya pear kiwi papaya orange kiwi papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'apple apricot peach kiwi tomato orange tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.9986629870798831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 0.9972605990166152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 0.9963537462476645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9961501064759409}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-789.html', 'title': 'N-789', 'score': 0.9952298162702385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9948401952077705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9946795081965989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html', 'title': 'N-527', 'score': 0.9943759155865228}]
result = search.search('apple apricot peach kiwi tomato orange tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'apple apricot peach kiwi tomato orange tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'apple apricot peach kiwi tomato orange tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'banana orange lime blueberry peach peach kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html', 'title': 'N-409', 'score': 0.9942643382108564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-84.html', 'title': 'N-84', 'score': 0.9924069452080752}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-430.html', 'title': 'N-430', 'score': 0.9919341937861988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'title': 'N-99', 'score': 0.9918190876185186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9918132187947597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9916911279211226}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9915901495453368}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html', 'title': 'N-706', 'score': 0.98951479784347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-386.html', 'title': 'N-386', 'score': 0.9893349069340605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html', 'title': 'N-180', 'score': 0.9852745695114803}]
result = search.search('banana orange lime blueberry peach peach kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'banana orange lime blueberry peach peach kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'banana orange lime blueberry peach peach kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'coconut apple coconut orange coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-303.html', 'title': 'N-303', 'score': 0.9997158926608921}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-535.html', 'title': 'N-535', 'score': 0.9996759577237758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-578.html', 'title': 'N-578', 'score': 0.9996458870079801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-346.html', 'title': 'N-346', 'score': 0.9995594495356823}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-793.html', 'title': 'N-793', 'score': 0.9995128476101605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-454.html', 'title': 'N-454', 'score': 0.9989232200316449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-428.html', 'title': 'N-428', 'score': 0.9989037731878786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-624.html', 'title': 'N-624', 'score': 0.9987571555987109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-710.html', 'title': 'N-710', 'score': 0.9986884207797935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-981.html', 'title': 'N-981', 'score': 0.9986502927937638}]
result = search.search('coconut apple coconut orange coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'coconut apple coconut orange coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'coconut apple coconut orange coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'apricot cherry apple coconut peach orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 0.9999999999999999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9985352218100524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 0.9977164269864582}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9963430847313656}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 0.994661468807904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-628.html', 'title': 'N-628', 'score': 0.9946134520693758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html', 'title': 'N-127', 'score': 0.9941830483372616}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-121.html', 'title': 'N-121', 'score': 0.9937762016867495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-392.html', 'title': 'N-392', 'score': 0.9925210077367673}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9919924485805811}]
result = search.search('apricot cherry apple coconut peach orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'apricot cherry apple coconut peach orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'apricot cherry apple coconut peach orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'kiwi kiwi lime coconut cherry kiwi orange apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-682.html', 'title': 'N-682', 'score': 0.992750805890681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-459.html', 'title': 'N-459', 'score': 0.9911462248216822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-569.html', 'title': 'N-569', 'score': 0.990325775999444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-602.html', 'title': 'N-602', 'score': 0.9860572035944923}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-845.html', 'title': 'N-845', 'score': 0.9860474817199488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-237.html', 'title': 'N-237', 'score': 0.9855197990163628}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-964.html', 'title': 'N-964', 'score': 0.983690671261563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9809462212105723}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-189.html', 'title': 'N-189', 'score': 0.978784315837503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html', 'title': 'N-699', 'score': 0.9782061339976634}]
result = search.search('kiwi kiwi lime coconut cherry kiwi orange apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'kiwi kiwi lime coconut cherry kiwi orange apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'kiwi kiwi lime coconut cherry kiwi orange apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'banana papaya blueberry lime tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-188.html', 'title': 'N-188', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-375.html', 'title': 'N-375', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'title': 'N-48', 'score': 0.997920298201408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html', 'title': 'N-966', 'score': 0.997292993240541}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-453.html', 'title': 'N-453', 'score': 0.9968138985782269}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.996197499075235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-706.html', 'title': 'N-706', 'score': 0.9961618394033935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 0.9960305035049897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html', 'title': 'N-957', 'score': 0.9939021491810179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-921.html', 'title': 'N-921', 'score': 0.9937768578652273}]
result = search.search('banana papaya blueberry lime tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'banana papaya blueberry lime tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'banana papaya blueberry lime tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'blueberry pear pear papaya coconut coconut orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 0.991320060701282}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-275.html', 'title': 'N-275', 'score': 0.9903260423893389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html', 'title': 'N-972', 'score': 0.9890080191290943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-681.html', 'title': 'N-681', 'score': 0.9883074971082029}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'title': 'N-34', 'score': 0.986984761144816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-443.html', 'title': 'N-443', 'score': 0.9869768787477337}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-430.html', 'title': 'N-430', 'score': 0.9866945479141838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-847.html', 'title': 'N-847', 'score': 0.9865073540850732}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-612.html', 'title': 'N-612', 'score': 0.9843492495750928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-215.html', 'title': 'N-215', 'score': 0.9837241141798625}]
result = search.search('blueberry pear pear papaya coconut coconut orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'blueberry pear pear papaya coconut coconut orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'blueberry pear pear papaya coconut coconut orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'banana blueberry apple blueberry apple lime pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-980.html', 'title': 'N-980', 'score': 0.9994117700531201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-641.html', 'title': 'N-641', 'score': 0.997413406532555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 0.9959589995117643}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-253.html', 'title': 'N-253', 'score': 0.9938184923667802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html', 'title': 'N-489', 'score': 0.9937609290426279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-757.html', 'title': 'N-757', 'score': 0.9935275432137467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-504.html', 'title': 'N-504', 'score': 0.992047435487629}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-67.html', 'title': 'N-67', 'score': 0.9912831922099917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-573.html', 'title': 'N-573', 'score': 0.9906675940458698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html', 'title': 'N-936', 'score': 0.9903549954032865}]
result = search.search('banana blueberry apple blueberry apple lime pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'banana blueberry apple blueberry apple lime pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'banana blueberry apple blueberry apple lime pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'cherry banana apricot peach tomato lime blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-529.html', 'title': 'N-529', 'score': 0.9944329777668239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9940715735785046}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-544.html', 'title': 'N-544', 'score': 0.9938466100638075}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.9933711109191466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9922219660105815}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-507.html', 'title': 'N-507', 'score': 0.9921009869686884}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.991622612869553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-391.html', 'title': 'N-391', 'score': 0.9901613244332828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html', 'title': 'N-854', 'score': 0.9896616013911612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-144.html', 'title': 'N-144', 'score': 0.9896344769660136}]
result = search.search('cherry banana apricot peach tomato lime blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'cherry banana apricot peach tomato lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'cherry banana apricot peach tomato lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'blueberry pear apple pear cherry fig pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-155.html', 'title': 'N-155', 'score': 0.9934379583655766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-548.html', 'title': 'N-548', 'score': 0.9893759614176596}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-358.html', 'title': 'N-358', 'score': 0.9890362435749941}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-338.html', 'title': 'N-338', 'score': 0.9832931383872637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-888.html', 'title': 'N-888', 'score': 0.9800690254368838}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html', 'title': 'N-178', 'score': 0.9799084563857974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-365.html', 'title': 'N-365', 'score': 0.9789318306773395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html', 'title': 'N-720', 'score': 0.9765327229050258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-107.html', 'title': 'N-107', 'score': 0.9763365432967802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'title': 'N-100', 'score': 0.9749582388132639}]
result = search.search('blueberry pear apple pear cherry fig pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'blueberry pear apple pear cherry fig pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'blueberry pear apple pear cherry fig pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'apple coconut blueberry peach apple coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-132.html', 'title': 'N-132', 'score': 0.9985805412695428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-14.html', 'title': 'N-14', 'score': 0.9979828590367105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-528.html', 'title': 'N-528', 'score': 0.9976625546280793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-270.html', 'title': 'N-270', 'score': 0.9959573947281978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-612.html', 'title': 'N-612', 'score': 0.9956251540474876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-782.html', 'title': 'N-782', 'score': 0.9950874247169736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html', 'title': 'N-377', 'score': 0.9939150703618835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-290.html', 'title': 'N-290', 'score': 0.9934363949288098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html', 'title': 'N-541', 'score': 0.9934334989054819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-539.html', 'title': 'N-539', 'score': 0.9934099347512636}]
result = search.search('apple coconut blueberry peach apple coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'apple coconut blueberry peach apple coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'apple coconut blueberry peach apple coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'fig lime coconut cherry banana pear papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 0.9950901234696283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-88.html', 'title': 'N-88', 'score': 0.9878109846446916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html', 'title': 'N-618', 'score': 0.9866420431674272}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-827.html', 'title': 'N-827', 'score': 0.9855345358603544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-157.html', 'title': 'N-157', 'score': 0.9855176853439287}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-860.html', 'title': 'N-860', 'score': 0.9849972461350478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html', 'title': 'N-824', 'score': 0.9846484612657811}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9840637276397132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-734.html', 'title': 'N-734', 'score': 0.9837440541502978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html', 'title': 'N-478', 'score': 0.9816095928848723}]
result = search.search('fig lime coconut cherry banana pear papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'fig lime coconut cherry banana pear papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'fig lime coconut cherry banana pear papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'fig kiwi apricot peach cherry pear coconut papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9983542573305293}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-560.html', 'title': 'N-560', 'score': 0.9929269674944626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-536.html', 'title': 'N-536', 'score': 0.9924031840698085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-360.html', 'title': 'N-360', 'score': 0.990917628168209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-886.html', 'title': 'N-886', 'score': 0.9896505343406599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html', 'title': 'N-445', 'score': 0.9881455205403992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-715.html', 'title': 'N-715', 'score': 0.9876038039404619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-776.html', 'title': 'N-776', 'score': 0.9864370824757384}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.9859088386113701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.9858398943546391}]
result = search.search('fig kiwi apricot peach cherry pear coconut papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'fig kiwi apricot peach cherry pear coconut papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'fig kiwi apricot peach cherry pear coconut papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'banana papaya orange lime kiwi apricot kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-375.html', 'title': 'N-375', 'score': 0.9998198774931611}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-54.html', 'title': 'N-54', 'score': 0.9966346601705572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-879.html', 'title': 'N-879', 'score': 0.9965627105476922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9948977122509232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-275.html', 'title': 'N-275', 'score': 0.9925532333814945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-389.html', 'title': 'N-389', 'score': 0.9903526507144049}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-578.html', 'title': 'N-578', 'score': 0.9896854605553649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-508.html', 'title': 'N-508', 'score': 0.988505725404689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-489.html', 'title': 'N-489', 'score': 0.9869008237170909}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-127.html', 'title': 'N-127', 'score': 0.9864712879676474}]
result = search.search('banana papaya orange lime kiwi apricot kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'banana papaya orange lime kiwi apricot kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'banana papaya orange lime kiwi apricot kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'papaya papaya coconut papaya pear cherry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html', 'title': 'N-736', 'score': 0.999374308874916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-205.html', 'title': 'N-205', 'score': 0.9888293932578753}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9885083135096563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-800.html', 'title': 'N-800', 'score': 0.9874393644499366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-522.html', 'title': 'N-522', 'score': 0.9870286735633755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-566.html', 'title': 'N-566', 'score': 0.9843053425759977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-359.html', 'title': 'N-359', 'score': 0.982226677180557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html', 'title': 'N-680', 'score': 0.9818681005198938}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-363.html', 'title': 'N-363', 'score': 0.9816543226259136}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-353.html', 'title': 'N-353', 'score': 0.9811253089686282}]
result = search.search('papaya papaya coconut papaya pear cherry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'papaya papaya coconut papaya pear cherry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'papaya papaya coconut papaya pear cherry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'blueberry lime blueberry apple blueberry lime banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-922.html', 'title': 'N-922', 'score': 0.9997133007380048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-739.html', 'title': 'N-739', 'score': 0.9978009691191145}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-341.html', 'title': 'N-341', 'score': 0.9971755777146644}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-275.html', 'title': 'N-275', 'score': 0.9968130686072088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-919.html', 'title': 'N-919', 'score': 0.9952140184931353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-949.html', 'title': 'N-949', 'score': 0.9948962830544821}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-169.html', 'title': 'N-169', 'score': 0.9939966708548695}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-110.html', 'title': 'N-110', 'score': 0.9933571737310978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-435.html', 'title': 'N-435', 'score': 0.9924216887741159}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html', 'title': 'N-579', 'score': 0.9920576826107073}]
result = search.search('blueberry lime blueberry apple blueberry lime banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'blueberry lime blueberry apple blueberry lime banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'blueberry lime blueberry apple blueberry lime banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'papaya coconut papaya banana papaya peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-398.html', 'title': 'N-398', 'score': 0.9948771312458663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html', 'title': 'N-484', 'score': 0.9946293844835967}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-383.html', 'title': 'N-383', 'score': 0.9943694396168621}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-831.html', 'title': 'N-831', 'score': 0.9920183699988537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-220.html', 'title': 'N-220', 'score': 0.9907983779415023}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-669.html', 'title': 'N-669', 'score': 0.9906428652750877}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-778.html', 'title': 'N-778', 'score': 0.9904134656546595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-262.html', 'title': 'N-262', 'score': 0.9900956570980202}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-640.html', 'title': 'N-640', 'score': 0.9895009727966636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html', 'title': 'N-478', 'score': 0.9894296393313845}]
result = search.search('papaya coconut papaya banana papaya peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'papaya coconut papaya banana papaya peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'papaya coconut papaya banana papaya peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'orange kiwi apricot peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-416.html', 'title': 'N-416', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html', 'title': 'N-193', 'score': 0.9986629870798833}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 0.9972605990166152}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 0.9963537462476645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9961501064759408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-789.html', 'title': 'N-789', 'score': 0.9952298162702385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-351.html', 'title': 'N-351', 'score': 0.9948401952077705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9946795081965989}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-527.html', 'title': 'N-527', 'score': 0.9943759155865229}]
result = search.search('orange kiwi apricot peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'orange kiwi apricot peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'orange kiwi apricot peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'pear cherry coconut pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-938.html', 'title': 'N-938', 'score': 0.9996620091892983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 0.9996349753187103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-623.html', 'title': 'N-623', 'score': 0.9992748113850047}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 0.9991893067822184}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-874.html', 'title': 'N-874', 'score': 0.9991281009884564}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-932.html', 'title': 'N-932', 'score': 0.9988320286616778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-162.html', 'title': 'N-162', 'score': 0.9981113605211873}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-912.html', 'title': 'N-912', 'score': 0.9975713058149208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-957.html', 'title': 'N-957', 'score': 0.9975399876502871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-548.html', 'title': 'N-548', 'score': 0.9972336362435874}]
result = search.search('pear cherry coconut pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'pear cherry coconut pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'pear cherry coconut pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'apple banana lime orange blueberry coconut apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.9998656101699948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-212.html', 'title': 'N-212', 'score': 0.9933768297437298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-615.html', 'title': 'N-615', 'score': 0.992341850050667}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-854.html', 'title': 'N-854', 'score': 0.9907097426363705}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-852.html', 'title': 'N-852', 'score': 0.990553057701253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-152.html', 'title': 'N-152', 'score': 0.9894801351002772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-743.html', 'title': 'N-743', 'score': 0.9889564956740072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-822.html', 'title': 'N-822', 'score': 0.9885213817401751}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-144.html', 'title': 'N-144', 'score': 0.9850772533099516}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-497.html', 'title': 'N-497', 'score': 0.9849191480546741}]
result = search.search('apple banana lime orange blueberry coconut apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'apple banana lime orange blueberry coconut apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'apple banana lime orange blueberry coconut apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'peach papaya apple pear pear blueberry fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'title': 'N-100', 'score': 0.9927355695576263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-77.html', 'title': 'N-77', 'score': 0.9908755181995318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-307.html', 'title': 'N-307', 'score': 0.988620864858706}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 0.9874213911885994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.9873671272376577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-482.html', 'title': 'N-482', 'score': 0.9865929527762952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-90.html', 'title': 'N-90', 'score': 0.9864290942407166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-56.html', 'title': 'N-56', 'score': 0.985162792290976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-865.html', 'title': 'N-865', 'score': 0.9850526793651847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-681.html', 'title': 'N-681', 'score': 0.9848573393870177}]
result = search.search('peach papaya apple pear pear blueberry fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'peach papaya apple pear pear blueberry fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'peach papaya apple pear pear blueberry fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'peach apple papaya pear apple fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-272.html', 'title': 'N-272', 'score': 0.9991958281572512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-573.html', 'title': 'N-573', 'score': 0.9969523924972338}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-177.html', 'title': 'N-177', 'score': 0.9967686033479952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html', 'title': 'N-59', 'score': 0.9937897618229651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9937204749026939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-553.html', 'title': 'N-553', 'score': 0.9931788720042113}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html', 'title': 'N-279', 'score': 0.9931777221026812}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-950.html', 'title': 'N-950', 'score': 0.9925760135197551}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-42.html', 'title': 'N-42', 'score': 0.9923688727217432}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-112.html', 'title': 'N-112', 'score': 0.9917407432301445}]
result = search.search('peach apple papaya pear apple fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'peach apple papaya pear apple fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'peach apple papaya pear apple fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'banana cherry peach papaya orange papaya peach peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-658.html', 'title': 'N-658', 'score': 0.9982053886198963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html', 'title': 'N-481', 'score': 0.9920835789139683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-579.html', 'title': 'N-579', 'score': 0.991646818332208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-172.html', 'title': 'N-172', 'score': 0.9905088227816805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-259.html', 'title': 'N-259', 'score': 0.9904032863524314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.9895057494386714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-125.html', 'title': 'N-125', 'score': 0.9892465603917459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html', 'title': 'N-154', 'score': 0.98702413069239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-994.html', 'title': 'N-994', 'score': 0.9858976934166112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.9857360744621828}]
result = search.search('banana cherry peach papaya orange papaya peach peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'banana cherry peach papaya orange papaya peach peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'banana cherry peach papaya orange papaya peach peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'apple tomato coconut lime apple coconut orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-638.html', 'title': 'N-638', 'score': 0.9998540402985843}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-331.html', 'title': 'N-331', 'score': 0.9979292264847063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-460.html', 'title': 'N-460', 'score': 0.9977733877284908}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 0.9974105578981464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-280.html', 'title': 'N-280', 'score': 0.9969810817289301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-177.html', 'title': 'N-177', 'score': 0.9968767947788132}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html', 'title': 'N-377', 'score': 0.9968520739368284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-187.html', 'title': 'N-187', 'score': 0.9967624042752907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-791.html', 'title': 'N-791', 'score': 0.9966496388640234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-184.html', 'title': 'N-184', 'score': 0.9956284056004546}]
result = search.search('apple tomato coconut lime apple coconut orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'apple tomato coconut lime apple coconut orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'apple tomato coconut lime apple coconut orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'orange apple fig peach cherry tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-993.html', 'title': 'N-993', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-895.html', 'title': 'N-895', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-492.html', 'title': 'N-492', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-768.html', 'title': 'N-768', 'score': 0.9989802542631219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9982574526508875}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-452.html', 'title': 'N-452', 'score': 0.9979929174530294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-841.html', 'title': 'N-841', 'score': 0.9979031102557258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-639.html', 'title': 'N-639', 'score': 0.9972762038897213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-333.html', 'title': 'N-333', 'score': 0.9964785024019192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-893.html', 'title': 'N-893', 'score': 0.9960002817819492}]
result = search.search('orange apple fig peach cherry tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'orange apple fig peach cherry tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'orange apple fig peach cherry tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'orange lime apricot blueberry banana peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9992950070662953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-198.html', 'title': 'N-198', 'score': 0.9943163518182906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-92.html', 'title': 'N-92', 'score': 0.9922458871484524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-696.html', 'title': 'N-696', 'score': 0.9918078979551864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-659.html', 'title': 'N-659', 'score': 0.9882765868988304}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-484.html', 'title': 'N-484', 'score': 0.9873191014935032}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-681.html', 'title': 'N-681', 'score': 0.9869649432990266}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-783.html', 'title': 'N-783', 'score': 0.9868992090850327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html', 'title': 'N-972', 'score': 0.9868161370074828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-157.html', 'title': 'N-157', 'score': 0.9858130068476396}]
result = search.search('orange lime apricot blueberry banana peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'orange lime apricot blueberry banana peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'orange lime apricot blueberry banana peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'tomato pear cherry peach papaya lime pear blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'title': 'N-652', 'score': 0.9999280950792953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-14.html', 'title': 'N-14', 'score': 0.9921985308086235}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-225.html', 'title': 'N-225', 'score': 0.9909418844711118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-720.html', 'title': 'N-720', 'score': 0.9907470547373454}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-987.html', 'title': 'N-987', 'score': 0.9903042788908006}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.9901223706838829}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-511.html', 'title': 'N-511', 'score': 0.9887308957561212}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-176.html', 'title': 'N-176', 'score': 0.9874284042218091}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-391.html', 'title': 'N-391', 'score': 0.9832497483852572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-94.html', 'title': 'N-94', 'score': 0.9827223490890669}]
result = search.search('tomato pear cherry peach papaya lime pear blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'tomato pear cherry peach papaya lime pear blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'tomato pear cherry peach papaya lime pear blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'banana fig coconut apple papaya fig tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-412.html', 'title': 'N-412', 'score': 0.9999151391561246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-525.html', 'title': 'N-525', 'score': 0.9998808474973323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-594.html', 'title': 'N-594', 'score': 0.9947268725973044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-858.html', 'title': 'N-858', 'score': 0.9932830180972625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-807.html', 'title': 'N-807', 'score': 0.9898437484993493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-131.html', 'title': 'N-131', 'score': 0.9895634614923624}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-388.html', 'title': 'N-388', 'score': 0.9895397003475775}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'title': 'N-143', 'score': 0.9895354481978945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-891.html', 'title': 'N-891', 'score': 0.9870215780327279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-867.html', 'title': 'N-867', 'score': 0.986543504659705}]
result = search.search('banana fig coconut apple papaya fig tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'banana fig coconut apple papaya fig tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'banana fig coconut apple papaya fig tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'blueberry blueberry kiwi banana blueberry cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html', 'title': 'N-680', 'score': 0.9968893982439194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-863.html', 'title': 'N-863', 'score': 0.992127267363571}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-304.html', 'title': 'N-304', 'score': 0.9917787137963663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-949.html', 'title': 'N-949', 'score': 0.9907755335907826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-158.html', 'title': 'N-158', 'score': 0.9884989385918239}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-598.html', 'title': 'N-598', 'score': 0.9880243502416772}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-460.html', 'title': 'N-460', 'score': 0.9862550085252311}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-976.html', 'title': 'N-976', 'score': 0.9831062042559404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-568.html', 'title': 'N-568', 'score': 0.9830621901896626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html', 'title': 'N-35', 'score': 0.9817259922822965}]
result = search.search('blueberry blueberry kiwi banana blueberry cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'blueberry blueberry kiwi banana blueberry cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'blueberry blueberry kiwi banana blueberry cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'tomato apple cherry lime coconut apricot lime blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-500.html', 'title': 'N-500', 'score': 0.9981120345918532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-101.html', 'title': 'N-101', 'score': 0.9951982915732476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-673.html', 'title': 'N-673', 'score': 0.9941879601422684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-885.html', 'title': 'N-885', 'score': 0.9940224455859281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html', 'title': 'N-202', 'score': 0.9937745127530867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html', 'title': 'N-244', 'score': 0.9931359624371491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 0.9915300080225082}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-102.html', 'title': 'N-102', 'score': 0.9866116959727088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-704.html', 'title': 'N-704', 'score': 0.986517567038166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-979.html', 'title': 'N-979', 'score': 0.9860313871494794}]
result = search.search('tomato apple cherry lime coconut apricot lime blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'tomato apple cherry lime coconut apricot lime blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'tomato apple cherry lime coconut apricot lime blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'coconut cherry papaya blueberry apricot papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-292.html', 'title': 'N-292', 'score': 0.9997815725284819}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9957673174783234}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-618.html', 'title': 'N-618', 'score': 0.9956846302822302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-906.html', 'title': 'N-906', 'score': 0.9949079465947726}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-202.html', 'title': 'N-202', 'score': 0.9945928907669885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'title': 'N-99', 'score': 0.9938146460746323}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html', 'title': 'N-478', 'score': 0.9929570003790558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-797.html', 'title': 'N-797', 'score': 0.9924519390462299}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-396.html', 'title': 'N-396', 'score': 0.992084636738618}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-572.html', 'title': 'N-572', 'score': 0.9920721410546381}]
result = search.search('coconut cherry papaya blueberry apricot papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'coconut cherry papaya blueberry apricot papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'coconut cherry papaya blueberry apricot papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'banana kiwi banana apricot peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-846.html', 'title': 'N-846', 'score': 0.9997738529009353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-868.html', 'title': 'N-868', 'score': 0.9997738529009353}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-89.html', 'title': 'N-89', 'score': 0.9996317934812864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-212.html', 'title': 'N-212', 'score': 0.9996199427462161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-485.html', 'title': 'N-485', 'score': 0.9995114933477262}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-311.html', 'title': 'N-311', 'score': 0.998213600343025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-787.html', 'title': 'N-787', 'score': 0.9978266982403061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-967.html', 'title': 'N-967', 'score': 0.9972833504935427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-809.html', 'title': 'N-809', 'score': 0.9968090754489252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-988.html', 'title': 'N-988', 'score': 0.9966249956210605}]
result = search.search('banana kiwi banana apricot peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'banana kiwi banana apricot peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'banana kiwi banana apricot peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'apple papaya banana lime cherry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-652.html', 'title': 'N-652', 'score': 0.9998126193778536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-586.html', 'title': 'N-586', 'score': 0.9994896614302778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html', 'title': 'N-699', 'score': 0.9951618521642792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-855.html', 'title': 'N-855', 'score': 0.9941548672510486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html', 'title': 'N-571', 'score': 0.9937602238538679}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-569.html', 'title': 'N-569', 'score': 0.9937358298052366}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.9928429472971261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-958.html', 'title': 'N-958', 'score': 0.9906521797499735}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-884.html', 'title': 'N-884', 'score': 0.990438277580584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-310.html', 'title': 'N-310', 'score': 0.9901332665528373}]
result = search.search('apple papaya banana lime cherry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'apple papaya banana lime cherry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'apple papaya banana lime cherry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'apricot papaya blueberry coconut coconut tomato tomato papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-86.html', 'title': 'N-86', 'score': 0.9999501969369837}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-113.html', 'title': 'N-113', 'score': 0.9991723790779793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-76.html', 'title': 'N-76', 'score': 0.9981536164703935}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-833.html', 'title': 'N-833', 'score': 0.9981077837123914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-584.html', 'title': 'N-584', 'score': 0.9980873022371808}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-248.html', 'title': 'N-248', 'score': 0.997398637491127}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-11.html', 'title': 'N-11', 'score': 0.9968943167787175}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-769.html', 'title': 'N-769', 'score': 0.9964580652459927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-199.html', 'title': 'N-199', 'score': 0.9963740531984361}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-944.html', 'title': 'N-944', 'score': 0.996349108296497}]
result = search.search('apricot papaya blueberry coconut coconut tomato tomato papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'apricot papaya blueberry coconut coconut tomato tomato papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'apricot papaya blueberry coconut coconut tomato tomato papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'apple tomato fig lime lime apricot' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-6.html', 'title': 'N-6', 'score': 0.018597775510852496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'title': 'N-0', 'score': 0.01448143924180104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'title': 'N-5', 'score': 0.011609374522719552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-25.html', 'title': 'N-25', 'score': 0.009869917680238285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-4.html', 'title': 'N-4', 'score': 0.009310117901697192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'title': 'N-64', 'score': 0.007958242763284572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'title': 'N-2', 'score': 0.0063374280316804595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'title': 'N-3', 'score': 0.006314007203132737}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'title': 'N-7', 'score': 0.006126736120350534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-41.html', 'title': 'N-41', 'score': 0.006018874146809867}]
result = search.search('apple tomato fig lime lime apricot',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'apple tomato fig lime lime apricot' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'apple tomato fig lime lime apricot' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
