
import testingtools
import crawler
import searchdata
import search
output = open('fruits4-incoming-links-failed.txt', 'w')
success_output = open('fruits4-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html')
#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-852.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-753.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-47.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-62.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-47.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-47.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-47.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-510.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-33.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-565.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-496.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-523.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-496.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-496.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-496.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-296.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-296.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-296.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-296.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-453.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-467.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-227.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-875.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-807.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-690.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-166.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-123.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-380.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-465.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-443.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-347.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-153.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-968.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-643.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-314.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-577.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-669.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-283.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-243.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-215.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-523.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-207.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-670.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-733.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-111.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-971.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-573.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-133.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-223.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-36.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-112.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-515.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-184.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-966.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-544.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-361.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-958.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-74.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-273.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-335.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-358.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-678.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-405.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-211.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-520.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-873.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-82.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-927.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-103.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-407.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-789.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-851.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-537.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-725.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-274.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-181.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-154.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-181.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-181.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-181.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-726.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-88.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-571.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-516.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-472.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-42.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-472.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-472.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-472.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-263.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-263.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-263.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-263.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-881.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-199.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-292.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-192.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-547.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-344.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-273.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-273.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-273.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-273.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-79.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-597.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-837.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-837.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-837.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-837.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-123.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-123.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-123.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-123.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-622.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-487.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-469.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-265.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-731.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-474.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-909.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-143.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-896.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-918.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-79.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-564.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-323.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html\n\n')
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
