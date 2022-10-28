
import testingtools
import crawler
import searchdata
import search
output = open('fruits-incoming-links-failed.txt', 'w')
success_output = open('fruits-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')
#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-101.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-716.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-110.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-311.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-539.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-918.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-509.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-679.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-68.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-995.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-68.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-68.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-68.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-396.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-400.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-662.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-505.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-768.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-262.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-260.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-291.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-296.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-240.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-769.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-923.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-254.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-479.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-180.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-338.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-383.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-362.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-696.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-942.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-590.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-942.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-942.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-942.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-190.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-747.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-222.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-796.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-424.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-124.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-174.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-176.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-198.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-231.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-266.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-334.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-823.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-854.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-877.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-937.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-13.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-20.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-33.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-100.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-142.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-167.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-288.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-346.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-391.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-567.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-945.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-981.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-623.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-397.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-384.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-55.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-384.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-384.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-384.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-425.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-738.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-425.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-425.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-425.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-423.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-183.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-513.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-466.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-472.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-962.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-26.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-515.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-793.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-827.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-97.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-745.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-912.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-988.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-320.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-988.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-988.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-988.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-645.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-783.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-875.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-497.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-365.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-497.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-497.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-497.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-120.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-607.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-675.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-603.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-485.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-91.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-725.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-349.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-756.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-470.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-584.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-915.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-140.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-830.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-272.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-830.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-830.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-830.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-139.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-941.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-454.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-920.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-726.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-247.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-126.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-126.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-126.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-126.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-379.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-547.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-606.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-813.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-389.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-310.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-775.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-496.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-883.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-468.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-861.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-714.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-9.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-714.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-714.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-714.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-892.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-175.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-467.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-892.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-892.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-892.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-933.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-888.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-165.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-608.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-62.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-608.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-608.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-608.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-896.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-508.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-896.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-896.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-896.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-276.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-560.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-425.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-943.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-498.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-436.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-660.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-498.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-498.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-498.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-193.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-450.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-286.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-528.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-141.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-439.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-29.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-38.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-123.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-382.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-483.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-160.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-179.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-200.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-527.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-683.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-67.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-825.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-811.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-825.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-825.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-825.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-170.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-906.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-137.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-24.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-137.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-137.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-137.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-273.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-172.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-459.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-157.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-49.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-270.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-576.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits/N-277.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-835.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-938.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-969.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits/N-690.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-457.html\n\n')
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
