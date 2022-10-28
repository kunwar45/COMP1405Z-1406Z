
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html')


output = open('fruits4-all-outgoing-failed.txt', 'w')
success_output = open('fruits4-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-959.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-162.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-959.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-959.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-959.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-141.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-639.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-131.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-532.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-629.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-281.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-203.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-653.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-714.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-841.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-850.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-990.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-322.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-235.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-260.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-167.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-706.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-543.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-343.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-250.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-504.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-402.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-640.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-743.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-639.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-639.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-639.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-639.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-644.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-350.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-59.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-350.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-350.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-350.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-898.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-906.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-997.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-23.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-368.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-248.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-368.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-368.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-368.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-405.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-476.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-174.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-352.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-64.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-454.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-630.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-793.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-894.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-429.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-894.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-894.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-894.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-71.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-71.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-71.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-71.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-693.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-315.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-387.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-174.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-387.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-387.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-387.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-581.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-754.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-581.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-581.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-581.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-93.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-110.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-250.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-254.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-189.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-292.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-357.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-964.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-376.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-858.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-635.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-94.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-482.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-94.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-94.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-94.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-59.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-170.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-160.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-604.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-971.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-526.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-601.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-170.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-170.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-170.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-422.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-825.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-151.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-436.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-767.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-996.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-684.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-294.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-803.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-126.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-161.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-664.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-932.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-482.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-621.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-35.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-84.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-133.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-264.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-365.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-368.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-859.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-445.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-569.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-763.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-374.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-77.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-374.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-374.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-374.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-75.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-120.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-405.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-408.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-131.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-95.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-243.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-440.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-188.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-771.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-139.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-408.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-449.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-669.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-17.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-193.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-962.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-137.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-962.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-962.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-962.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-917.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-353.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-917.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-917.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-917.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-852.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-159.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-852.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-852.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-852.html\n\n')
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









output = open('fruits4-all-incoming-failed.txt', 'w')
success_output = open('fruits4-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-96.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-170.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-459.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-396.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-980.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-376.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-196.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-518.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-794.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-835.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-780.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-780.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-780.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-780.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-18.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-869.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-236.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-182.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-236.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-236.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-236.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-30.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-597.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-31.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-601.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-948.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-31.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-31.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-31.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-271.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-178.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-271.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-271.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-271.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-54.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-226.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-201.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-59.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-201.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-201.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-201.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-558.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-508.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-491.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-599.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-541.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-256.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-112.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-104.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-861.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-861.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-861.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-861.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-761.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-761.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-761.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-761.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-820.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-643.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-986.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-691.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-102.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-876.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-691.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-691.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-691.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-810.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-407.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-810.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-810.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-810.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-836.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-836.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-836.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-836.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-271.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-272.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-56.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-272.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-272.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-272.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-618.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-395.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-671.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-98.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-132.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-306.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-98.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-98.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-98.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-146.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-87.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-187.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-146.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-146.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-146.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-131.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-863.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-700.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-511.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-700.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-700.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-700.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-515.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-738.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-515.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-515.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-515.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-342.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-542.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-265.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-823.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-765.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-853.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-422.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-389.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-853.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-853.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-853.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-205.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-561.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-857.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-316.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-857.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-857.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-857.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-468.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-468.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-468.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-468.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-185.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-185.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-185.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-185.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-14.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-699.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-641.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-216.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-401.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-213.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-401.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-401.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-401.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-81.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-60.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-682.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-487.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-712.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-487.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-487.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-487.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-640.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-668.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits4/N-70.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-907.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-49.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html\n\n')
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









