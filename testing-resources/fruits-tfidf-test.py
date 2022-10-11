
import testingtools
import crawler
import searchdata
import search
output = open('fruits-tfidf-failed.txt', 'w')
success_output = open('fruits-tfidf-passed.txt', 'w')

#Performing crawl starting at seed http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html
crawler.crawl('http://people.scs.carleton.ca/~davidmckenney/fruits/N-0.html')
#Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word peach
expected = 0.01507262712743627
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #0 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word banana
expected = 0.026435697651786105
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #1 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word coconut
expected = 0.007642508877644972
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #2 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word apple
expected = 0.014161063490706421
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #3 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word pear
expected = 0.015886562565125537
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #4 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #5 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-128.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word peach
expected = 0.014307045475623087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #6 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word banana
expected = 0.01646917062056189
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #7 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word coconut
expected = 0.016371547269107223
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #8 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word apple
expected = 0.01217813669875404
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #9 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word pear
expected = 0.019443581172158126
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #10 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #11 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-722.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word peach
expected = 0.00982173918215607
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #12 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word banana
expected = 0.01923116078623852
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #13 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word coconut
expected = 0.0215626226256398
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #14 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word apple
expected = 0.012598064527532328
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #15 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word pear
expected = 0.015886562565125537
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #16 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #17 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-871.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word peach
expected = 0.01209643459154539
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #18 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word banana
expected = 0.0031423938279027314
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #19 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word coconut
expected = 0.024443089428098932
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #20 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word apple
expected = 0.013431897262154007
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #21 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word pear
expected = 0.02286107235814336
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #22 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #23 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-444.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word peach
expected = 0.015235713081979433
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #24 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word banana
expected = 0.008718228088337566
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #25 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word coconut
expected = 0.02291213569987703
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #26 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word apple
expected = 0.021898246475129658
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #27 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word pear
expected = 0.00792681277814716
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #28 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #29 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-178.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word peach
expected = 0.014307045475623087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #30 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word banana
expected = 0.01923116078623852
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #31 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word coconut
expected = 0.015491066507565628
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #32 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word apple
expected = 0.010906072415966224
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #33 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word pear
expected = 0.019055451996668523
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #34 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #35 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-226.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word peach
expected = 0.014307045475623087
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #36 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word banana
expected = 0.018465793366799335
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #37 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word coconut
expected = 0.0181055999688694
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #38 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word apple
expected = 0.014974147360882971
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #39 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word pear
expected = 0.013120144314836671
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #40 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #41 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-196.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word peach
expected = 0.01284024581822718
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #42 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word banana
expected = 0.01923116078623852
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #43 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word coconut
expected = 0.013902877591502586
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #44 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word apple
expected = 0.021358710040301147
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #45 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word pear
expected = 0.011756175313239121
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #46 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #47 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-894.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word peach
expected = 0.009753827886802994
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #48 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word banana
expected = 0.013148590639014034
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #49 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word coconut
expected = 0.014864011018402363
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #50 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word apple
expected = 0.01736884373111887
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #51 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word pear
expected = 0.0234504873846046
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #52 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #53 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-629.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word peach
expected = 0.022574842851635843
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #54 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word banana
expected = 0.01923116078623852
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #55 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word coconut
expected = 0.008952022920533313
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #56 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word apple
expected = 0.017485412117501323
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #57 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word pear
expected = 0.009180573341547111
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #58 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #59 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/fruits/N-259.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','peach')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #60 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word peach\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','banana')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #61 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word banana\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','coconut')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #62 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word coconut\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','apple')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #63 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word apple\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','pear')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #64 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word pear\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


#Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato
expected = 0.0
result = searchdata.get_tf_idf('http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html','tomato')
if not testingtools.compare_doubles(expected, result):
  output.write('Failed Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  output.write('expected = {}\n'.format(str(expected)))
  output.write('result = {}\n\n\n'.format(str(result)))
else:
  success_output.write('Passed Test #65 checking TF-IDF for URL http://people.scs.carleton.ca/~davidmckenney/tinyfruits/N.html and word tomato\n\n')
  success_output.write('expected = {}\n'.format(str(expected)))
  success_output.write('result = {}\n\n\n'.format(str(result)))


output.close()
success_output.close()
