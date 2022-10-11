
import testingtools
import crawler
import searchdata
import search

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html')


output = open('fruits5-all-outgoing-failed.txt', 'w')
success_output = open('fruits5-all-outgoing-passed.txt', 'w')

#Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-683.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-683.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-683.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-683.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-463.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-626.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-778.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-622.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-554.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-596.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-733.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-531.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-570.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-806.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-826.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-531.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-531.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-531.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-130.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-233.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-473.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-479.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-304.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-8.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-183.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-376.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-835.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-40.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-31.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-30.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-531.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-923.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-741.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-811.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-898.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-46.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-368.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-753.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-668.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-131.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-589.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-278.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-222.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-716.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-455.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-62.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-653.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-653.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-653.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-653.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-661.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-151.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-661.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-661.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-661.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-202.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-958.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-300.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-578.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-186.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-866.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-578.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-578.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-578.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-670.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-959.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-426.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-217.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-522.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-572.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-583.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-712.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-903.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-942.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-111.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-255.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-201.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-255.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-255.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-255.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-141.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-268.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-141.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-141.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-141.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-271.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-282.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-411.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-945.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-51.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-945.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-945.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-945.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-620.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-620.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-620.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-620.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-325.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-334.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-943.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-41.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-299.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-943.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-943.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-943.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-503.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-763.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-503.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-503.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-503.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-742.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-609.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-136.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-136.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-136.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-136.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-933.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-93.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-933.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-933.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-933.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-419.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-149.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-738.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-520.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-690.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-408.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-690.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-690.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-690.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-443.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-129.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-240.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-799.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-166.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-270.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-430.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-388.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-270.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-270.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-270.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-633.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-485.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-39.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-853.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-14.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-953.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-500.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-500.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-500.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-500.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-247.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-318.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-350.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-495.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-507.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-912.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-357.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-642.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-53.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-791.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-437.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-791.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-791.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-791.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-414.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-533.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-153.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-86.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-975.html']
result = searchdata.get_outgoing_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking outgoing links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html\n\n')
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









output = open('fruits5-all-incoming-failed.txt', 'w')
success_output = open('fruits5-all-incoming-passed.txt', 'w')

#Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-972.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-994.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-342.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-171.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-112.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-627.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-469.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-663.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-724.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-706.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-412.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-985.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-377.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-69.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-125.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-225.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-565.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-961.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-787.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-154.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-787.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-787.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-787.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-632.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-757.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-398.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-562.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-757.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-757.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-757.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-102.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-965.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-486.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-102.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-102.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-102.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-987.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-150.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-987.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-987.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-987.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-396.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-876.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-864.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-795.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-34.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-117.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-246.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-188.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-246.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-246.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #66 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-246.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-377.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-195.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-377.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-377.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #67 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-377.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-127.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-453.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #68 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-203.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-433.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #69 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-624.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-101.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-624.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-624.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #70 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-624.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-175.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-716.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-175.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-175.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #71 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-175.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-347.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-137.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-347.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-347.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #72 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-347.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #73 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-513.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #74 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-107.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #75 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-74.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-914.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-366.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-74.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-74.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #76 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-74.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-7.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-823.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-829.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-534.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #77 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-191.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #78 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-135.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-447.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-68.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-875.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #79 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-631.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-631.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-631.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #80 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-631.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-155.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-353.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #81 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-96.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #82 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #83 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-825.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-318.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-861.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #84 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-692.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-190.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-154.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-427.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-22.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-271.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-645.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-800.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-5.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-108.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-628.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-786.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-397.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-827.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-841.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #85 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-4.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-169.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #86 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-629.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #87 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #88 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-184.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #89 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-67.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-303.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-303.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-303.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #90 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-303.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-205.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-243.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-159.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-756.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #91 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-490.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-789.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-365.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-789.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-789.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #92 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-789.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-773.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-330.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-355.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-773.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-773.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #93 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-773.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-392.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-392.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-392.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #94 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-392.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-223.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-60.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-223.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-223.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #95 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-223.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-63.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-567.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #96 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-531.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-274.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-895.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #97 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-238.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-224.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-549.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-518.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #98 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-256.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #99 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-212.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html
expected = ['http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-66.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html', 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-980.html']
result = searchdata.get_incoming_links('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html')
if not testingtools.compare_unsorted_lists(expected, result):
  output.write('Failed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #100 checking incoming links for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html\n\n')
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









output = open('fruits5-all-pagerank-failed.txt', 'w')
success_output = open('fruits5-all-pagerank-passed.txt', 'w')

#Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html
expected = 0.0004511913111582482
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #102 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-944.html
expected = 0.0004674471026569333
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-944.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-944.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #103 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-944.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html
expected = 0.0008761886931068969
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #104 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-673.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html
expected = 0.0003827997889854634
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #105 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html
expected = 0.00035663076171876703
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #106 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-540.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html
expected = 0.0006361318036190639
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #107 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-399.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html
expected = 0.0027325101296903492
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #108 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-95.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-683.html
expected = 0.0003949000403119274
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-683.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-683.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #109 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-683.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html
expected = 0.0009609451521803732
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #110 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-91.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html
expected = 0.0035823548844784664
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #111 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-88.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-671.html
expected = 0.00035925602547880794
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-671.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-671.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #112 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-671.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html
expected = 0.00035451373937112806
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #113 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-222.html
expected = 0.0015285481858928142
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-222.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-222.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #114 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-222.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html
expected = 0.00041408813686226947
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #115 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-360.html
expected = 0.0014381392675236063
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-360.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-360.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #116 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-360.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html
expected = 0.0007327989483376267
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #117 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-703.html
expected = 0.0006633958947614839
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-703.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-703.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #118 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-703.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html
expected = 0.0006760202647360442
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #119 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html
expected = 0.0003804539804548974
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #120 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-812.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-312.html
expected = 0.0009600987000536588
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-312.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-312.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #121 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-312.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html
expected = 0.0023460571538229244
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #122 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-196.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-446.html
expected = 0.00036533971883514896
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-446.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-446.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #123 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-446.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html
expected = 0.0009222648485645562
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #124 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html
expected = 0.0006831749362623834
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #125 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html
expected = 0.0006165865651798642
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #126 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-915.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-518.html
expected = 0.0007777320450638774
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-518.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-518.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #127 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-518.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-113.html
expected = 0.0009191873339403809
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-113.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-113.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #128 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-113.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-856.html
expected = 0.000360004864997057
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-856.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-856.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #129 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-856.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html
expected = 0.0006555769979858365
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #130 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-855.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html
expected = 0.003145577267715368
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #131 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-35.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html
expected = 0.0012126258845619512
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #132 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html
expected = 0.0006185035900496878
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #133 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-979.html
expected = 0.0003557155967425787
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-979.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-979.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #134 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-979.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-432.html
expected = 0.001245091372725168
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-432.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-432.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #135 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-432.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html
expected = 0.004437582365803979
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #136 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html
expected = 0.00283224601187559
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #137 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html
expected = 0.0003520668302131229
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #138 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-601.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html
expected = 0.0006306319300624248
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #139 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-206.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-497.html
expected = 0.0003622716737841131
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-497.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-497.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #140 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-497.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-838.html
expected = 0.0004011813250807284
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-838.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-838.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #141 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-838.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html
expected = 0.0010139796223463274
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #142 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-167.html
expected = 0.0003684244750648093
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-167.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-167.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #143 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-167.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html
expected = 0.0009423859946335992
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #144 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-263.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html
expected = 0.00040915642256552775
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #145 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html
expected = 0.0014179444854222146
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #146 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-902.html
expected = 0.0003649743439592553
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-902.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-902.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #147 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-902.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html
expected = 0.000365912126428853
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #148 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-272.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-676.html
expected = 0.00037215864613469955
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-676.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-676.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #149 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-676.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-480.html
expected = 0.00041408813686226947
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-480.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-480.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #150 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-480.html\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html
expected = 0.0007984881367083571
result = searchdata.get_page_rank('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #151 checking page rank for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-362.html\n\n')
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









output = open('fruits5-all-idf-failed.txt', 'w')
success_output = open('fruits5-all-idf-passed.txt', 'w')

#Test #153 checking IDF for word fig
expected = 0.16650266314016507
result = searchdata.get_idf('fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #153 checking IDF for word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #153 checking IDF for word fig\n\n')
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


#Test #155 checking IDF for word coconut
expected = 0.1600404125104682
result = searchdata.get_idf('coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #155 checking IDF for word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #155 checking IDF for word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #156 checking IDF for word papaya
expected = 0.16650266314016507
result = searchdata.get_idf('papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #156 checking IDF for word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #156 checking IDF for word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #157 checking IDF for word pear
expected = 0.16812275880832706
result = searchdata.get_idf('pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #157 checking IDF for word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #157 checking IDF for word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #158 checking IDF for word blueberry
expected = 0.1729939903610231
result = searchdata.get_idf('blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #158 checking IDF for word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #158 checking IDF for word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #159 checking IDF for word apple
expected = 0.15521264992094008
result = searchdata.get_idf('apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #159 checking IDF for word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #159 checking IDF for word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #160 checking IDF for word lime
expected = 0.16326791954086414
result = searchdata.get_idf('lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #160 checking IDF for word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #160 checking IDF for word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #161 checking IDF for word banana
expected = 0.16326791954086414
result = searchdata.get_idf('banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #161 checking IDF for word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #161 checking IDF for word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #162 checking IDF for word kiwi
expected = 0.1729939903610231
result = searchdata.get_idf('kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #162 checking IDF for word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #162 checking IDF for word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #163 checking IDF for word cherry
expected = 0.15682010974282581
result = searchdata.get_idf('cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #163 checking IDF for word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #163 checking IDF for word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #164 checking IDF for word orange
expected = 0.16650266314016507
result = searchdata.get_idf('orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #164 checking IDF for word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #164 checking IDF for word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #165 checking IDF for word apricot
expected = 0.1729939903610231
result = searchdata.get_idf('apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #165 checking IDF for word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #165 checking IDF for word apricot\n\n')
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









output = open('fruits5-all-tf-failed.txt', 'w')
success_output = open('fruits5-all-tf-passed.txt', 'w')

#Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word cherry
expected = 0.0392156862745098
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #167 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word fig
expected = 0.0392156862745098
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #168 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word lime
expected = 0.1568627450980392
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #169 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word apple
expected = 0.0784313725490196
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #170 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word papaya
expected = 0.13725490196078433
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #171 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word blueberry
expected = 0.13725490196078433
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #172 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word apricot
expected = 0.09803921568627451
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #173 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word orange
expected = 0.0392156862745098
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #174 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word kiwi
expected = 0.0392156862745098
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #175 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word banana
expected = 0.0392156862745098
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #176 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #177 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-416.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word cherry
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #178 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word fig
expected = 0.027777777777777776
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #179 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word lime
expected = 0.1111111111111111
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #180 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word apple
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #181 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word papaya
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #182 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word blueberry
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #183 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word apricot
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #184 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word orange
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #185 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word kiwi
expected = 0.05555555555555555
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #186 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word banana
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #187 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #188 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-146.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word cherry
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #189 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word fig
expected = 0.05952380952380952
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #190 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word lime
expected = 0.023809523809523808
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #191 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word apple
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #192 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word papaya
expected = 0.10714285714285714
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #193 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word blueberry
expected = 0.11904761904761904
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #194 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word apricot
expected = 0.09523809523809523
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #195 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word orange
expected = 0.13095238095238096
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #196 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word kiwi
expected = 0.05952380952380952
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #197 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word banana
expected = 0.047619047619047616
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #198 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #199 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-585.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word cherry
expected = 0.03333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #200 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word fig
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #201 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #202 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word apple
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #203 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word papaya
expected = 0.1
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #204 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word blueberry
expected = 0.06666666666666667
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #205 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word apricot
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #206 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word orange
expected = 0.03333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #207 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word kiwi
expected = 0.13333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #208 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word banana
expected = 0.13333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #209 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #210 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-231.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word cherry
expected = 0.12280701754385964
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #211 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word fig
expected = 0.08771929824561403
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #212 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word lime
expected = 0.08771929824561403
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #213 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word apple
expected = 0.12280701754385964
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #214 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word papaya
expected = 0.03508771929824561
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #215 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word blueberry
expected = 0.12280701754385964
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #216 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word apricot
expected = 0.08771929824561403
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #217 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word orange
expected = 0.08771929824561403
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #218 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word kiwi
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #219 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word banana
expected = 0.07017543859649122
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #220 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #221 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-283.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word cherry
expected = 0.06818181818181818
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #222 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word fig
expected = 0.11363636363636363
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #223 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word lime
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #224 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word apple
expected = 0.056818181818181816
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #225 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word papaya
expected = 0.045454545454545456
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #226 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word blueberry
expected = 0.07954545454545454
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #227 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word apricot
expected = 0.056818181818181816
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #228 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word orange
expected = 0.07954545454545454
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #229 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word kiwi
expected = 0.10227272727272728
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #230 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word banana
expected = 0.06818181818181818
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #231 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #232 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word cherry
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #233 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word fig
expected = 0.10909090909090909
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #234 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word lime
expected = 0.07272727272727272
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #235 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word apple
expected = 0.05454545454545454
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #236 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word papaya
expected = 0.03636363636363636
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #237 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word blueberry
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #238 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word apricot
expected = 0.05454545454545454
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #239 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word orange
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #240 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word kiwi
expected = 0.03636363636363636
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #241 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word banana
expected = 0.09090909090909091
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #242 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #243 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-986.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word cherry
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #244 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #245 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #246 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word apple
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #247 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #248 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word blueberry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #249 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word apricot
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #250 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word orange
expected = 0.16666666666666666
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #251 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #252 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word banana
expected = 0.08333333333333333
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #253 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #254 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-351.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word cherry
expected = 0.03508771929824561
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #255 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word fig
expected = 0.14035087719298245
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #256 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word lime
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #257 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word apple
expected = 0.03508771929824561
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #258 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word papaya
expected = 0.15789473684210525
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #259 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word blueberry
expected = 0.08771929824561403
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #260 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word apricot
expected = 0.07017543859649122
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #261 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word orange
expected = 0.05263157894736842
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #262 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word kiwi
expected = 0.10526315789473684
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #263 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word banana
expected = 0.017543859649122806
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #264 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #265 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-92.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #266 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #267 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word lime
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #268 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #269 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word papaya
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #270 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word papaya\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word blueberry
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #271 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word apricot
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #272 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word orange
expected = 0.11764705882352941
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #273 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word kiwi
expected = 0.058823529411764705
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #274 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word banana
expected = 0.11764705882352941
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #275 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word tomato
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #276 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-157.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #277 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #278 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #279 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #280 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','papaya')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #281 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word papaya\n\n')
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


#Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apricot')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #283 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apricot\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','orange')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #284 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word orange\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #285 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0
result = searchdata.get_tf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #286 checking TF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
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









output = open('fruits5-all-tfidf-failed.txt', 'w')
success_output = open('fruits5-all-tfidf-passed.txt', 'w')

#Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word lime
expected = 0.011682352063921712
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #288 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word coconut
expected = 0.015145724375758824
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #289 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word cherry
expected = 0.011220990246402903
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #290 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word apple
expected = 0.018215283295189576
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #291 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word fig
expected = 0.008007827067304593
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #292 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word kiwi
expected = 0.008320022829471826
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #293 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word pear
expected = 0.02349091274147251
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #294 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #295 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word peach
expected = 0.011451413410915658
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #296 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word banana
expected = 0.029950869804532522
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #297 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #298 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-27.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #299 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word coconut
expected = 0.01776949703627324
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #300 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word cherry
expected = 0.0174119425936928
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #301 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word apple
expected = 0.01723346422005665
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #302 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #303 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word kiwi
expected = 0.019207749785150115
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #304 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word pear
expected = 0.018666890552904814
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #305 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word blueberry
expected = 0.02828429811658396
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #306 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word peach
expected = 0.009055651221051234
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #307 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word banana
expected = 0.034959711492051876
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #308 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #309 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-928.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word lime
expected = 0.005608498720288206
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #310 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word coconut
expected = 0.008198121880744038
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #311 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word cherry
expected = 0.025737219145061236
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #312 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word apple
expected = 0.010539569791727356
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #313 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word fig
expected = 0.01405152393207063
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #314 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word kiwi
expected = 0.017419456799583975
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #315 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word pear
expected = 0.01963903562341158
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #316 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word blueberry
expected = 0.03631542943988216
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #317 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word peach
expected = 0.023769606121698712
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #318 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word banana
expected = 0.016440099828119923
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #319 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #320 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-311.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word lime
expected = 0.01830402626828158
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #321 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word coconut
expected = 0.011376168336281751
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #322 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word cherry
expected = 0.013312286235464463
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #323 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word apple
expected = 0.01529835393656687
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #324 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word fig
expected = 0.02311518254973964
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #325 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word kiwi
expected = 0.014685269130839097
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #326 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word pear
expected = 0.014271755654442095
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #327 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word blueberry
expected = 0.014685269130839097
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #328 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word peach
expected = 0.013585654187304421
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #329 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word banana
expected = 0.024817228830548887
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #330 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #331 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-371.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word lime
expected = 0.003651946297834804
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #332 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word coconut
expected = 0.023965590777783694
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #333 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word cherry
expected = 0.01701881722173303
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #334 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word apple
expected = 0.016844368517770148
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #335 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word fig
expected = 0.041280591254076064
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #336 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word kiwi
expected = 0.011433032777019705
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #337 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word pear
expected = 0.01824543107172083
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #338 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word blueberry
expected = 0.02590535174818394
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #339 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word peach
expected = 0.007104853175165849
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #340 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word banana
expected = 0.017718562277474096
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #341 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #342 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-462.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word lime
expected = 0.016831860114449884
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #343 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word coconut
expected = 0.012483554197536504
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #344 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word cherry
expected = 0.004151375090797281
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #345 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word apple
expected = 0.01210697658820754
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #346 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word fig
expected = 0.017165341130945092
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #347 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word kiwi
expected = 0.02210094190060251
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #348 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word pear
expected = 0.013113997511633686
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #349 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word blueberry
expected = 0.004579533477052873
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #350 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word peach
expected = 0.02044605047412815
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #351 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word banana
expected = 0.02085838240088298
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #352 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #353 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-140.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word lime
expected = 0.026198733188798045
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #354 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word coconut
expected = 0.006692918169428345
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #355 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word cherry
expected = 0.009767427351098729
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #356 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word apple
expected = 0.018934472554049137
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #357 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word fig
expected = 0.017043498588942933
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #358 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word kiwi
expected = 0.017707961992966245
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #359 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word pear
expected = 0.013863765868768701
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #360 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word blueberry
expected = 0.024453712421857454
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #361 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word peach
expected = 0.013197278133627663
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #362 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word banana
expected = 0.003438686149398293
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #363 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #364 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word lime
expected = 0.03630954795325715
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #365 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #366 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word cherry
expected = 0.034875603919954534
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #367 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #368 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word fig
expected = 0.03702893041470826
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #369 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #370 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #371 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #372 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #373 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word banana
expected = 0.06776230903869972
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #374 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #375 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-474.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word lime
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #376 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #377 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word cherry
expected = 0.02664765737423326
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #378 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word apple
expected = 0.02637450976168087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #379 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #380 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word kiwi
expected = 0.015130545916208906
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #381 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word pear
expected = 0.02856826003299051
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #382 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word blueberry
expected = 0.029396004061608222
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #383 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word peach
expected = 0.027194867326669574
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #384 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word banana
expected = 0.014279876128075786
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #385 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #386 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-973.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word lime
expected = 0.019640189271853268
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','lime')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word lime\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #387 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word lime\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word coconut
expected = 0.019251938786813257
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #388 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word cherry
expected = 0.02334477251579782
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #389 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word apple
expected = 0.014147305240209723
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #390 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word fig
expected = 0.020029310274404445
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #391 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word kiwi
expected = 0.020810179508248483
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #392 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word pear
expected = 0.015324034399896384
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #393 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word blueberry
expected = 0.025752471147999296
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #394 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word peach
expected = 0.009826568496416917
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #395 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word banana
expected = 0.019640189271853268
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #396 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #397 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html and word tomato\n\n')
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


#Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #399 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','cherry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #400 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word cherry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #401 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','fig')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #402 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word fig\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','kiwi')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #403 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word kiwi\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #404 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','blueberry')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #405 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word blueberry\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #406 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #407 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
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









output = open('fruits5-all-search-failed.txt', 'w')
success_output = open('fruits5-all-search-passed.txt', 'w')

#Test #409 checking search results for 'blueberry apple fig blueberry banana coconut banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-9.html', 'title': 'N-9', 'score': 0.9969049075148041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-595.html', 'title': 'N-595', 'score': 0.9957734265776538}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-934.html', 'title': 'N-934', 'score': 0.9944964335410302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-546.html', 'title': 'N-546', 'score': 0.9939528946984846}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html', 'title': 'N-974', 'score': 0.9934981628858722}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html', 'title': 'N-937', 'score': 0.9896168085335149}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-921.html', 'title': 'N-921', 'score': 0.9895469393027841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-289.html', 'title': 'N-289', 'score': 0.9889255395172669}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9886554159251845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 0.9879913777155961}]
result = search.search('blueberry apple fig blueberry banana coconut banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #409 checking search results for 'blueberry apple fig blueberry banana coconut banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #409 checking search results for 'blueberry apple fig blueberry banana coconut banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #410 checking search results for 'lime papaya apple cherry banana cherry fig papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9916622524264544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9904252351276309}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-597.html', 'title': 'N-597', 'score': 0.9901700226843757}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-494.html', 'title': 'N-494', 'score': 0.9900635027400696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-285.html', 'title': 'N-285', 'score': 0.9891761784587387}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-264.html', 'title': 'N-264', 'score': 0.9884670839438094}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-957.html', 'title': 'N-957', 'score': 0.9866382006259464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.9866152874917683}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0.9862193975539911}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-894.html', 'title': 'N-894', 'score': 0.9853683367303858}]
result = search.search('lime papaya apple cherry banana cherry fig papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #410 checking search results for 'lime papaya apple cherry banana cherry fig papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #410 checking search results for 'lime papaya apple cherry banana cherry fig papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #411 checking search results for 'lime banana blueberry pear apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-484.html', 'title': 'N-484', 'score': 0.9979479042468004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html', 'title': 'N-865', 'score': 0.9971905316038524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9968560707992631}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-102.html', 'title': 'N-102', 'score': 0.996405007086078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9963215039649468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html', 'title': 'N-550', 'score': 0.9961421806091167}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9956655758540067}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-98.html', 'title': 'N-98', 'score': 0.9956022371246469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-232.html', 'title': 'N-232', 'score': 0.9954022041594054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.994970618867333}]
result = search.search('lime banana blueberry pear apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #411 checking search results for 'lime banana blueberry pear apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #411 checking search results for 'lime banana blueberry pear apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #412 checking search results for 'orange blueberry cherry blueberry apple apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-971.html', 'title': 'N-971', 'score': 0.9997664248659479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-740.html', 'title': 'N-740', 'score': 0.9997049294221321}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9983126497632198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html', 'title': 'N-711', 'score': 0.9971445889344605}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-549.html', 'title': 'N-549', 'score': 0.9971108731419087}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html', 'title': 'N-614', 'score': 0.9960147895922645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'title': 'N-128', 'score': 0.9954077719067161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-230.html', 'title': 'N-230', 'score': 0.995003010087476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-189.html', 'title': 'N-189', 'score': 0.9948057649309271}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-223.html', 'title': 'N-223', 'score': 0.9946925150978729}]
result = search.search('orange blueberry cherry blueberry apple apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #412 checking search results for 'orange blueberry cherry blueberry apple apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #412 checking search results for 'orange blueberry cherry blueberry apple apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #413 checking search results for 'papaya pear cherry peach fig papaya apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-332.html', 'title': 'N-332', 'score': 0.9950713654110919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9920154835021809}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-261.html', 'title': 'N-261', 'score': 0.9914280657482946}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-711.html', 'title': 'N-711', 'score': 0.9914106585862482}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-286.html', 'title': 'N-286', 'score': 0.9912125917533104}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-339.html', 'title': 'N-339', 'score': 0.9899747515852101}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-588.html', 'title': 'N-588', 'score': 0.9897574080821255}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html', 'title': 'N-439', 'score': 0.9897279297496788}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9892828720157506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9891302451684058}]
result = search.search('papaya pear cherry peach fig papaya apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #413 checking search results for 'papaya pear cherry peach fig papaya apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #413 checking search results for 'papaya pear cherry peach fig papaya apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #414 checking search results for 'orange apricot lime orange blueberry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-114.html', 'title': 'N-114', 'score': 0.999817566715553}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-946.html', 'title': 'N-946', 'score': 0.99808176589185}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-71.html', 'title': 'N-71', 'score': 0.9968704535199944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-964.html', 'title': 'N-964', 'score': 0.9959604276376518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-817.html', 'title': 'N-817', 'score': 0.9950394803460619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-338.html', 'title': 'N-338', 'score': 0.9948757959285647}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-636.html', 'title': 'N-636', 'score': 0.9948585112237106}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-876.html', 'title': 'N-876', 'score': 0.9947958899874402}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-854.html', 'title': 'N-854', 'score': 0.9946561147451786}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'title': 'N-199', 'score': 0.9940966947993887}]
result = search.search('orange apricot lime orange blueberry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #414 checking search results for 'orange apricot lime orange blueberry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #414 checking search results for 'orange apricot lime orange blueberry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #415 checking search results for 'orange peach apple apricot apple banana coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-531.html', 'title': 'N-531', 'score': 0.9999215186937142}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-662.html', 'title': 'N-662', 'score': 0.9899286416680557}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-956.html', 'title': 'N-956', 'score': 0.9895100317524279}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-816.html', 'title': 'N-816', 'score': 0.9884248686587347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-450.html', 'title': 'N-450', 'score': 0.9879316375126853}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-316.html', 'title': 'N-316', 'score': 0.9864967489276881}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.9864820562213699}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-860.html', 'title': 'N-860', 'score': 0.9861744765173468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-792.html', 'title': 'N-792', 'score': 0.9855475231861133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-542.html', 'title': 'N-542', 'score': 0.9849078265576466}]
result = search.search('orange peach apple apricot apple banana coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #415 checking search results for 'orange peach apple apricot apple banana coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #415 checking search results for 'orange peach apple apricot apple banana coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #416 checking search results for 'peach orange fig kiwi peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-514.html', 'title': 'N-514', 'score': 0.9997440246228341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-144.html', 'title': 'N-144', 'score': 0.9996702919086942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.999630507868133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 0.9996128821476037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-893.html', 'title': 'N-893', 'score': 0.9984147013639572}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9977276560756893}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-78.html', 'title': 'N-78', 'score': 0.9968569028406771}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9963925747419918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'title': 'N-211', 'score': 0.9962294741849015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-277.html', 'title': 'N-277', 'score': 0.9960158839720464}]
result = search.search('peach orange fig kiwi peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #416 checking search results for 'peach orange fig kiwi peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #416 checking search results for 'peach orange fig kiwi peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #417 checking search results for 'banana fig apple coconut coconut' and boost = True
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-2.html', 'title': 'N-2', 'score': 0.014364104421961314}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-0.html', 'title': 'N-0', 'score': 0.011336587098164532}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-3.html', 'title': 'N-3', 'score': 0.008350382742413003}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-10.html', 'title': 'N-10', 'score': 0.006725302259032555}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-13.html', 'title': 'N-13', 'score': 0.006643724810215061}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.006221717460444767}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-12.html', 'title': 'N-12', 'score': 0.006078219445594577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-15.html', 'title': 'N-15', 'score': 0.005869918255829056}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.005373780868315852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-11.html', 'title': 'N-11', 'score': 0.005177321040763518}]
result = search.search('banana fig apple coconut coconut',True)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #417 checking search results for 'banana fig apple coconut coconut' and boost = True\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #417 checking search results for 'banana fig apple coconut coconut' and boost = True\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #418 checking search results for 'banana cherry apricot fig coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-306.html', 'title': 'N-306', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-558.html', 'title': 'N-558', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-685.html', 'title': 'N-685', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-308.html', 'title': 'N-308', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-239.html', 'title': 'N-239', 'score': 0.9968342485261646}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-441.html', 'title': 'N-441', 'score': 0.9967221464915427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html', 'title': 'N-539', 'score': 0.9961523082770639}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-968.html', 'title': 'N-968', 'score': 0.9960526171649197}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-356.html', 'title': 'N-356', 'score': 0.995963373105628}]
result = search.search('banana cherry apricot fig coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #418 checking search results for 'banana cherry apricot fig coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #418 checking search results for 'banana cherry apricot fig coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #419 checking search results for 'blueberry fig fig papaya banana pear coconut papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html', 'title': 'N-245', 'score': 0.9906098492597452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-714.html', 'title': 'N-714', 'score': 0.9890407784280897}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-903.html', 'title': 'N-903', 'score': 0.9870798751231886}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-954.html', 'title': 'N-954', 'score': 0.9869724643123028}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-773.html', 'title': 'N-773', 'score': 0.9868394216054578}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-133.html', 'title': 'N-133', 'score': 0.9864253030280055}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-677.html', 'title': 'N-677', 'score': 0.9841409635334416}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9841230605966609}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9826542671683525}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-730.html', 'title': 'N-730', 'score': 0.9821032148959183}]
result = search.search('blueberry fig fig papaya banana pear coconut papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #419 checking search results for 'blueberry fig fig papaya banana pear coconut papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #419 checking search results for 'blueberry fig fig papaya banana pear coconut papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #420 checking search results for 'papaya cherry lime fig kiwi banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.997555725720238}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-798.html', 'title': 'N-798', 'score': 0.9959769523276297}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 0.9958817849833581}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-180.html', 'title': 'N-180', 'score': 0.9952275502542097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-450.html', 'title': 'N-450', 'score': 0.9943185583706804}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9942114523665636}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-559.html', 'title': 'N-559', 'score': 0.9931778975118603}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-36.html', 'title': 'N-36', 'score': 0.9924484205215583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-824.html', 'title': 'N-824', 'score': 0.9921709801875715}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html', 'title': 'N-84', 'score': 0.9917668163781158}]
result = search.search('papaya cherry lime fig kiwi banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #420 checking search results for 'papaya cherry lime fig kiwi banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #420 checking search results for 'papaya cherry lime fig kiwi banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #421 checking search results for 'coconut tomato orange kiwi apricot apricot apricot blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9949752980269261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-253.html', 'title': 'N-253', 'score': 0.9907487753932971}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'title': 'N-106', 'score': 0.9897501074367204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html', 'title': 'N-617', 'score': 0.9893568753311014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 0.9860305459013301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-724.html', 'title': 'N-724', 'score': 0.98572096111885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html', 'title': 'N-634', 'score': 0.9834674818920468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html', 'title': 'N-516', 'score': 0.980990569055976}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-561.html', 'title': 'N-561', 'score': 0.9808755621978725}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-805.html', 'title': 'N-805', 'score': 0.9807893659863486}]
result = search.search('coconut tomato orange kiwi apricot apricot apricot blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #421 checking search results for 'coconut tomato orange kiwi apricot apricot apricot blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #421 checking search results for 'coconut tomato orange kiwi apricot apricot apricot blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #422 checking search results for 'kiwi orange fig lime orange coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9974825866998864}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-32.html', 'title': 'N-32', 'score': 0.9957640314020991}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9949425293337265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-889.html', 'title': 'N-889', 'score': 0.9931861758026841}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-577.html', 'title': 'N-577', 'score': 0.9928897328390084}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html', 'title': 'N-704', 'score': 0.9921362093471341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'title': 'N-429', 'score': 0.9912091052906483}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-935.html', 'title': 'N-935', 'score': 0.990686494159776}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-147.html', 'title': 'N-147', 'score': 0.9905825588902313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-19.html', 'title': 'N-19', 'score': 0.9896129929140758}]
result = search.search('kiwi orange fig lime orange coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #422 checking search results for 'kiwi orange fig lime orange coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #422 checking search results for 'kiwi orange fig lime orange coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #423 checking search results for 'lime blueberry apricot coconut papaya pear banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9963363113866281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9963092041553666}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-865.html', 'title': 'N-865', 'score': 0.9949396629448435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-394.html', 'title': 'N-394', 'score': 0.9931385223195424}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-833.html', 'title': 'N-833', 'score': 0.992911138345494}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-164.html', 'title': 'N-164', 'score': 0.9916284849193231}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-846.html', 'title': 'N-846', 'score': 0.9897915022976183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9896269376602164}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-546.html', 'title': 'N-546', 'score': 0.9895397999004294}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.98860391544257}]
result = search.search('lime blueberry apricot coconut papaya pear banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #423 checking search results for 'lime blueberry apricot coconut papaya pear banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #423 checking search results for 'lime blueberry apricot coconut papaya pear banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #424 checking search results for 'pear papaya apple apricot coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-768.html', 'title': 'N-768', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html', 'title': 'N-291', 'score': 0.9979717447224364}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9979688111819464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-614.html', 'title': 'N-614', 'score': 0.9976876791962522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-208.html', 'title': 'N-208', 'score': 0.9970507962487524}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html', 'title': 'N-415', 'score': 0.9967122046750261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.9966616026582934}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9961439924702153}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-667.html', 'title': 'N-667', 'score': 0.9960221060837097}]
result = search.search('pear papaya apple apricot coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #424 checking search results for 'pear papaya apple apricot coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #424 checking search results for 'pear papaya apple apricot coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #425 checking search results for 'cherry apricot papaya kiwi lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-364.html', 'title': 'N-364', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-218.html', 'title': 'N-218', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.997988825293758}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-974.html', 'title': 'N-974', 'score': 0.9948321733742964}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-180.html', 'title': 'N-180', 'score': 0.9947761536330963}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-70.html', 'title': 'N-70', 'score': 0.9945987709603998}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9943996220939795}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-886.html', 'title': 'N-886', 'score': 0.9942992074631251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9942458199369584}]
result = search.search('cherry apricot papaya kiwi lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #425 checking search results for 'cherry apricot papaya kiwi lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #425 checking search results for 'cherry apricot papaya kiwi lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #426 checking search results for 'kiwi apricot apricot lime apricot fig apple fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-658.html', 'title': 'N-658', 'score': 0.9935705045684088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-106.html', 'title': 'N-106', 'score': 0.990724891303391}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-377.html', 'title': 'N-377', 'score': 0.9898805360888518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-21.html', 'title': 'N-21', 'score': 0.9886802045540344}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.986293638829512}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-512.html', 'title': 'N-512', 'score': 0.9856478868540827}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 0.9854333456445983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-133.html', 'title': 'N-133', 'score': 0.985323388884408}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 0.9850875952279354}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-276.html', 'title': 'N-276', 'score': 0.9841808617418484}]
result = search.search('kiwi apricot apricot lime apricot fig apple fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #426 checking search results for 'kiwi apricot apricot lime apricot fig apple fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #426 checking search results for 'kiwi apricot apricot lime apricot fig apple fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #427 checking search results for 'lime banana lime pear lime coconut kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-774.html', 'title': 'N-774', 'score': 0.9997381082272179}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-209.html', 'title': 'N-209', 'score': 0.999477871914464}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-68.html', 'title': 'N-68', 'score': 0.9885041529116092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-751.html', 'title': 'N-751', 'score': 0.9875961458545814}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-373.html', 'title': 'N-373', 'score': 0.9849888811941634}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-759.html', 'title': 'N-759', 'score': 0.9838299910644561}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-258.html', 'title': 'N-258', 'score': 0.9815648162178329}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-48.html', 'title': 'N-48', 'score': 0.9814872383881481}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-28.html', 'title': 'N-28', 'score': 0.9814363568895657}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-479.html', 'title': 'N-479', 'score': 0.9812741541053213}]
result = search.search('lime banana lime pear lime coconut kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #427 checking search results for 'lime banana lime pear lime coconut kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #427 checking search results for 'lime banana lime pear lime coconut kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #428 checking search results for 'lime pear apricot kiwi fig orange coconut' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.9984588484854435}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9945169943413403}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html', 'title': 'N-539', 'score': 0.9931531154597558}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-473.html', 'title': 'N-473', 'score': 0.9928865673884002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9919432544037183}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9918690195699289}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html', 'title': 'N-320', 'score': 0.9911754273024302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-439.html', 'title': 'N-439', 'score': 0.9911667349463664}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-105.html', 'title': 'N-105', 'score': 0.9907898726645258}]
result = search.search('lime pear apricot kiwi fig orange coconut',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #428 checking search results for 'lime pear apricot kiwi fig orange coconut' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #428 checking search results for 'lime pear apricot kiwi fig orange coconut' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #429 checking search results for 'banana coconut kiwi orange lime peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-182.html', 'title': 'N-182', 'score': 1.0000000000000004}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html', 'title': 'N-678', 'score': 0.9975556290081977}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-498.html', 'title': 'N-498', 'score': 0.997479663564417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9959264267533428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9957928918205312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-320.html', 'title': 'N-320', 'score': 0.9956680451415097}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9951648891802427}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html', 'title': 'N-760', 'score': 0.9934584567184847}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-245.html', 'title': 'N-245', 'score': 0.9924101191512432}]
result = search.search('banana coconut kiwi orange lime peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #429 checking search results for 'banana coconut kiwi orange lime peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #429 checking search results for 'banana coconut kiwi orange lime peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #430 checking search results for 'blueberry banana orange banana papaya fig apricot banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'title': 'N-273', 'score': 0.992625029356224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 0.9889512355067899}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 0.9867443713722189}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-154.html', 'title': 'N-154', 'score': 0.9840660636593948}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.9810723797263298}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-211.html', 'title': 'N-211', 'score': 0.9798026324746187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-754.html', 'title': 'N-754', 'score': 0.9792685632265992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-834.html', 'title': 'N-834', 'score': 0.9783634484172887}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html', 'title': 'N-746', 'score': 0.9772518235845983}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-897.html', 'title': 'N-897', 'score': 0.9767979571681417}]
result = search.search('blueberry banana orange banana papaya fig apricot banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #430 checking search results for 'blueberry banana orange banana papaya fig apricot banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #430 checking search results for 'blueberry banana orange banana papaya fig apricot banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #431 checking search results for 'blueberry pear orange peach lime coconut kiwi pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html', 'title': 'N-678', 'score': 0.9959940645441869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'title': 'N-297', 'score': 0.9837824561980334}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-204.html', 'title': 'N-204', 'score': 0.9818693609460736}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-225.html', 'title': 'N-225', 'score': 0.9811935303261637}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-737.html', 'title': 'N-737', 'score': 0.9803822170617869}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-523.html', 'title': 'N-523', 'score': 0.9795888648005602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-752.html', 'title': 'N-752', 'score': 0.9794035862817443}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html', 'title': 'N-84', 'score': 0.9777531538258825}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-429.html', 'title': 'N-429', 'score': 0.9770335924972973}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-844.html', 'title': 'N-844', 'score': 0.9766751987425899}]
result = search.search('blueberry pear orange peach lime coconut kiwi pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #431 checking search results for 'blueberry pear orange peach lime coconut kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #431 checking search results for 'blueberry pear orange peach lime coconut kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #432 checking search results for 'cherry lime banana blueberry kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html', 'title': 'N-672', 'score': 0.9979541421474506}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9962745317999312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9960911344193848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 0.9959458421056518}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-664.html', 'title': 'N-664', 'score': 0.9956706283364196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-450.html', 'title': 'N-450', 'score': 0.9950899251325648}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-448.html', 'title': 'N-448', 'score': 0.9944131927472312}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-539.html', 'title': 'N-539', 'score': 0.9944122482560162}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-765.html', 'title': 'N-765', 'score': 0.9942638821925885}]
result = search.search('cherry lime banana blueberry kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #432 checking search results for 'cherry lime banana blueberry kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #432 checking search results for 'cherry lime banana blueberry kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #433 checking search results for 'pear orange pear apricot fig fig kiwi' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-305.html', 'title': 'N-305', 'score': 0.9999720645775954}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-417.html', 'title': 'N-417', 'score': 0.9998062263581468}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-593.html', 'title': 'N-593', 'score': 0.9948581689161576}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9945271045098135}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-853.html', 'title': 'N-853', 'score': 0.9938410017472259}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-387.html', 'title': 'N-387', 'score': 0.9937395186784199}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-759.html', 'title': 'N-759', 'score': 0.9924061877321779}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-744.html', 'title': 'N-744', 'score': 0.9915885279240527}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-168.html', 'title': 'N-168', 'score': 0.9915179022706015}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-524.html', 'title': 'N-524', 'score': 0.9892943809465601}]
result = search.search('pear orange pear apricot fig fig kiwi',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #433 checking search results for 'pear orange pear apricot fig fig kiwi' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #433 checking search results for 'pear orange pear apricot fig fig kiwi' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #434 checking search results for 'peach tomato lime cherry cherry kiwi cherry blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-187.html', 'title': 'N-187', 'score': 0.9997564431596335}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-920.html', 'title': 'N-920', 'score': 0.9912683150659358}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-977.html', 'title': 'N-977', 'score': 0.9909024199690131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-752.html', 'title': 'N-752', 'score': 0.9904622770137794}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html', 'title': 'N-525', 'score': 0.9897355571632471}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 0.9896734716612919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-858.html', 'title': 'N-858', 'score': 0.9889793878574635}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-684.html', 'title': 'N-684', 'score': 0.9870922223014642}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-396.html', 'title': 'N-396', 'score': 0.986482200820601}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-590.html', 'title': 'N-590', 'score': 0.9863414575692185}]
result = search.search('peach tomato lime cherry cherry kiwi cherry blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #434 checking search results for 'peach tomato lime cherry cherry kiwi cherry blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #434 checking search results for 'peach tomato lime cherry cherry kiwi cherry blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #435 checking search results for 'lime orange papaya peach blueberry lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-814.html', 'title': 'N-814', 'score': 0.9952280333110417}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-406.html', 'title': 'N-406', 'score': 0.994849591044313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-33.html', 'title': 'N-33', 'score': 0.9945214836027818}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-689.html', 'title': 'N-689', 'score': 0.9935394549773071}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-24.html', 'title': 'N-24', 'score': 0.9935276241154316}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html', 'title': 'N-969', 'score': 0.993090113862599}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html', 'title': 'N-293', 'score': 0.9927245164786465}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9925778707588822}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-759.html', 'title': 'N-759', 'score': 0.992495196276251}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.9912176438783245}]
result = search.search('lime orange papaya peach blueberry lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #435 checking search results for 'lime orange papaya peach blueberry lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #435 checking search results for 'lime orange papaya peach blueberry lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #436 checking search results for 'peach orange orange banana coconut tomato blueberry apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.9926327423631306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.9918196516233787}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-963.html', 'title': 'N-963', 'score': 0.9917378033217645}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-44.html', 'title': 'N-44', 'score': 0.9902667313586224}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-903.html', 'title': 'N-903', 'score': 0.98970287875305}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-525.html', 'title': 'N-525', 'score': 0.9893685940968888}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.986905992451749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html', 'title': 'N-672', 'score': 0.9867225446157163}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-257.html', 'title': 'N-257', 'score': 0.9854491577025021}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-777.html', 'title': 'N-777', 'score': 0.9846547258722622}]
result = search.search('peach orange orange banana coconut tomato blueberry apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #436 checking search results for 'peach orange orange banana coconut tomato blueberry apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #436 checking search results for 'peach orange orange banana coconut tomato blueberry apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #437 checking search results for 'cherry papaya blueberry fig banana kiwi apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9927894280983351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-918.html', 'title': 'N-918', 'score': 0.9908864522190213}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.9908651479209907}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html', 'title': 'N-415', 'score': 0.9852198946980318}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'title': 'N-674', 'score': 0.985009428809123}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 0.9831354852735388}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-689.html', 'title': 'N-689', 'score': 0.9824277784552412}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-743.html', 'title': 'N-743', 'score': 0.9786663215636014}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-505.html', 'title': 'N-505', 'score': 0.9768700716630092}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-74.html', 'title': 'N-74', 'score': 0.9763009048581549}]
result = search.search('cherry papaya blueberry fig banana kiwi apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #437 checking search results for 'cherry papaya blueberry fig banana kiwi apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #437 checking search results for 'cherry papaya blueberry fig banana kiwi apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #438 checking search results for 'lime apple papaya blueberry coconut orange peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9943862508353437}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-876.html', 'title': 'N-876', 'score': 0.9930325192932246}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-760.html', 'title': 'N-760', 'score': 0.9925791348466939}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-270.html', 'title': 'N-270', 'score': 0.9917780288442434}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-291.html', 'title': 'N-291', 'score': 0.991388574422979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html', 'title': 'N-84', 'score': 0.9908804488808151}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'title': 'N-651', 'score': 0.9905159210686396}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-506.html', 'title': 'N-506', 'score': 0.9901297526659879}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9897662179583261}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'title': 'N-297', 'score': 0.9887015382802996}]
result = search.search('lime apple papaya blueberry coconut orange peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #438 checking search results for 'lime apple papaya blueberry coconut orange peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #438 checking search results for 'lime apple papaya blueberry coconut orange peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #439 checking search results for 'lime apricot pear apple apricot cherry coconut orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-617.html', 'title': 'N-617', 'score': 0.9945229717430916}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-680.html', 'title': 'N-680', 'score': 0.9911296436020658}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-623.html', 'title': 'N-623', 'score': 0.9899379848533901}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-296.html', 'title': 'N-296', 'score': 0.9897229480593194}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-504.html', 'title': 'N-504', 'score': 0.9869243594523125}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-42.html', 'title': 'N-42', 'score': 0.9857824999705762}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-516.html', 'title': 'N-516', 'score': 0.9857030803097997}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-651.html', 'title': 'N-651', 'score': 0.9853824974152204}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9842271666480615}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-891.html', 'title': 'N-891', 'score': 0.9811550385000131}]
result = search.search('lime apricot pear apple apricot cherry coconut orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #439 checking search results for 'lime apricot pear apple apricot cherry coconut orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #439 checking search results for 'lime apricot pear apple apricot cherry coconut orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #440 checking search results for 'lime pear papaya lime apricot banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-271.html', 'title': 'N-271', 'score': 0.9967344490801041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html', 'title': 'N-142', 'score': 0.9964931394654606}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-751.html', 'title': 'N-751', 'score': 0.9953069072379944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-689.html', 'title': 'N-689', 'score': 0.9931868851757548}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-527.html', 'title': 'N-527', 'score': 0.9927424187407373}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-250.html', 'title': 'N-250', 'score': 0.991128267875734}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'title': 'N-254', 'score': 0.9900584856960981}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-235.html', 'title': 'N-235', 'score': 0.9898954253087349}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-610.html', 'title': 'N-610', 'score': 0.9897608538105563}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-199.html', 'title': 'N-199', 'score': 0.9892335251413759}]
result = search.search('lime pear papaya lime apricot banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #440 checking search results for 'lime pear papaya lime apricot banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #440 checking search results for 'lime pear papaya lime apricot banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #441 checking search results for 'apple papaya fig fig blueberry kiwi pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-931.html', 'title': 'N-931', 'score': 0.9958151673223665}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html', 'title': 'N-138', 'score': 0.9942029168470513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-734.html', 'title': 'N-734', 'score': 0.9921283868807622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.991340219017301}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-415.html', 'title': 'N-415', 'score': 0.9910889905220552}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-625.html', 'title': 'N-625', 'score': 0.9903512124173036}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-801.html', 'title': 'N-801', 'score': 0.9897897460856039}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-65.html', 'title': 'N-65', 'score': 0.9897434077075904}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9887900765522161}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'title': 'N-55', 'score': 0.9886993913296748}]
result = search.search('apple papaya fig fig blueberry kiwi pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #441 checking search results for 'apple papaya fig fig blueberry kiwi pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #441 checking search results for 'apple papaya fig fig blueberry kiwi pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #442 checking search results for 'blueberry coconut blueberry apple peach coconut apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-422.html', 'title': 'N-422', 'score': 0.998182988890885}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-99.html', 'title': 'N-99', 'score': 0.9925769399821196}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-266.html', 'title': 'N-266', 'score': 0.9913816790594544}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-602.html', 'title': 'N-602', 'score': 0.9905979881850905}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-960.html', 'title': 'N-960', 'score': 0.9900935416877499}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-528.html', 'title': 'N-528', 'score': 0.9895570618411187}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html', 'title': 'N-719', 'score': 0.989210513652813}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-148.html', 'title': 'N-148', 'score': 0.9889330314457193}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9888999527924529}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html', 'title': 'N-600', 'score': 0.9882490161662147}]
result = search.search('blueberry coconut blueberry apple peach coconut apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #442 checking search results for 'blueberry coconut blueberry apple peach coconut apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #442 checking search results for 'blueberry coconut blueberry apple peach coconut apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #443 checking search results for 'tomato kiwi lime lime banana tomato cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-885.html', 'title': 'N-885', 'score': 0.9999671544965684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-458.html', 'title': 'N-458', 'score': 0.9999105954204466}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-809.html', 'title': 'N-809', 'score': 0.999838752926895}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-110.html', 'title': 'N-110', 'score': 0.9998120667588452}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-939.html', 'title': 'N-939', 'score': 0.9983048847298129}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-293.html', 'title': 'N-293', 'score': 0.9979784746435363}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-128.html', 'title': 'N-128', 'score': 0.997491105931093}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-717.html', 'title': 'N-717', 'score': 0.9974839429549383}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-701.html', 'title': 'N-701', 'score': 0.997350401877918}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.9971822751300414}]
result = search.search('tomato kiwi lime lime banana tomato cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #443 checking search results for 'tomato kiwi lime lime banana tomato cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #443 checking search results for 'tomato kiwi lime lime banana tomato cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #444 checking search results for 'fig lime orange apple pear pear' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-678.html', 'title': 'N-678', 'score': 0.9966898729884865}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-418.html', 'title': 'N-418', 'score': 0.9948077997154083}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-185.html', 'title': 'N-185', 'score': 0.9936237104642718}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-160.html', 'title': 'N-160', 'score': 0.9935042642930583}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-378.html', 'title': 'N-378', 'score': 0.9924111986433848}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-634.html', 'title': 'N-634', 'score': 0.9922846646124281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9915279726334979}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-746.html', 'title': 'N-746', 'score': 0.9912387243831273}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-950.html', 'title': 'N-950', 'score': 0.989674552898992}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-535.html', 'title': 'N-535', 'score': 0.9892423511179165}]
result = search.search('fig lime orange apple pear pear',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #444 checking search results for 'fig lime orange apple pear pear' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #444 checking search results for 'fig lime orange apple pear pear' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #445 checking search results for 'pear kiwi orange fig lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-390.html', 'title': 'N-390', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-440.html', 'title': 'N-440', 'score': 0.9987890451923542}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-226.html', 'title': 'N-226', 'score': 0.9972711993637684}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-544.html', 'title': 'N-544', 'score': 0.9965753827581486}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-798.html', 'title': 'N-798', 'score': 0.9957679200817793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 0.995003597826206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-464.html', 'title': 'N-464', 'score': 0.994949129498088}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-322.html', 'title': 'N-322', 'score': 0.9948672728491164}]
result = search.search('pear kiwi orange fig lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #445 checking search results for 'pear kiwi orange fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #445 checking search results for 'pear kiwi orange fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #446 checking search results for 'coconut blueberry papaya fig peach apricot kiwi tomato' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-553.html', 'title': 'N-553', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-219.html', 'title': 'N-219', 'score': 0.9968435634528223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9964292963083428}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-270.html', 'title': 'N-270', 'score': 0.9925654265331649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 0.9911437884480045}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9892518223127793}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'title': 'N-273', 'score': 0.9879521823791828}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-210.html', 'title': 'N-210', 'score': 0.9877993366315158}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.9877011283725385}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-1.html', 'title': 'N-1', 'score': 0.9869492443723156}]
result = search.search('coconut blueberry papaya fig peach apricot kiwi tomato',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #446 checking search results for 'coconut blueberry papaya fig peach apricot kiwi tomato' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #446 checking search results for 'coconut blueberry papaya fig peach apricot kiwi tomato' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #447 checking search results for 'kiwi fig fig coconut fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-853.html', 'title': 'N-853', 'score': 0.9996388945689522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-730.html', 'title': 'N-730', 'score': 0.9994610088572806}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-29.html', 'title': 'N-29', 'score': 0.9991464028671782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-892.html', 'title': 'N-892', 'score': 0.9989684343163951}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-491.html', 'title': 'N-491', 'score': 0.9989129947203945}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-835.html', 'title': 'N-835', 'score': 0.998821034516782}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-679.html', 'title': 'N-679', 'score': 0.9987825227518852}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-360.html', 'title': 'N-360', 'score': 0.9980436405636423}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-31.html', 'title': 'N-31', 'score': 0.9974640524639748}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-988.html', 'title': 'N-988', 'score': 0.9974228028300521}]
result = search.search('kiwi fig fig coconut fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #447 checking search results for 'kiwi fig fig coconut fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #447 checking search results for 'kiwi fig fig coconut fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #448 checking search results for 'apricot peach blueberry pear cherry banana fig banana' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-280.html', 'title': 'N-280', 'score': 0.9964363264894994}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-339.html', 'title': 'N-339', 'score': 0.9944104555387755}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 0.9909525548299317}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9903910146882943}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-158.html', 'title': 'N-158', 'score': 0.9902654782933515}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-704.html', 'title': 'N-704', 'score': 0.990070183470958}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-273.html', 'title': 'N-273', 'score': 0.9900464546675798}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-87.html', 'title': 'N-87', 'score': 0.9878898444946025}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-797.html', 'title': 'N-797', 'score': 0.986437429718924}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-873.html', 'title': 'N-873', 'score': 0.9860889515322727}]
result = search.search('apricot peach blueberry pear cherry banana fig banana',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #448 checking search results for 'apricot peach blueberry pear cherry banana fig banana' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #448 checking search results for 'apricot peach blueberry pear cherry banana fig banana' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #449 checking search results for 'cherry papaya cherry orange peach apple' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-675.html', 'title': 'N-675', 'score': 0.9964379608690258}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9937731616001749}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html', 'title': 'N-142', 'score': 0.9930069809434573}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-535.html', 'title': 'N-535', 'score': 0.9925964752493649}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html', 'title': 'N-244', 'score': 0.9919098868037906}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-192.html', 'title': 'N-192', 'score': 0.9918116793909858}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-550.html', 'title': 'N-550', 'score': 0.9902257336966365}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-656.html', 'title': 'N-656', 'score': 0.9898311381166012}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-722.html', 'title': 'N-722', 'score': 0.989806470487584}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-24.html', 'title': 'N-24', 'score': 0.9894817094837689}]
result = search.search('cherry papaya cherry orange peach apple',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #449 checking search results for 'cherry papaya cherry orange peach apple' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #449 checking search results for 'cherry papaya cherry orange peach apple' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #450 checking search results for 'peach coconut banana coconut apple papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-244.html', 'title': 'N-244', 'score': 0.9966252034262781}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-142.html', 'title': 'N-142', 'score': 0.9943873433466469}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-719.html', 'title': 'N-719', 'score': 0.9926458403165438}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html', 'title': 'N-600', 'score': 0.9917083791483845}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-76.html', 'title': 'N-76', 'score': 0.9909121551645227}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-315.html', 'title': 'N-315', 'score': 0.9906510827041206}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-709.html', 'title': 'N-709', 'score': 0.9904041228911619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-132.html', 'title': 'N-132', 'score': 0.9902366021920442}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-84.html', 'title': 'N-84', 'score': 0.9889642086823692}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-176.html', 'title': 'N-176', 'score': 0.988343785260997}]
result = search.search('peach coconut banana coconut apple papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #450 checking search results for 'peach coconut banana coconut apple papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #450 checking search results for 'peach coconut banana coconut apple papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #451 checking search results for 'cherry kiwi peach coconut banana peach blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.991460816317265}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9907861607198478}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-156.html', 'title': 'N-156', 'score': 0.9902342196679942}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-370.html', 'title': 'N-370', 'score': 0.9895329014688393}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-335.html', 'title': 'N-335', 'score': 0.9892273535381078}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-482.html', 'title': 'N-482', 'score': 0.9881254067133131}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-567.html', 'title': 'N-567', 'score': 0.9880098402855801}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-743.html', 'title': 'N-743', 'score': 0.9877739698962479}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 0.9877738209871567}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-284.html', 'title': 'N-284', 'score': 0.9875001761348942}]
result = search.search('cherry kiwi peach coconut banana peach blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #451 checking search results for 'cherry kiwi peach coconut banana peach blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #451 checking search results for 'cherry kiwi peach coconut banana peach blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #452 checking search results for 'peach cherry apple tomato papaya tomato apricot fig' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9962748212833306}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-767.html', 'title': 'N-767', 'score': 0.9954567024079425}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html', 'title': 'N-213', 'score': 0.9943509340951394}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-648.html', 'title': 'N-648', 'score': 0.9936318773536533}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-937.html', 'title': 'N-937', 'score': 0.9935652616194133}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-661.html', 'title': 'N-661', 'score': 0.9929468848695401}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-836.html', 'title': 'N-836', 'score': 0.9925917598742513}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-297.html', 'title': 'N-297', 'score': 0.9925075693202866}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-270.html', 'title': 'N-270', 'score': 0.9919960249422302}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-917.html', 'title': 'N-917', 'score': 0.9910826766459445}]
result = search.search('peach cherry apple tomato papaya tomato apricot fig',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #452 checking search results for 'peach cherry apple tomato papaya tomato apricot fig' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #452 checking search results for 'peach cherry apple tomato papaya tomato apricot fig' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #453 checking search results for 'peach pear peach tomato coconut fig fig lime' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-682.html', 'title': 'N-682', 'score': 0.9948823972784473}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-875.html', 'title': 'N-875', 'score': 0.9942759837833949}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'title': 'N-174', 'score': 0.9934688016112903}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-80.html', 'title': 'N-80', 'score': 0.9922688125329041}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-155.html', 'title': 'N-155', 'score': 0.9919851832301716}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-743.html', 'title': 'N-743', 'score': 0.9918558133535622}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-138.html', 'title': 'N-138', 'score': 0.9915714797285176}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-248.html', 'title': 'N-248', 'score': 0.9914807277137223}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-285.html', 'title': 'N-285', 'score': 0.9892902083782914}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-407.html', 'title': 'N-407', 'score': 0.9885195751769531}]
result = search.search('peach pear peach tomato coconut fig fig lime',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #453 checking search results for 'peach pear peach tomato coconut fig fig lime' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #453 checking search results for 'peach pear peach tomato coconut fig fig lime' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #454 checking search results for 'orange pear fig lime papaya' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-908.html', 'title': 'N-908', 'score': 1.0000000000000002}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-755.html', 'title': 'N-755', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-793.html', 'title': 'N-793', 'score': 1.0}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-927.html', 'title': 'N-927', 'score': 0.9977806933991348}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-394.html', 'title': 'N-394', 'score': 0.9972820831578172}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-329.html', 'title': 'N-329', 'score': 0.9972023015780593}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-798.html', 'title': 'N-798', 'score': 0.9971333967835768}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-571.html', 'title': 'N-571', 'score': 0.9968366682517054}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-213.html', 'title': 'N-213', 'score': 0.9962249794057955}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-16.html', 'title': 'N-16', 'score': 0.9957727644912012}]
result = search.search('orange pear fig lime papaya',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #454 checking search results for 'orange pear fig lime papaya' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #454 checking search results for 'orange pear fig lime papaya' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #455 checking search results for 'papaya cherry peach blueberry apricot orange coconut peach' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-576.html', 'title': 'N-576', 'score': 0.9920166002517444}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-853.html', 'title': 'N-853', 'score': 0.989225586190117}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-465.html', 'title': 'N-465', 'score': 0.9885452459252508}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-141.html', 'title': 'N-141', 'score': 0.9885243190600037}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-428.html', 'title': 'N-428', 'score': 0.9883858552290166}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-966.html', 'title': 'N-966', 'score': 0.9864216914183488}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-606.html', 'title': 'N-606', 'score': 0.9858396703426662}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'title': 'N-174', 'score': 0.9853019163401414}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-254.html', 'title': 'N-254', 'score': 0.9848709429520313}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-852.html', 'title': 'N-852', 'score': 0.9845586580983682}]
result = search.search('papaya cherry peach blueberry apricot orange coconut peach',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #455 checking search results for 'papaya cherry peach blueberry apricot orange coconut peach' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #455 checking search results for 'papaya cherry peach blueberry apricot orange coconut peach' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #456 checking search results for 'orange peach fig apricot fig papaya lime cherry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 0.9998969563148198}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-674.html', 'title': 'N-674', 'score': 0.9961805954676936}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html', 'title': 'N-952', 'score': 0.9941509982841379}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-262.html', 'title': 'N-262', 'score': 0.9920923479901677}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-139.html', 'title': 'N-139', 'score': 0.9897154201281874}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-55.html', 'title': 'N-55', 'score': 0.9887241775991487}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html', 'title': 'N-879', 'score': 0.9880411210881005}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-637.html', 'title': 'N-637', 'score': 0.9866435715516347}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-969.html', 'title': 'N-969', 'score': 0.9853680690622476}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-996.html', 'title': 'N-996', 'score': 0.98519356332515}]
result = search.search('orange peach fig apricot fig papaya lime cherry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #456 checking search results for 'orange peach fig apricot fig papaya lime cherry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #456 checking search results for 'orange peach fig apricot fig papaya lime cherry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #457 checking search results for 'lime cherry blueberry coconut blueberry' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-18.html', 'title': 'N-18', 'score': 0.9998096234655341}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-54.html', 'title': 'N-54', 'score': 0.9997245261468459}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-354.html', 'title': 'N-354', 'score': 0.9997007209486851}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-413.html', 'title': 'N-413', 'score': 0.9996587740734859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-810.html', 'title': 'N-810', 'score': 0.9996587740734859}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-90.html', 'title': 'N-90', 'score': 0.9996231599458522}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-113.html', 'title': 'N-113', 'score': 0.9991519032104016}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-879.html', 'title': 'N-879', 'score': 0.9988865361173169}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-739.html', 'title': 'N-739', 'score': 0.9985463178416099}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-124.html', 'title': 'N-124', 'score': 0.998242195785155}]
result = search.search('lime cherry blueberry coconut blueberry',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #457 checking search results for 'lime cherry blueberry coconut blueberry' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #457 checking search results for 'lime cherry blueberry coconut blueberry' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #458 checking search results for 'banana kiwi lime orange tomato peach cherry orange' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-976.html', 'title': 'N-976', 'score': 0.9969395378953595}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-37.html', 'title': 'N-37', 'score': 0.9928316170528281}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-621.html', 'title': 'N-621', 'score': 0.9909660476344919}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-234.html', 'title': 'N-234', 'score': 0.990866829298511}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-25.html', 'title': 'N-25', 'score': 0.9902107537733619}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-890.html', 'title': 'N-890', 'score': 0.9898030791952577}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-94.html', 'title': 'N-94', 'score': 0.9877063172206237}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-672.html', 'title': 'N-672', 'score': 0.9867931936237103}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-327.html', 'title': 'N-327', 'score': 0.986690723437222}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-818.html', 'title': 'N-818', 'score': 0.9852100883619769}]
result = search.search('banana kiwi lime orange tomato peach cherry orange',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #458 checking search results for 'banana kiwi lime orange tomato peach cherry orange' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #458 checking search results for 'banana kiwi lime orange tomato peach cherry orange' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #459 checking search results for 'fig kiwi cherry fig kiwi apricot' and boost = False
expected = [{'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-641.html', 'title': 'N-641', 'score': 0.9998517491895944}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-945.html', 'title': 'N-945', 'score': 0.9997947434537517}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-758.html', 'title': 'N-758', 'score': 0.9993685692269824}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-600.html', 'title': 'N-600', 'score': 0.9973525079778351}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-49.html', 'title': 'N-49', 'score': 0.9962397635477696}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-996.html', 'title': 'N-996', 'score': 0.995968921562687}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-174.html', 'title': 'N-174', 'score': 0.9957816340559764}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-577.html', 'title': 'N-577', 'score': 0.9956231871669138}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-952.html', 'title': 'N-952', 'score': 0.9953671423084602}, {'url': 'http://people.scs.carleton.ca/~davidmckenney/fruits5/N-654.html', 'title': 'N-654', 'score': 0.9948291823281534}]
result = search.search('fig kiwi cherry fig kiwi apricot',False)
if not testingtools.compare_search_results(expected, result):
  output.write("Failed Test #459 checking search results for 'fig kiwi cherry fig kiwi apricot' and boost = False\n\n")
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write("Passed Test #459 checking search results for 'fig kiwi cherry fig kiwi apricot' and boost = False\n\n")
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()







output.close()
success_output.close()
