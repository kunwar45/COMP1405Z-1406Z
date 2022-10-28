
import testingtools
import crawler
import searchdata
import search
output = open('fruits3-incoming-links-failed.txt', 'w')
success_output = open('fruits3-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html')
#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-865.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-892.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-59.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-892.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-892.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-892.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-710.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-710.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-710.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-710.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-590.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-481.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-194.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-683.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-761.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-58.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-133.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-201.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-108.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-265.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-194.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-295.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-404.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-889.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-285.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-451.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-194.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-194.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-194.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-693.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-680.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-219.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-573.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-671.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-377.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-808.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-972.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-651.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-407.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-24.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-651.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-651.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-651.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-688.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-777.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-860.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-246.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-860.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-860.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-860.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-853.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-784.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-298.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-282.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-273.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-282.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-282.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-282.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-399.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-136.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-70.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-399.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-399.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-399.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-288.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-410.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-785.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-786.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-63.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-786.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-786.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-786.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-679.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-246.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-319.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-326.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-660.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-71.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-336.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-206.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-660.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-660.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-660.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-182.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-180.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-182.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-182.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-182.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-196.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-281.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-728.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-50.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-728.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-728.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-728.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-875.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-445.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-409.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-875.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-875.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-875.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-509.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-49.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-699.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-279.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-509.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-509.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-509.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-380.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-49.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-395.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-308.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-487.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-535.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-27.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-446.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-385.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-143.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-472.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-592.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-765.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-988.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-838.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-230.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-114.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-230.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-230.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-230.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-178.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-322.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-464.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-936.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-478.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-457.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-203.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-457.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-457.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-457.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-283.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-556.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-51.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-646.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-306.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-920.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-244.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-437.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-363.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-437.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-437.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-437.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-350.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-193.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-966.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-735.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-505.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-735.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-735.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-735.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-207.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-360.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-220.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-517.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-98.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-614.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-241.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-154.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-674.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-394.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-707.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-140.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-824.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-352.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-736.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-541.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-973.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-973.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-973.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-973.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-210.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-327.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-833.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-424.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-99.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-571.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-750.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-495.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-369.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-119.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-31.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-189.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-197.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-821.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-738.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-721.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-832.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-881.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-438.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-870.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-3.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits3/N-542.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-794.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-926.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits3/N-271.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits3/N-926.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-926.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits3/N-926.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html
expected = None
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #50 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
