
import testingtools
import crawler
import searchdata
import search
output = open('fruits5-incoming-links-failed.txt', 'w')
success_output = open('fruits5-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')
#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-549.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-434.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-957.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-999.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-529.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-183.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-285.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-227.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-886.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-886.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-886.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-886.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-557.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-557.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-557.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-557.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-783.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-783.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-783.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-783.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-546.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-546.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-546.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-546.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-5.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-508.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-5.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-5.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-5.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-618.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-618.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-618.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-618.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-102.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-901.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-444.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-813.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-444.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-444.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-444.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-317.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-317.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-317.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-317.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-418.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-418.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-418.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-418.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-494.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-346.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-494.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-494.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-494.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-582.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-926.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-991.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-99.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-592.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-376.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-851.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-38.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-197.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-851.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-851.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-851.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-165.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-165.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-165.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-165.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-156.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-156.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-156.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-156.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-749.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-749.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-749.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-749.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-340.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-951.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-36.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-526.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-569.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-660.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-569.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-569.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-569.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-551.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-776.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-524.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-313.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-524.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-524.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-524.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-431.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-431.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-431.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-431.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-497.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-100.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-313.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-571.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-583.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-524.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-313.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-313.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-313.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-269.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-134.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-907.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-849.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-381.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-441.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-339.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-115.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-716.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-222.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-897.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-837.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-186.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-517.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-643.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-703.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-216.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-216.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-216.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-216.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-246.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-470.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-461.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-375.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-449.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-363.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-630.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-457.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-556.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-872.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-613.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-561.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-646.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-868.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-997.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-929.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-933.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-935.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-715.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-447.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html\n\n')
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
