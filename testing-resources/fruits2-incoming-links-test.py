
import testingtools
import crawler
import searchdata
import search
output = open('fruits2-incoming-links-failed.txt', 'w')
success_output = open('fruits2-incoming-links-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html')
#Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-444.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-266.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-35.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-161.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-89.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-397.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-45.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-443.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-805.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-323.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-441.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-760.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-392.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-459.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-669.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-799.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-420.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-673.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-777.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-812.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-556.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-267.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-556.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-556.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-556.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-109.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-192.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-679.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-12.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-259.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-888.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-343.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-888.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-888.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-888.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-236.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-512.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-236.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-236.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-236.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-51.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-686.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-524.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-630.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-865.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-51.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-51.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-51.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-66.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-183.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-45.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-128.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-164.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-283.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-551.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-587.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-636.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-677.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-856.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-935.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-941.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-150.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-281.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-997.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-66.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-66.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-66.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-526.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-541.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-535.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-782.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-657.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-549.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-657.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-657.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-657.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-396.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-506.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-396.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-396.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-396.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-118.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-56.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-118.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-118.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-118.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-288.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-83.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-487.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-338.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-839.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-125.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-848.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-826.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-839.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-839.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-839.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-709.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-20.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-709.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-709.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-709.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-439.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-691.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-157.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-726.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-439.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-439.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-439.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-386.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-748.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-499.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-651.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-499.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-499.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-499.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-549.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-193.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-720.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-88.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-110.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-566.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-60.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-566.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-566.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-566.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-360.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-48.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-159.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-67.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-346.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-202.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-67.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-67.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-67.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-423.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-423.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-423.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-423.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-863.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-52.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-185.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-583.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-86.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-310.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-629.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-325.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-6.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-325.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-325.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-325.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-98.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-77.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-131.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-747.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-651.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-786.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-308.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-458.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-560.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-850.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-884.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-98.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-98.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-98.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-476.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-537.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-476.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-476.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-476.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-787.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-787.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-787.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-787.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-212.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-642.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-114.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-290.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-168.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-168.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-168.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-168.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-177.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-916.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-275.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-433.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-781.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-177.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-177.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-177.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-200.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-108.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-200.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-200.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-200.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-490.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-800.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-840.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-840.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-840.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-840.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-795.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-156.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-498.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-798.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-795.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-795.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-795.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-892.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-8.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-892.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-892.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-892.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-972.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-233.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-972.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-972.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-972.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-65.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-50.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-641.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-641.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-641.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-641.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-18.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-123.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-326.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-166.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-18.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-18.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-18.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-393.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-423.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-103.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-796.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-445.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-38.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-796.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-796.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-796.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-491.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-463.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-491.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-491.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-491.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-7.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-361.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-676.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-201.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-28.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-676.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-676.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-676.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-84.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-404.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-498.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-864.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-274.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits2/N-77.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-129.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-34.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-331.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits2/N-973.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits2/N-919.html\n\n')
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