output = open('fruits4-all-pagerank-failed.txt', 'w')
success_output = open('fruits4-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html
expected = 0.0030651662579671514
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-73.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html
expected = 0.002537455147776608
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html
expected = 0.0006829270773183403
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-723.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-633.html
expected = 0.00035377166889291053
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-633.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-633.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-633.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-28.html
expected = 0.0023371261465085936
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-28.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-28.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-28.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html
expected = 0.0009516879353851571
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-506.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html
expected = 0.0006666142577418365
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-872.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html
expected = 0.00035898075656200283
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html
expected = 0.0006274222305976262
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-854.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html
expected = 0.000615017264689792
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-954.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html
expected = 0.0031643109195962273
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html
expected = 0.000646630316083717
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-147.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html
expected = 0.0011017713984853921
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-910.html
expected = 0.0003542254174817144
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-910.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-910.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-910.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-642.html
expected = 0.0003701127819782397
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-642.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-642.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-642.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html
expected = 0.008749954127657852
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html
expected = 0.0003556433712095456
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-27.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html
expected = 0.0006295152080735538
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html
expected = 0.0006321640644354999
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-813.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-334.html
expected = 0.0006278625537578458
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-334.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-334.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-334.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html
expected = 0.001176375611364304
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-847.html
expected = 0.00039994037961784
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-847.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-847.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-847.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-599.html
expected = 0.00036398997219045493
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-599.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-599.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-599.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-297.html
expected = 0.0007810987822541561
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-297.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-297.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-297.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html
expected = 0.0015898532243535295
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-424.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html
expected = 0.0003821066814644754
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-913.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-434.html
expected = 0.00036310387844817323
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-434.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-434.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-434.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html
expected = 0.00035377166889291053
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html
expected = 0.0007220196820028966
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html
expected = 0.0006198909099215758
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-983.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html
expected = 0.0003690675699315359
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-719.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html
expected = 0.0006704199753876384
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html
expected = 0.0003607659482262596
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-956.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-976.html
expected = 0.0006664452478245812
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-976.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-976.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-976.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html
expected = 0.0018429528954152189
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-758.html
expected = 0.00038437102671007257
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-758.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-758.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-758.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-277.html
expected = 0.0008755331809870123
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-277.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-277.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-277.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html
expected = 0.0009192142181493798
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-331.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html
expected = 0.0004021482167713442
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-549.html
expected = 0.0004515875011094794
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-549.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-549.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-549.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-760.html
expected = 0.00037073874617614676
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-760.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-760.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-760.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html
expected = 0.0006409621280638856
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html
expected = 0.000395899345614179
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-598.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-828.html
expected = 0.0008744433590516055
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-828.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-828.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-828.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-694.html
expected = 0.0006402769636831306
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-694.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-694.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-694.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html
expected = 0.0009352557567870621
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-447.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html
expected = 0.00036492920035369967
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-321.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html
expected = 0.001689264018461736
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-268.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html
expected = 0.0008959032073345508
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html
expected = 0.00038106868937091265
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html\n\n')
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









output = open('fruits4-all-idf-failed.txt', 'w')
success_output = open('fruits4-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word kiwi
expected = 0.1729939903610231
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #154 checking IDF for word apricot
expected = 0.14560532224689926
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #154 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #154 checking IDF for word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #155 checking IDF for word apple
expected = 0.18114943910456646
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word blueberry
expected = 0.17136841831198113
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word papaya
expected = 0.16974467583231712
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word cherry
expected = 0.18114943910456646
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word orange
expected = 0.17136841831198113
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word fig
expected = 0.17462139610706884
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word peach
expected = 0.1795146570136211
result = searchdata.get_idf('peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word lime
expected = 0.18278607574167338
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word banana
expected = 0.16650266314016507
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word pear
expected = 0.17462139610706884
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word coconut
expected = 0.18114943910456646
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word coconut\n\n')
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









output = open('fruits4-all-tf-failed.txt', 'w')
success_output = open('fruits4-all-tf-passed.txt', 'w')

#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word pear
expected = 0.0963855421686747
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word orange
expected = 0.0963855421686747
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word papaya
expected = 0.04819277108433735
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word peach
expected = 0.13253012048192772
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word apple
expected = 0.12048192771084337
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word blueberry
expected = 0.024096385542168676
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word lime
expected = 0.10843373493975904
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word fig
expected = 0.07228915662650602
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word apricot
expected = 0.012048192771084338
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word cherry
expected = 0.03614457831325301
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-981.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word pear
expected = 0.07042253521126761
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word orange
expected = 0.028169014084507043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word papaya
expected = 0.07042253521126761
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word peach
expected = 0.08450704225352113
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word apple
expected = 0.09859154929577464
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word blueberry
expected = 0.1267605633802817
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word lime
expected = 0.056338028169014086
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word fig
expected = 0.014084507042253521
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word apricot
expected = 0.07042253521126761
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word cherry
expected = 0.09859154929577464
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word pear
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word orange
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word papaya
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word peach
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word apple
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word blueberry
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word lime
expected = 0.09722222222222222
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word fig
expected = 0.06944444444444445
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word apricot
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word cherry
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word pear
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word orange
expected = 0.16
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word papaya
expected = 0.16
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word apple
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word blueberry
expected = 0.24
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word lime
expected = 0.08
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word fig
expected = 0.04
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-284.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word pear
expected = 0.07246376811594203
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word orange
expected = 0.15942028985507245
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word papaya
expected = 0.057971014492753624
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word peach
expected = 0.07246376811594203
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word apple
expected = 0.028985507246376812
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word blueberry
expected = 0.08695652173913043
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word lime
expected = 0.11594202898550725
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word fig
expected = 0.043478260869565216
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word apricot
expected = 0.10144927536231885
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word cherry
expected = 0.057971014492753624
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-745.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word pear
expected = 0.3333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word papaya
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word blueberry
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word apricot
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-210.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word pear
expected = 0.05063291139240506
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word orange
expected = 0.06329113924050633
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word papaya
expected = 0.06329113924050633
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word peach
expected = 0.06329113924050633
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word apple
expected = 0.1518987341772152
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word blueberry
expected = 0.0759493670886076
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word lime
expected = 0.10126582278481013
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word fig
expected = 0.10126582278481013
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word apricot
expected = 0.05063291139240506
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word cherry
expected = 0.05063291139240506
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word pear
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word orange
expected = 0.13725490196078433
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word papaya
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word peach
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word apple
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word blueberry
expected = 0.09803921568627451
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word lime
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word fig
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word apricot
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word cherry
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word pear
expected = 0.06153846153846154
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word orange
expected = 0.12307692307692308
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word papaya
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word peach
expected = 0.1076923076923077
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word apple
expected = 0.13846153846153847
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word blueberry
expected = 0.07692307692307693
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word lime
expected = 0.06153846153846154
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word fig
expected = 0.015384615384615385
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word apricot
expected = 0.03076923076923077
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word cherry
expected = 0.09230769230769231
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-377.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word pear
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word orange
expected = 0.10416666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word papaya
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word peach
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word apple
expected = 0.041666666666666664
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word blueberry
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word lime
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word fig
expected = 0.125
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word apricot
expected = 0.14583333333333334
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word cherry
expected = 0.0625
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-464.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
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


#Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
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









output = open('fruits4-all-tfidf-failed.txt', 'w')
success_output = open('fruits4-all-tfidf-passed.txt', 'w')

#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word peach
expected = 0.011261987603779978
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word apricot
expected = 0.022132459403592056
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word banana
expected = 0.015502963794576245
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word pear
expected = 0.01625889418553814
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word kiwi
expected = 0.01085290865595697
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word coconut
expected = 0.016866716380877125
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word lime
expected = 0.017019102643363426
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word orange
expected = 0.021053766546960846
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word apple
expected = 0.011364546893084757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word papaya
expected = 0.030651177300784416
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word peach
expected = 0.02253463324190123
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word apricot
expected = 0.018277964537757777
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word banana
expected = 0.02090122617329653
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word pear
expected = 0.021920377884035263
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word kiwi
expected = 0.0217160882052258
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word lime
expected = 0.022945297320499287
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word apple
expected = 0.043658482044770006
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word papaya
expected = 0.02130819888626944
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word peach
expected = 0.027286783184797558
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word apricot
expected = 0.00913465987384275
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word banana
expected = 0.015502963794576245
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word pear
expected = 0.026542992389967886
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word kiwi
expected = 0.03608423204308269
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word coconut
expected = 0.011364546893084757
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word lime
expected = 0.01146722252874381
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word orange
expected = 0.021053766546960846
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word apple
expected = 0.02753527511972982
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word papaya
expected = 0.015804825665372144
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-624.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word peach
expected = 0.02442504240488257
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word apricot
expected = 0.017700071253531457
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word banana
expected = 0.027411450279805384
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word pear
expected = 0.026265999044639228
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word kiwi
expected = 0.02353783039586135
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word coconut
expected = 0.011242309567443763
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word lime
expected = 0.014105210398281253
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word orange
expected = 0.013224134202253532
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word apple
expected = 0.016687160621525504
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word papaya
expected = 0.015636574334782195
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word peach
expected = 0.029725125793597224
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word apricot
expected = 0.018986444387524566
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word banana
expected = 0.009546126334762253
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word pear
expected = 0.010011599073267461
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word kiwi
expected = 0.016318070307315736
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word coconut
expected = 0.017087352440799806
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word lime
expected = 0.023834689613875294
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word orange
expected = 0.01616473435078617
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word apple
expected = 0.013758092163847048
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word papaya
expected = 0.02213413492058877
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word peach
expected = 0.0375999490912295
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word apricot
expected = 0.01882429534332318
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word banana
expected = 0.007391739100944854
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word pear
expected = 0.036575039125451556
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word kiwi
expected = 0.022365184987221513
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word coconut
expected = 0.008041969821325016
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word lime
expected = 0.008114626863539158
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word orange
expected = 0.007607750016811468
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word papaya
expected = 0.014846351635412276
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-605.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word peach
expected = 0.04326448631992842
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word apricot
expected = 0.03509206199236283
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word pear
expected = 0.021920377884035263
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word coconut
expected = 0.022739848879792496
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word lime
expected = 0.022945297320499287
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word orange
expected = 0.021512028712018696
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word apple
expected = 0.022739848879792496
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-249.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word peach
expected = 0.01671450279407934
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word apricot
expected = 0.00688796384442255
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word banana
expected = 0.015502963794576245
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word pear
expected = 0.012291482707434161
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word kiwi
expected = 0.016107367405820545
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word coconut
expected = 0.028838736163177475
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word lime
expected = 0.029099286416083704
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word orange
expected = 0.023563761377350296
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word apple
expected = 0.028838736163177475
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word papaya
expected = 0.015804825665372144
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-999.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word peach
expected = 0.015389768931577518
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word apricot
expected = 0.0042438630520734155
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word banana
expected = 0.014274252335980557
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word pear
expected = 0.005089575570483979
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word kiwi
expected = 0.014830753000885507
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word coconut
expected = 0.02539310413043405
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word lime
expected = 0.010549589362627744
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word orange
expected = 0.0330132823025767
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word apple
expected = 0.010455130064307278
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word papaya
expected = 0.03270047630602344
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-299.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word peach
expected = 0.021776258159909034
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word apricot
expected = 0.01077487850757903
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word banana
expected = 0.01629183992692806
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word pear
expected = 0.017086236217123872
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word kiwi
expected = 0.02890902327881537
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word coconut
expected = 0.00901273441970437
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word lime
expected = 0.026392464904072585
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word orange
expected = 0.012681362596186968
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word apple
expected = 0.026156151088426092
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word papaya
expected = 0.0205910979286451
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits4/N-68.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #398 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
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









output = open('fruits4-all-search-failed.txt', 'w')
success_output = open('fruits4-all-search-passed.txt', 'w')

#Test #409 checking search results for 'orange papaya lime fig tomato lime kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-945.html', 'title': 'N-945', 'score': 0.9999022680041744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9983738725418976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'title': 'N-253', 'score': 0.9953586822504802}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-350.html', 'title': 'N-350', 'score': 0.9944071762587902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-812.html', 'title': 'N-812', 'score': 0.9932897013350789}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-619.html', 'title': 'N-619', 'score': 0.9930102636615867}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-750.html', 'title': 'N-750', 'score': 0.9930071084190523}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 0.992550554781977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-322.html', 'title': 'N-322', 'score': 0.9916663664254778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-341.html', 'title': 'N-341', 'score': 0.9908933229401773}]
result = search.search('orange papaya lime fig tomato lime kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'orange papaya lime fig tomato lime kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'orange papaya lime fig tomato lime kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'blueberry peach orange orange kiwi papaya blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html', 'title': 'N-517', 'score': 0.9997988675788171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-871.html', 'title': 'N-871', 'score': 0.9927533522122932}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-934.html', 'title': 'N-934', 'score': 0.990619929208487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-370.html', 'title': 'N-370', 'score': 0.9905650726428051}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-529.html', 'title': 'N-529', 'score': 0.9889158270614153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-368.html', 'title': 'N-368', 'score': 0.985150994193649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-264.html', 'title': 'N-264', 'score': 0.9844076213650154}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.9834197516117105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html', 'title': 'N-977', 'score': 0.9832847109757651}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-971.html', 'title': 'N-971', 'score': 0.9821144882814117}]
result = search.search('blueberry peach orange orange kiwi papaya blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'blueberry peach orange orange kiwi papaya blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'blueberry peach orange orange kiwi papaya blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'kiwi blueberry banana pear cherry orange tomato banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-109.html', 'title': 'N-109', 'score': 0.9968178475029604}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.9965821135494555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-729.html', 'title': 'N-729', 'score': 0.9914991161837581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-547.html', 'title': 'N-547', 'score': 0.9907107127550144}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-236.html', 'title': 'N-236', 'score': 0.9906734688557645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9885059351651858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html', 'title': 'N-52', 'score': 0.9876375361560036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-835.html', 'title': 'N-835', 'score': 0.9871148307195118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-397.html', 'title': 'N-397', 'score': 0.9858636207070192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.9854827275532502}]
result = search.search('kiwi blueberry banana pear cherry orange tomato banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'kiwi blueberry banana pear cherry orange tomato banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'kiwi blueberry banana pear cherry orange tomato banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'pear banana peach tomato orange apple banana fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9956554088730204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9924542563780289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'title': 'N-382', 'score': 0.9897040052857536}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-860.html', 'title': 'N-860', 'score': 0.9884619818490334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-750.html', 'title': 'N-750', 'score': 0.9876868350022292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-776.html', 'title': 'N-776', 'score': 0.9876840296855897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-264.html', 'title': 'N-264', 'score': 0.9865589959045158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-703.html', 'title': 'N-703', 'score': 0.983377683736213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-262.html', 'title': 'N-262', 'score': 0.9820626708573714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.9808251678859589}]
result = search.search('pear banana peach tomato orange apple banana fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'pear banana peach tomato orange apple banana fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'pear banana peach tomato orange apple banana fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'fig cherry apple tomato coconut coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'title': 'N-567', 'score': 0.9999023753237996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-686.html', 'title': 'N-686', 'score': 0.9968302102162196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-859.html', 'title': 'N-859', 'score': 0.9960935211647088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-446.html', 'title': 'N-446', 'score': 0.9938168212802926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-886.html', 'title': 'N-886', 'score': 0.9935820403935813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 0.993372108909333}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html', 'title': 'N-119', 'score': 0.9931960951771018}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-552.html', 'title': 'N-552', 'score': 0.992857800691191}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9923715798648373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-818.html', 'title': 'N-818', 'score': 0.9921043337773647}]
result = search.search('fig cherry apple tomato coconut coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'fig cherry apple tomato coconut coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'fig cherry apple tomato coconut coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'papaya papaya apricot kiwi cherry coconut apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html', 'title': 'N-660', 'score': 0.9979112658188425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html', 'title': 'N-593', 'score': 0.997296003240465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html', 'title': 'N-58', 'score': 0.9971651601963976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-612.html', 'title': 'N-612', 'score': 0.9958391798996327}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-791.html', 'title': 'N-791', 'score': 0.9918384935545284}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-95.html', 'title': 'N-95', 'score': 0.9913977031831037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-129.html', 'title': 'N-129', 'score': 0.9911661435480189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html', 'title': 'N-814', 'score': 0.9909994385373001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html', 'title': 'N-877', 'score': 0.9893519822375185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9893307603475656}]
result = search.search('papaya papaya apricot kiwi cherry coconut apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'papaya papaya apricot kiwi cherry coconut apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'papaya papaya apricot kiwi cherry coconut apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'peach pear coconut tomato papaya peach fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-636.html', 'title': 'N-636', 'score': 0.998250417797714}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-930.html', 'title': 'N-930', 'score': 0.9981350776458688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-601.html', 'title': 'N-601', 'score': 0.9974164102678688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'title': 'N-253', 'score': 0.9967419621378208}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.9950096044432715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-823.html', 'title': 'N-823', 'score': 0.9949215986199816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html', 'title': 'N-483', 'score': 0.9947532351995332}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-160.html', 'title': 'N-160', 'score': 0.9944842353107974}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-127.html', 'title': 'N-127', 'score': 0.9936195981719005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-919.html', 'title': 'N-919', 'score': 0.9935547196604386}]
result = search.search('peach pear coconut tomato papaya peach fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'peach pear coconut tomato papaya peach fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'peach pear coconut tomato papaya peach fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'cherry kiwi lime fig banana lime apricot lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html', 'title': 'N-190', 'score': 0.9976281782469267}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 0.9902168953430668}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-613.html', 'title': 'N-613', 'score': 0.9867648756725804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9852926448555197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'title': 'N-86', 'score': 0.9815537584254856}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-354.html', 'title': 'N-354', 'score': 0.9807587070105053}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-812.html', 'title': 'N-812', 'score': 0.9790266776239608}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-975.html', 'title': 'N-975', 'score': 0.9771914237945839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html', 'title': 'N-448', 'score': 0.9769464924590219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-65.html', 'title': 'N-65', 'score': 0.9767525826429972}]
result = search.search('cherry kiwi lime fig banana lime apricot lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'cherry kiwi lime fig banana lime apricot lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'cherry kiwi lime fig banana lime apricot lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'fig pear coconut pear pear coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01684371651258179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.015935878457349173}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013466112035500952}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.010803279989646771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.008780711566928496}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.008020514805507676}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.0072530953062633465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006233025776724009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.00619027609961917}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006071185321786053}]
result = search.search('fig pear coconut pear pear coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'fig pear coconut pear pear coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'fig pear coconut pear pear coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'coconut apple kiwi apple kiwi kiwi banana apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-708.html', 'title': 'N-708', 'score': 0.9993644122703422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-106.html', 'title': 'N-106', 'score': 0.9979944767042455}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-944.html', 'title': 'N-944', 'score': 0.9960914699880317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html', 'title': 'N-849', 'score': 0.9939657941248626}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-388.html', 'title': 'N-388', 'score': 0.9935606301194881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-852.html', 'title': 'N-852', 'score': 0.9932796461363518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-269.html', 'title': 'N-269', 'score': 0.9930123232544649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 0.9928218492665691}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-101.html', 'title': 'N-101', 'score': 0.992667919732754}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-406.html', 'title': 'N-406', 'score': 0.9925451572424173}]
result = search.search('coconut apple kiwi apple kiwi kiwi banana apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'coconut apple kiwi apple kiwi kiwi banana apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'coconut apple kiwi apple kiwi kiwi banana apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'pear coconut orange pear peach apricot peach blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-233.html', 'title': 'N-233', 'score': 0.9885309760651467}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-318.html', 'title': 'N-318', 'score': 0.9863197440827303}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-501.html', 'title': 'N-501', 'score': 0.9862467417944638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-417.html', 'title': 'N-417', 'score': 0.9854942007803649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-592.html', 'title': 'N-592', 'score': 0.9848020757133034}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-193.html', 'title': 'N-193', 'score': 0.9845192188431302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-507.html', 'title': 'N-507', 'score': 0.9820931333354816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-63.html', 'title': 'N-63', 'score': 0.9816008155438698}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html', 'title': 'N-16', 'score': 0.9812022309358922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html', 'title': 'N-748', 'score': 0.9809226132582213}]
result = search.search('pear coconut orange pear peach apricot peach blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'pear coconut orange pear peach apricot peach blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'pear coconut orange pear peach apricot peach blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'peach papaya fig blueberry lime peach orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-676.html', 'title': 'N-676', 'score': 0.9970527489553507}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html', 'title': 'N-566', 'score': 0.9960482710460156}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-958.html', 'title': 'N-958', 'score': 0.9934436472123724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-525.html', 'title': 'N-525', 'score': 0.9933844250099181}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-847.html', 'title': 'N-847', 'score': 0.9915442290217694}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-66.html', 'title': 'N-66', 'score': 0.9900517823503625}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-711.html', 'title': 'N-711', 'score': 0.9888872948061485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-901.html', 'title': 'N-901', 'score': 0.9874414682686579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-346.html', 'title': 'N-346', 'score': 0.987001999127055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-544.html', 'title': 'N-544', 'score': 0.986546059615691}]
result = search.search('peach papaya fig blueberry lime peach orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'peach papaya fig blueberry lime peach orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'peach papaya fig blueberry lime peach orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'blueberry kiwi lime peach lime coconut peach lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-58.html', 'title': 'N-58', 'score': 0.9940574336057845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-128.html', 'title': 'N-128', 'score': 0.9912221947075779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-65.html', 'title': 'N-65', 'score': 0.990892763596852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-417.html', 'title': 'N-417', 'score': 0.9896163642857274}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-223.html', 'title': 'N-223', 'score': 0.9890484072135359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-758.html', 'title': 'N-758', 'score': 0.9883899193315503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html', 'title': 'N-485', 'score': 0.98688845242701}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-777.html', 'title': 'N-777', 'score': 0.9864211055687878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-140.html', 'title': 'N-140', 'score': 0.9862396143260079}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-660.html', 'title': 'N-660', 'score': 0.9851095989698534}]
result = search.search('blueberry kiwi lime peach lime coconut peach lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'blueberry kiwi lime peach lime coconut peach lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'blueberry kiwi lime peach lime coconut peach lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'kiwi banana blueberry pear lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-278.html', 'title': 'N-278', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-947.html', 'title': 'N-947', 'score': 0.9980953433716999}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-165.html', 'title': 'N-165', 'score': 0.9980781949178014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-727.html', 'title': 'N-727', 'score': 0.9979784577987696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-186.html', 'title': 'N-186', 'score': 0.9973223649644237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-554.html', 'title': 'N-554', 'score': 0.997302912642192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-2.html', 'title': 'N-2', 'score': 0.9972758546529769}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'title': 'N-614', 'score': 0.9964859473576971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-951.html', 'title': 'N-951', 'score': 0.9964650267636332}]
result = search.search('kiwi banana blueberry pear lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'kiwi banana blueberry pear lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'kiwi banana blueberry pear lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'blueberry fig fig kiwi lime coconut blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 0.9998161374410445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-82.html', 'title': 'N-82', 'score': 0.9956858988571003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-609.html', 'title': 'N-609', 'score': 0.9944992570714688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-224.html', 'title': 'N-224', 'score': 0.9942179815665447}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html', 'title': 'N-124', 'score': 0.9930833384444422}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-585.html', 'title': 'N-585', 'score': 0.9926858899573112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 0.9924189771725445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html', 'title': 'N-846', 'score': 0.9910578898729905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-805.html', 'title': 'N-805', 'score': 0.9906220299782076}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-557.html', 'title': 'N-557', 'score': 0.990357926424378}]
result = search.search('blueberry fig fig kiwi lime coconut blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'blueberry fig fig kiwi lime coconut blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'blueberry fig fig kiwi lime coconut blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'tomato apricot fig apple banana pear papaya apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 0.9999779881552405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9999461219929063}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.9939084440515649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html', 'title': 'N-488', 'score': 0.9914870204262246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-783.html', 'title': 'N-783', 'score': 0.9912971771456882}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-836.html', 'title': 'N-836', 'score': 0.9908737792131836}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-635.html', 'title': 'N-635', 'score': 0.9899645170324395}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-977.html', 'title': 'N-977', 'score': 0.9883490901442228}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-926.html', 'title': 'N-926', 'score': 0.9871933353462109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-614.html', 'title': 'N-614', 'score': 0.9846345847306008}]
result = search.search('tomato apricot fig apple banana pear papaya apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'tomato apricot fig apple banana pear papaya apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'tomato apricot fig apple banana pear papaya apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'cherry pear kiwi kiwi apple blueberry banana peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-83.html', 'title': 'N-83', 'score': 0.9934270953105659}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-567.html', 'title': 'N-567', 'score': 0.9921167590435768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-162.html', 'title': 'N-162', 'score': 0.9903666699135926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-45.html', 'title': 'N-45', 'score': 0.9884897170097985}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.9870326599651027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-962.html', 'title': 'N-962', 'score': 0.9865768331067278}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9862342350669423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-188.html', 'title': 'N-188', 'score': 0.9856076937885986}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-629.html', 'title': 'N-629', 'score': 0.9852435984524359}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-818.html', 'title': 'N-818', 'score': 0.9842937156850564}]
result = search.search('cherry pear kiwi kiwi apple blueberry banana peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'cherry pear kiwi kiwi apple blueberry banana peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'cherry pear kiwi kiwi apple blueberry banana peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'lime lime fig orange peach apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9976102169219171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-416.html', 'title': 'N-416', 'score': 0.9973126158093414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-442.html', 'title': 'N-442', 'score': 0.9972851656843237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html', 'title': 'N-113', 'score': 0.9966748902220013}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-119.html', 'title': 'N-119', 'score': 0.9960557631775483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-812.html', 'title': 'N-812', 'score': 0.9935957498685224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-350.html', 'title': 'N-350', 'score': 0.9921136504993172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-766.html', 'title': 'N-766', 'score': 0.9915455874970279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9908147331704068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-989.html', 'title': 'N-989', 'score': 0.9902199683222049}]
result = search.search('lime lime fig orange peach apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'lime lime fig orange peach apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'lime lime fig orange peach apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'banana cherry pear coconut blueberry peach cherry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-695.html', 'title': 'N-695', 'score': 0.9999243310835896}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-902.html', 'title': 'N-902', 'score': 0.9881041310199561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-957.html', 'title': 'N-957', 'score': 0.9868483807210071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-974.html', 'title': 'N-974', 'score': 0.986562736124426}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9858891546437093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html', 'title': 'N-369', 'score': 0.9853297614910853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-237.html', 'title': 'N-237', 'score': 0.983334643528041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-123.html', 'title': 'N-123', 'score': 0.9832624794008906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html', 'title': 'N-849', 'score': 0.9821161279325101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-461.html', 'title': 'N-461', 'score': 0.9810888794063515}]
result = search.search('banana cherry pear coconut blueberry peach cherry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'banana cherry pear coconut blueberry peach cherry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'banana cherry pear coconut blueberry peach cherry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'orange papaya cherry papaya kiwi apricot peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-410.html', 'title': 'N-410', 'score': 0.9942859623738115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-586.html', 'title': 'N-586', 'score': 0.9916599698594686}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-100.html', 'title': 'N-100', 'score': 0.9907478504924017}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 0.9880364619820579}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html', 'title': 'N-175', 'score': 0.9859430425688072}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-785.html', 'title': 'N-785', 'score': 0.9835036245665928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html', 'title': 'N-877', 'score': 0.9833711209636563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-589.html', 'title': 'N-589', 'score': 0.9831705660564766}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-929.html', 'title': 'N-929', 'score': 0.9829810257015376}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html', 'title': 'N-244', 'score': 0.9829092340357178}]
result = search.search('orange papaya cherry papaya kiwi apricot peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'orange papaya cherry papaya kiwi apricot peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'orange papaya cherry papaya kiwi apricot peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'peach apple tomato orange cherry pear cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html', 'title': 'N-849', 'score': 0.9945027428554956}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-157.html', 'title': 'N-157', 'score': 0.993948582087613}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.9932799269464465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-298.html', 'title': 'N-298', 'score': 0.9930209943487546}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-262.html', 'title': 'N-262', 'score': 0.9927774179842364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-697.html', 'title': 'N-697', 'score': 0.992327321174379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9921609050077389}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-993.html', 'title': 'N-993', 'score': 0.9911831218856684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'title': 'N-382', 'score': 0.9895998419315334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-252.html', 'title': 'N-252', 'score': 0.9893616507973305}]
result = search.search('peach apple tomato orange cherry pear cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'peach apple tomato orange cherry pear cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'peach apple tomato orange cherry pear cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'orange cherry cherry apple papaya papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-214.html', 'title': 'N-214', 'score': 0.9998107762655449}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-352.html', 'title': 'N-352', 'score': 0.99971481543437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9978553986957528}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html', 'title': 'N-722', 'score': 0.9974551900265493}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html', 'title': 'N-313', 'score': 0.9966602371135548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html', 'title': 'N-492', 'score': 0.99630155424978}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-399.html', 'title': 'N-399', 'score': 0.9957358020054778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-467.html', 'title': 'N-467', 'score': 0.9956102507196081}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-246.html', 'title': 'N-246', 'score': 0.9955978966753984}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-642.html', 'title': 'N-642', 'score': 0.9954033898282446}]
result = search.search('orange cherry cherry apple papaya papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'orange cherry cherry apple papaya papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'orange cherry cherry apple papaya papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'cherry apple fig lime cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-285.html', 'title': 'N-285', 'score': 0.999828031545813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9965447823574178}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.9930544062990854}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-286.html', 'title': 'N-286', 'score': 0.9907624772456537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-466.html', 'title': 'N-466', 'score': 0.9907609699083852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-24.html', 'title': 'N-24', 'score': 0.9900817551016264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-214.html', 'title': 'N-214', 'score': 0.989456743009767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-117.html', 'title': 'N-117', 'score': 0.9892881326545098}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-849.html', 'title': 'N-849', 'score': 0.9889133339452086}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html', 'title': 'N-313', 'score': 0.988165234492996}]
result = search.search('cherry apple fig lime cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'cherry apple fig lime cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'cherry apple fig lime cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'coconut orange blueberry banana peach blueberry blueberry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.9907046638504358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-200.html', 'title': 'N-200', 'score': 0.9885162588303407}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-480.html', 'title': 'N-480', 'score': 0.9872930038676828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9865859549268061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-791.html', 'title': 'N-791', 'score': 0.9822956598541612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-343.html', 'title': 'N-343', 'score': 0.9808541050177924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-288.html', 'title': 'N-288', 'score': 0.9796170587449898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-57.html', 'title': 'N-57', 'score': 0.9787186441525924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-877.html', 'title': 'N-877', 'score': 0.9782943881021358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-164.html', 'title': 'N-164', 'score': 0.9770481642559766}]
result = search.search('coconut orange blueberry banana peach blueberry blueberry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'coconut orange blueberry banana peach blueberry blueberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'coconut orange blueberry banana peach blueberry blueberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'coconut orange banana banana kiwi blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-842.html', 'title': 'N-842', 'score': 0.9998776205666543}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-398.html', 'title': 'N-398', 'score': 0.9945525232347119}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-109.html', 'title': 'N-109', 'score': 0.9938595955182151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-356.html', 'title': 'N-356', 'score': 0.9928537048305495}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-403.html', 'title': 'N-403', 'score': 0.9921202311662116}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-705.html', 'title': 'N-705', 'score': 0.9913822945076876}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-616.html', 'title': 'N-616', 'score': 0.9903765729384839}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-195.html', 'title': 'N-195', 'score': 0.9898790842334592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-236.html', 'title': 'N-236', 'score': 0.9898640434383171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.9896434726159075}]
result = search.search('coconut orange banana banana kiwi blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'coconut orange banana banana kiwi blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'coconut orange banana banana kiwi blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'orange orange tomato lime peach tomato coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-422.html', 'title': 'N-422', 'score': 0.9999822920067688}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html', 'title': 'N-124', 'score': 0.9999178464980537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-474.html', 'title': 'N-474', 'score': 0.9999178464980537}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-935.html', 'title': 'N-935', 'score': 0.9999024199026916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-517.html', 'title': 'N-517', 'score': 0.9998611261931538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-702.html', 'title': 'N-702', 'score': 0.9998077312847182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-261.html', 'title': 'N-261', 'score': 0.9988737529818863}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-596.html', 'title': 'N-596', 'score': 0.9988679101194187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-450.html', 'title': 'N-450', 'score': 0.9974655249384485}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9974146672885513}]
result = search.search('orange orange tomato lime peach tomato coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'orange orange tomato lime peach tomato coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'orange orange tomato lime peach tomato coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'coconut apple blueberry fig tomato apple papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 0.9973127657543654}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.9972436920872817}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-763.html', 'title': 'N-763', 'score': 0.9958432917985263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9957778120860703}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-179.html', 'title': 'N-179', 'score': 0.9950052841178381}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-336.html', 'title': 'N-336', 'score': 0.9949440631762497}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9944826948935296}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-559.html', 'title': 'N-559', 'score': 0.9929240248870143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html', 'title': 'N-295', 'score': 0.9925587216947792}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-287.html', 'title': 'N-287', 'score': 0.9913923760786824}]
result = search.search('coconut apple blueberry fig tomato apple papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'coconut apple blueberry fig tomato apple papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'coconut apple blueberry fig tomato apple papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'peach peach papaya orange lime cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-414.html', 'title': 'N-414', 'score': 0.9977976034995857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-415.html', 'title': 'N-415', 'score': 0.9969931895176641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-676.html', 'title': 'N-676', 'score': 0.9966531008874335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-525.html', 'title': 'N-525', 'score': 0.9961010328577707}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-579.html', 'title': 'N-579', 'score': 0.9958257658246508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-769.html', 'title': 'N-769', 'score': 0.995617804680118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html', 'title': 'N-566', 'score': 0.9947328130552922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-472.html', 'title': 'N-472', 'score': 0.9946585830376663}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-930.html', 'title': 'N-930', 'score': 0.9945478565978568}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-397.html', 'title': 'N-397', 'score': 0.9919678388056521}]
result = search.search('peach peach papaya orange lime cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'peach peach papaya orange lime cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'peach peach papaya orange lime cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'coconut tomato apricot pear pear peach lime apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-300.html', 'title': 'N-300', 'score': 0.9999025380740204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-768.html', 'title': 'N-768', 'score': 0.9949140477073888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html', 'title': 'N-295', 'score': 0.9945816590898438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-562.html', 'title': 'N-562', 'score': 0.9945650450081109}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-742.html', 'title': 'N-742', 'score': 0.9939155568945518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-754.html', 'title': 'N-754', 'score': 0.9938035831695902}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html', 'title': 'N-814', 'score': 0.9926927636511008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-497.html', 'title': 'N-497', 'score': 0.9921297762066489}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-449.html', 'title': 'N-449', 'score': 0.991349652044847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 0.9902962676653043}]
result = search.search('coconut tomato apricot pear pear peach lime apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'coconut tomato apricot pear pear peach lime apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'coconut tomato apricot pear pear peach lime apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'papaya papaya coconut fig apricot coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-121.html', 'title': 'N-121', 'score': 0.9999474866071727}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-155.html', 'title': 'N-155', 'score': 0.9971880517271947}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-620.html', 'title': 'N-620', 'score': 0.9946310664059946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-427.html', 'title': 'N-427', 'score': 0.9938990238418112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-113.html', 'title': 'N-113', 'score': 0.9937286025905828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-428.html', 'title': 'N-428', 'score': 0.9931866464830953}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-855.html', 'title': 'N-855', 'score': 0.992742720727805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-244.html', 'title': 'N-244', 'score': 0.99262453950599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-26.html', 'title': 'N-26', 'score': 0.9922098586002724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-952.html', 'title': 'N-952', 'score': 0.9921231734323677}]
result = search.search('papaya papaya coconut fig apricot coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'papaya papaya coconut fig apricot coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'papaya papaya coconut fig apricot coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'peach peach cherry coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-5.html', 'title': 'N-5', 'score': 0.9998405592456103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-272.html', 'title': 'N-272', 'score': 0.9998066213320816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-16.html', 'title': 'N-16', 'score': 0.9997374051863475}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-37.html', 'title': 'N-37', 'score': 0.9997036667747623}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-899.html', 'title': 'N-899', 'score': 0.999646664557048}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-302.html', 'title': 'N-302', 'score': 0.9996253890370522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-472.html', 'title': 'N-472', 'score': 0.9992087152426715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-127.html', 'title': 'N-127', 'score': 0.9982421703834778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-354.html', 'title': 'N-354', 'score': 0.9966495704809107}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-878.html', 'title': 'N-878', 'score': 0.9955444415660286}]
result = search.search('peach peach cherry coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'peach peach cherry coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'peach peach cherry coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'papaya blueberry peach coconut apple pear blueberry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.9935733783725765}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9895246292200068}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-222.html', 'title': 'N-222', 'score': 0.9868993816760689}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'title': 'N-382', 'score': 0.9868575968438232}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-124.html', 'title': 'N-124', 'score': 0.9834610274632106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-949.html', 'title': 'N-949', 'score': 0.9820360351135372}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9820170672753283}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-183.html', 'title': 'N-183', 'score': 0.9815064440040264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-164.html', 'title': 'N-164', 'score': 0.9812327561024826}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-483.html', 'title': 'N-483', 'score': 0.981185073359009}]
result = search.search('papaya blueberry peach coconut apple pear blueberry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'papaya blueberry peach coconut apple pear blueberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'papaya blueberry peach coconut apple pear blueberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'papaya fig fig blueberry coconut apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.9933129104886285}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-748.html', 'title': 'N-748', 'score': 0.989878227976592}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.9868599574225561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-193.html', 'title': 'N-193', 'score': 0.9860958986852606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 0.9844851066490242}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-141.html', 'title': 'N-141', 'score': 0.983287059075816}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-525.html', 'title': 'N-525', 'score': 0.982843938631466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-156.html', 'title': 'N-156', 'score': 0.9815807846937971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-566.html', 'title': 'N-566', 'score': 0.9803529020745402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-219.html', 'title': 'N-219', 'score': 0.979667402001351}]
result = search.search('papaya fig fig blueberry coconut apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'papaya fig fig blueberry coconut apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'papaya fig fig blueberry coconut apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'lime fig pear lime apple coconut blueberry banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-608.html', 'title': 'N-608', 'score': 0.9931002389849074}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-417.html', 'title': 'N-417', 'score': 0.991899519462022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-844.html', 'title': 'N-844', 'score': 0.991554089182292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-239.html', 'title': 'N-239', 'score': 0.991316362347809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-171.html', 'title': 'N-171', 'score': 0.9900057963949925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-952.html', 'title': 'N-952', 'score': 0.989720337610898}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-642.html', 'title': 'N-642', 'score': 0.988008957039036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-878.html', 'title': 'N-878', 'score': 0.9867551435386077}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-221.html', 'title': 'N-221', 'score': 0.9854035186706201}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-125.html', 'title': 'N-125', 'score': 0.9838776199665356}]
result = search.search('lime fig pear lime apple coconut blueberry banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'lime fig pear lime apple coconut blueberry banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'lime fig pear lime apple coconut blueberry banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'banana kiwi papaya fig lime orange papaya coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-512.html', 'title': 'N-512', 'score': 0.9974823492212193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-652.html', 'title': 'N-652', 'score': 0.9889229090746292}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-791.html', 'title': 'N-791', 'score': 0.9865179262064308}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-551.html', 'title': 'N-551', 'score': 0.9864907011191147}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-175.html', 'title': 'N-175', 'score': 0.9862305098125427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-241.html', 'title': 'N-241', 'score': 0.9856900914338655}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html', 'title': 'N-313', 'score': 0.9845995928441584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.983866238595658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 0.9829177521796583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-749.html', 'title': 'N-749', 'score': 0.982749152527342}]
result = search.search('banana kiwi papaya fig lime orange papaya coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'banana kiwi papaya fig lime orange papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'banana kiwi papaya fig lime orange papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'cherry orange apple apricot tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-212.html', 'title': 'N-212', 'score': 0.9998560701569025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-734.html', 'title': 'N-734', 'score': 0.9997187055894451}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-903.html', 'title': 'N-903', 'score': 0.9996890369589793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-669.html', 'title': 'N-669', 'score': 0.9996721340411503}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-914.html', 'title': 'N-914', 'score': 0.9996571078720448}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-819.html', 'title': 'N-819', 'score': 0.9995424621872925}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9989599380048027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-625.html', 'title': 'N-625', 'score': 0.9989599380048027}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-665.html', 'title': 'N-665', 'score': 0.9969483550059879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-704.html', 'title': 'N-704', 'score': 0.9961274731423578}]
result = search.search('cherry orange apple apricot tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'cherry orange apple apricot tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'cherry orange apple apricot tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'coconut apple papaya peach banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-435.html', 'title': 'N-435', 'score': 0.9988138728289998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-115.html', 'title': 'N-115', 'score': 0.9983004792277261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.998099413319658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9978930193967398}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-239.html', 'title': 'N-239', 'score': 0.9972786799333085}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-973.html', 'title': 'N-973', 'score': 0.9962437569185855}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9948885328880008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.994549992415124}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-67.html', 'title': 'N-67', 'score': 0.9942693180950679}]
result = search.search('coconut apple papaya peach banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'coconut apple papaya peach banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'coconut apple papaya peach banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'tomato lime pear banana orange banana fig blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-52.html', 'title': 'N-52', 'score': 0.9973742433283904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-97.html', 'title': 'N-97', 'score': 0.9946342122119554}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html', 'title': 'N-295', 'score': 0.9926446456480742}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-109.html', 'title': 'N-109', 'score': 0.9925398796686253}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-349.html', 'title': 'N-349', 'score': 0.9909337076310143}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.9908153726033094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-452.html', 'title': 'N-452', 'score': 0.9907118873184719}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-421.html', 'title': 'N-421', 'score': 0.9899825257435001}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-856.html', 'title': 'N-856', 'score': 0.9897759764474413}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-259.html', 'title': 'N-259', 'score': 0.9876403296238659}]
result = search.search('tomato lime pear banana orange banana fig blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'tomato lime pear banana orange banana fig blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'tomato lime pear banana orange banana fig blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'orange blueberry papaya blueberry cherry lime papaya cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-548.html', 'title': 'N-548', 'score': 0.9999378476947469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-375.html', 'title': 'N-375', 'score': 0.9998927461904699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-105.html', 'title': 'N-105', 'score': 0.9937507162868218}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html', 'title': 'N-313', 'score': 0.9937067820635365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-741.html', 'title': 'N-741', 'score': 0.9935174928139835}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-492.html', 'title': 'N-492', 'score': 0.9933027252922114}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-214.html', 'title': 'N-214', 'score': 0.9929844419354263}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-144.html', 'title': 'N-144', 'score': 0.9925475198910996}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-201.html', 'title': 'N-201', 'score': 0.991337971970871}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-167.html', 'title': 'N-167', 'score': 0.9910455441808563}]
result = search.search('orange blueberry papaya blueberry cherry lime papaya cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'orange blueberry papaya blueberry cherry lime papaya cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'orange blueberry papaya blueberry cherry lime papaya cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'coconut apple papaya lime cherry cherry lime lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-92.html', 'title': 'N-92', 'score': 0.9963056797545561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-707.html', 'title': 'N-707', 'score': 0.9926189092027641}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-369.html', 'title': 'N-369', 'score': 0.9925940504633096}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-727.html', 'title': 'N-727', 'score': 0.9901535370245405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-417.html', 'title': 'N-417', 'score': 0.9876678114729112}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-237.html', 'title': 'N-237', 'score': 0.9868515017540186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-688.html', 'title': 'N-688', 'score': 0.9858411643946491}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-78.html', 'title': 'N-78', 'score': 0.9855975620859511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-253.html', 'title': 'N-253', 'score': 0.9850693789706456}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-86.html', 'title': 'N-86', 'score': 0.9847121234063805}]
result = search.search('coconut apple papaya lime cherry cherry lime lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'coconut apple papaya lime cherry cherry lime lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'coconut apple papaya lime cherry cherry lime lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'blueberry lime orange kiwi fig tomato lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-845.html', 'title': 'N-845', 'score': 0.9956983650931697}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9934593864653476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9926239306371704}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-724.html', 'title': 'N-724', 'score': 0.9913893554627631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-722.html', 'title': 'N-722', 'score': 0.991000269132958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-372.html', 'title': 'N-372', 'score': 0.9907983313071044}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-77.html', 'title': 'N-77', 'score': 0.990635862890219}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-190.html', 'title': 'N-190', 'score': 0.9896547420572105}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-878.html', 'title': 'N-878', 'score': 0.9893763001525762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-766.html', 'title': 'N-766', 'score': 0.989108849148589}]
result = search.search('blueberry lime orange kiwi fig tomato lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'blueberry lime orange kiwi fig tomato lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'blueberry lime orange kiwi fig tomato lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'banana apricot blueberry tomato blueberry lime pear kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-61.html', 'title': 'N-61', 'score': 0.9999329697973128}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-313.html', 'title': 'N-313', 'score': 0.9942127800214209}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-732.html', 'title': 'N-732', 'score': 0.9919629142074146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-224.html', 'title': 'N-224', 'score': 0.9917784235557878}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-756.html', 'title': 'N-756', 'score': 0.9903403168312473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-784.html', 'title': 'N-784', 'score': 0.9896936475970556}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-392.html', 'title': 'N-392', 'score': 0.9878867550209682}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-798.html', 'title': 'N-798', 'score': 0.9874497082079405}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-456.html', 'title': 'N-456', 'score': 0.985894617056341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-580.html', 'title': 'N-580', 'score': 0.9858177795652269}]
result = search.search('banana apricot blueberry tomato blueberry lime pear kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'banana apricot blueberry tomato blueberry lime pear kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'banana apricot blueberry tomato blueberry lime pear kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'orange blueberry orange orange coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.017757879230558445}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.01747926870050033}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013279743543258221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.01309744507633254}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.007118054243718983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.006942641646286649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006340013952438828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.006323227198052681}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.006310578722450991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.006146839966339949}]
result = search.search('orange blueberry orange orange coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'orange blueberry orange orange coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'orange blueberry orange orange coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'apricot apple banana fig apple papaya kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-138.html', 'title': 'N-138', 'score': 0.9999507369130585}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9999065379969252}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-22.html', 'title': 'N-22', 'score': 0.993545176014309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-72.html', 'title': 'N-72', 'score': 0.9925956699962247}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-433.html', 'title': 'N-433', 'score': 0.9918194410515612}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-379.html', 'title': 'N-379', 'score': 0.9914628214195749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-191.html', 'title': 'N-191', 'score': 0.9909810507594404}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-763.html', 'title': 'N-763', 'score': 0.9909666157331553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-635.html', 'title': 'N-635', 'score': 0.9909579637476146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-836.html', 'title': 'N-836', 'score': 0.9907475960205908}]
result = search.search('apricot apple banana fig apple papaya kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'apricot apple banana fig apple papaya kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'apricot apple banana fig apple papaya kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'orange banana fig fig fig pear papaya coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 0.9942385034771439}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-979.html', 'title': 'N-979', 'score': 0.9914261697150171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-473.html', 'title': 'N-473', 'score': 0.9871661265759477}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-500.html', 'title': 'N-500', 'score': 0.9864782810654008}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-792.html', 'title': 'N-792', 'score': 0.9799354958549942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-846.html', 'title': 'N-846', 'score': 0.9793818437462402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-485.html', 'title': 'N-485', 'score': 0.9770289542922813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-904.html', 'title': 'N-904', 'score': 0.9766324844796362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-39.html', 'title': 'N-39', 'score': 0.9761822462763399}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-645.html', 'title': 'N-645', 'score': 0.9756488048618805}]
result = search.search('orange banana fig fig fig pear papaya coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'orange banana fig fig fig pear papaya coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'orange banana fig fig fig pear papaya coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'orange peach kiwi kiwi blueberry apricot kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-298.html', 'title': 'N-298', 'score': 0.9958197274135204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-442.html', 'title': 'N-442', 'score': 0.9951343852301391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-455.html', 'title': 'N-455', 'score': 0.9940367340923182}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-858.html', 'title': 'N-858', 'score': 0.9916933552269158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-560.html', 'title': 'N-560', 'score': 0.989230600038781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.9881613764958038}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-916.html', 'title': 'N-916', 'score': 0.9864628892183778}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-242.html', 'title': 'N-242', 'score': 0.9857453748550787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-295.html', 'title': 'N-295', 'score': 0.9851104278734273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-362.html', 'title': 'N-362', 'score': 0.9836779206122794}]
result = search.search('orange peach kiwi kiwi blueberry apricot kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'orange peach kiwi kiwi blueberry apricot kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'orange peach kiwi kiwi blueberry apricot kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'papaya pear peach lime orange fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-488.html', 'title': 'N-488', 'score': 0.9968217368607125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-258.html', 'title': 'N-258', 'score': 0.996818428375004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-135.html', 'title': 'N-135', 'score': 0.995561323785928}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-662.html', 'title': 'N-662', 'score': 0.9928113101095453}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-340.html', 'title': 'N-340', 'score': 0.9921858792520593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-382.html', 'title': 'N-382', 'score': 0.9911179824017534}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-505.html', 'title': 'N-505', 'score': 0.9910246795444221}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9905670081876198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-530.html', 'title': 'N-530', 'score': 0.9901539719346588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-452.html', 'title': 'N-452', 'score': 0.9901364337408659}]
result = search.search('papaya pear peach lime orange fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'papaya pear peach lime orange fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'papaya pear peach lime orange fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'peach banana banana orange lime blueberry cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-616.html', 'title': 'N-616', 'score': 0.9952661823253012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-991.html', 'title': 'N-991', 'score': 0.993041427156419}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-835.html', 'title': 'N-835', 'score': 0.9918532994105597}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-386.html', 'title': 'N-386', 'score': 0.990411110847396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-563.html', 'title': 'N-563', 'score': 0.9901289179836638}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-109.html', 'title': 'N-109', 'score': 0.9897247248795011}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-403.html', 'title': 'N-403', 'score': 0.9892344208249205}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-43.html', 'title': 'N-43', 'score': 0.9870178397235857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-76.html', 'title': 'N-76', 'score': 0.9857621356749031}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-814.html', 'title': 'N-814', 'score': 0.985653722883359}]
result = search.search('peach banana banana orange lime blueberry cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'peach banana banana orange lime blueberry cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'peach banana banana orange lime blueberry cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'peach apple apricot cherry orange tomato orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-7.html', 'title': 'N-7', 'score': 0.9987742384869471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-701.html', 'title': 'N-701', 'score': 0.9929174390182927}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-804.html', 'title': 'N-804', 'score': 0.9927182720503245}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-471.html', 'title': 'N-471', 'score': 0.9926890691297602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-665.html', 'title': 'N-665', 'score': 0.992273451329603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-400.html', 'title': 'N-400', 'score': 0.9922221546635857}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-896.html', 'title': 'N-896', 'score': 0.9899837610734362}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-755.html', 'title': 'N-755', 'score': 0.9894433428653931}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-590.html', 'title': 'N-590', 'score': 0.9890451220175763}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-448.html', 'title': 'N-448', 'score': 0.9887919006070602}]
result = search.search('peach apple apricot cherry orange tomato orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'peach apple apricot cherry orange tomato orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'peach apple apricot cherry orange tomato orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'banana blueberry apricot orange cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-507.html', 'title': 'N-507', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-360.html', 'title': 'N-360', 'score': 0.9984616292384264}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-795.html', 'title': 'N-795', 'score': 0.9979467348551149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-867.html', 'title': 'N-867', 'score': 0.9975666503927089}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-967.html', 'title': 'N-967', 'score': 0.9974964537691671}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-647.html', 'title': 'N-647', 'score': 0.9972799038123997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-41.html', 'title': 'N-41', 'score': 0.9967962581341647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-13.html', 'title': 'N-13', 'score': 0.9967638125354805}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-231.html', 'title': 'N-231', 'score': 0.9965318426663146}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-824.html', 'title': 'N-824', 'score': 0.996002299552058}]
result = search.search('banana blueberry apricot orange cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'banana blueberry apricot orange cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'banana blueberry apricot orange cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'coconut kiwi apple lime apple cherry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-826.html', 'title': 'N-826', 'score': 0.9957876290396888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-787.html', 'title': 'N-787', 'score': 0.9942525600929831}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-843.html', 'title': 'N-843', 'score': 0.9929829492813959}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-90.html', 'title': 'N-90', 'score': 0.9913912883532009}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-311.html', 'title': 'N-311', 'score': 0.9907993178991724}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-394.html', 'title': 'N-394', 'score': 0.9901206157037186}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-763.html', 'title': 'N-763', 'score': 0.9900798562681922}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-593.html', 'title': 'N-593', 'score': 0.9896801384271721}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-958.html', 'title': 'N-958', 'score': 0.9894916798032739}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-525.html', 'title': 'N-525', 'score': 0.9890454545638117}]
result = search.search('coconut kiwi apple lime apple cherry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'coconut kiwi apple lime apple cherry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'coconut kiwi apple lime apple cherry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #460 checking search results for 'tomato peach orange tomato orange lime orange orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-953.html', 'title': 'N-953', 'score': 0.9999222881867892}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-736.html', 'title': 'N-736', 'score': 0.9993194913340115}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-885.html', 'title': 'N-885', 'score': 0.9981150412252171}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-666.html', 'title': 'N-666', 'score': 0.9979883944146039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-709.html', 'title': 'N-709', 'score': 0.9978090762242022}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-217.html', 'title': 'N-217', 'score': 0.9972015628420744}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-278.html', 'title': 'N-278', 'score': 0.9969132636710988}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-218.html', 'title': 'N-218', 'score': 0.996622167913588}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-232.html', 'title': 'N-232', 'score': 0.9954267185997505}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-897.html', 'title': 'N-897', 'score': 0.9941548577562114}]
result = search.search('tomato peach orange tomato orange lime orange orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #460 checking search results for 'tomato peach orange tomato orange lime orange orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #460 checking search results for 'tomato peach orange tomato orange lime orange orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #461 checking search results for 'apple lime banana pear lime fig peach lime' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-3.html', 'title': 'N-3', 'score': 0.015330174558113469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-1.html', 'title': 'N-1', 'score': 0.014984603338357574}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-0.html', 'title': 'N-0', 'score': 0.013198431820724192}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-12.html', 'title': 'N-12', 'score': 0.011802143018257907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-6.html', 'title': 'N-6', 'score': 0.008867180470470174}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-4.html', 'title': 'N-4', 'score': 0.007236932660096118}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-8.html', 'title': 'N-8', 'score': 0.006496335576608666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-15.html', 'title': 'N-15', 'score': 0.00647939273718803}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-32.html', 'title': 'N-32', 'score': 0.005984608271322926}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits4/N-9.html', 'title': 'N-9', 'score': 0.005921152638726563}]
result = search.search('apple lime banana pear lime fig peach lime',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #461 checking search results for 'apple lime banana pear lime fig peach lime' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #461 checking search results for 'apple lime banana pear lime fig peach lime' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
