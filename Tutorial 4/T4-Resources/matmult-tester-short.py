import matmult



def check_equality(a, b):
  if len(a) != len(b):
    return False
  for row in range(len(a)):
    if len(a[row]) != len(b[row]):
      return False
    for col in range(len(a[row])):
      if a[row][col] != b[row][col]:
        return False
  return True



a = [[4, 1, 1, 9, 1, 10, 10, 7], [9, 10, 8, 10, 4, 3, 0, 3], [5, 10, 5, 6, 5, 4, 1, 0], [10, 3, 10, 0, 5, 2, 9, 3], [3, 6, 10, 10, 5, 5, 5, 5], [6, 7, 6, 7, 9, 5, 8, 8], [4, 2, 9, 0, 1, 3, 1, 6], [10, 7, 3, 6, 0, 9, 0, 6], [3, 3, 6, 6, 4, 10, 5, 6], [9, 10, 9, 10, 7, 2, 10, 10]]
scalar = 9
expected = [[36, 9, 9, 81, 9, 90, 90, 63], [81, 90, 72, 90, 36, 27, 0, 27], [45, 90, 45, 54, 45, 36, 9, 0], [90, 27, 90, 0, 45, 18, 81, 27], [27, 54, 90, 90, 45, 45, 45, 45], [54, 63, 54, 63, 81, 45, 72, 72], [36, 18, 81, 0, 9, 27, 9, 54], [90, 63, 27, 54, 0, 81, 0, 54], [27, 27, 54, 54, 36, 90, 45, 54], [81, 90, 81, 90, 63, 18, 90, 90]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #0 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



a = [[6, 3, 10, 8, 9], [6, 7, 10, 7, 9], [9, 7, 7, 3, 1], [6, 0, 8, 1, 1], [3, 9, 5, 1, 4], [4, 0, 5, 6, 0], [7, 6, 8, 9, 5], [0, 1, 7, 1, 2], [1, 8, 9, 1, 9]]
scalar = 4
expected = [[24, 12, 40, 32, 36], [24, 28, 40, 28, 36], [36, 28, 28, 12, 4], [24, 0, 32, 4, 4], [12, 36, 20, 4, 16], [16, 0, 20, 24, 0], [28, 24, 32, 36, 20], [0, 4, 28, 4, 8], [4, 32, 36, 4, 36]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #1 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



a = [[1, 7], [4, 9], [2, 4], [0, 1], [3, 3], [5, 2]]
scalar = 8
expected = [[8, 56], [32, 72], [16, 32], [0, 8], [24, 24], [40, 16]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #2 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



a = [[8, 7, 7, 4, 10, 8, 8, 1], [4, 6, 1, 7, 10, 8, 8, 5], [4, 4, 9, 2, 1, 10, 1, 9], [2, 3, 7, 8, 6, 3, 0, 2], [1, 7, 2, 2, 1, 5, 4, 7], [2, 9, 6, 9, 7, 2, 0, 3]]
scalar = 6
expected = [[48, 42, 42, 24, 60, 48, 48, 6], [24, 36, 6, 42, 60, 48, 48, 30], [24, 24, 54, 12, 6, 60, 6, 54], [12, 18, 42, 48, 36, 18, 0, 12], [6, 42, 12, 12, 6, 30, 24, 42], [12, 54, 36, 54, 42, 12, 0, 18]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #3 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



a = [[6, 7], [4, 6], [0, 2], [9, 10], [8, 6], [2, 2], [10, 4], [3, 2], [9, 3], [0, 3]]
scalar = 6
expected = [[36, 42], [24, 36], [0, 12], [54, 60], [48, 36], [12, 12], [60, 24], [18, 12], [54, 18], [0, 18]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #4 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



a = [[8, 0, 1], [7, 8, 4], [10, 0, 1], [4, 4, 9], [1, 5, 0]]
scalar = 3
expected = [[24, 0, 3], [21, 24, 12], [30, 0, 3], [12, 12, 27], [3, 15, 0]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #5 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



a = [[9, 3, 1, 1], [1, 4, 3, 2], [5, 3, 8, 7], [8, 3, 1, 5], [10, 7, 6, 6]]
scalar = 7
expected = [[63, 21, 7, 7], [7, 28, 21, 14], [35, 21, 56, 49], [56, 21, 7, 35], [70, 49, 42, 42]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #6 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



a = [[5]]
scalar = 0
expected = [[0]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #7 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



a = [[3, 0, 3], [2, 8, 10], [4, 5, 2], [10, 3, 7], [10, 8, 9], [9, 7, 7], [4, 4, 2], [10, 9, 5], [5, 9, 0], [1, 4, 2]]
scalar = 3
expected = [[9, 0, 9], [6, 24, 30], [12, 15, 6], [30, 9, 21], [30, 24, 27], [27, 21, 21], [12, 12, 6], [30, 27, 15], [15, 27, 0], [3, 12, 6]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #8 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



a = [[4, 8], [1, 7], [5, 8], [8, 8]]
scalar = 10
expected = [[40, 80], [10, 70], [50, 80], [80, 80]]
result = matmult.mult_scalar(a,scalar)
if not check_equality(expected,result):
  raise Exception('Scalar Case #9 Failed:\n a = ' + str(a) + '\nscalar = ' + str(scalar) + '\n result = ' + str(result))



print('Scalar multiplication tests completed successfully')



a = [[4, 3, 9], [9, 6, 0]]
b = [[7, 1, 5, 2, 3, 1, 5, 10], [4, 9, 3, 10, 6, 10, 10, 8], [2, 2, 0, 9, 7, 5, 0, 1]]
expected = [[58, 49, 29, 119, 93, 79, 50, 73], [87, 63, 63, 78, 63, 69, 105, 138]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #0 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[3, 5, 4, 2, 4, 7], [1, 8, 2, 10, 9, 9], [1, 5, 8, 2, 9, 6]]
b = [[5, 1, 5, 8, 4, 8], [2, 6, 2, 0, 4, 2], [6, 10, 1, 9, 4, 10], [7, 3, 4, 1, 5, 4], [0, 8, 4, 6, 1, 5], [9, 2, 8, 6, 8, 2]]
expected = [[126, 125, 109, 128, 118, 116], [184, 189, 171, 144, 175, 147], [131, 201, 115, 172, 123, 163]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #1 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[3, 4], [3, 6], [0, 9], [9, 9], [4, 8]]
b = [[7, 7, 1, 9, 9, 10, 6], [4, 10, 2, 8, 6, 6, 6]]
expected = [[37, 61, 11, 59, 51, 54, 42], [45, 81, 15, 75, 63, 66, 54], [36, 90, 18, 72, 54, 54, 54], [99, 153, 27, 153, 135, 144, 108], [60, 108, 20, 100, 84, 88, 72]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #2 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[10, 7, 9, 0, 10, 2, 3, 3, 2, 7], [7, 6, 0, 7, 0, 1, 2, 10, 2, 10], [7, 9, 8, 4, 8, 5, 0, 0, 1, 9], [6, 6, 9, 4, 8, 0, 9, 7, 4, 10], [1, 3, 1, 1, 9, 6, 2, 0, 6, 8], [7, 0, 2, 8, 7, 0, 1, 10, 10, 2], [2, 2, 5, 0, 4, 4, 10, 7, 7, 4], [9, 6, 9, 2, 10, 8, 8, 0, 6, 6], [2, 3, 10, 4, 3, 4, 8, 0, 0, 6], [2, 6, 7, 2, 8, 5, 2, 1, 6, 8]]
b = [[9, 5, 2], [1, 7, 8], [5, 2, 10], [6, 2, 2], [10, 10, 5], [7, 6, 7], [9, 10, 8], [2, 0, 6], [5, 8, 8], [3, 9, 9]]
expected = [[320, 338, 351], [196, 223, 265], [283, 321, 338], [354, 390, 434], [227, 296, 261], [276, 233, 251], [264, 290, 332], [420, 439, 432], [243, 247, 297], [260, 320, 343]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #3 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[5, 4, 8, 9, 10]]
b = [[2, 7, 3, 7, 7, 1], [6, 3, 9, 8, 4, 7], [8, 2, 7, 1, 9, 0], [6, 6, 0, 7, 10, 5], [8, 2, 2, 5, 9, 4]]
expected = [[232, 137, 127, 188, 303, 118]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #4 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[0, 6, 0], [1, 7, 6], [2, 6, 10]]
b = [[4], [7], [6]]
expected = [[42], [89], [110]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #5 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[7, 0, 6, 1, 4, 8, 1], [7, 7, 3, 6, 4, 0, 1], [3, 10, 6, 3, 3, 4, 7], [7, 3, 9, 3, 3, 1, 0], [4, 8, 3, 7, 10, 8, 3], [7, 8, 7, 0, 5, 4, 3], [0, 6, 9, 1, 0, 10, 10], [4, 0, 1, 5, 3, 3, 3], [9, 4, 3, 3, 0, 0, 2], [0, 10, 1, 9, 1, 4, 4]]
b = [[5, 6, 5, 6, 5, 3, 5, 7, 6, 6], [8, 1, 8, 5, 1, 2, 3, 4, 4, 8], [2, 1, 8, 1, 4, 6, 8, 9, 7, 0], [7, 10, 6, 7, 6, 7, 9, 7, 9, 2], [8, 0, 4, 6, 4, 1, 0, 10, 3, 2], [3, 5, 8, 6, 6, 3, 1, 8, 6, 8], [3, 8, 9, 9, 9, 1, 0, 0, 10, 5]]
expected = [[113, 106, 178, 136, 138, 93, 100, 214, 163, 121], [174, 120, 176, 155, 115, 100, 134, 186, 167, 123], [185, 140, 268, 200, 166, 108, 124, 198, 230, 177], [125, 89, 169, 111, 110, 108, 144, 201, 159, 86], [252, 169, 281, 251, 197, 132, 139, 300, 248, 201], [174, 101, 234, 170, 142, 99, 119, 226, 192, 163], [133, 155, 296, 196, 198, 113, 109, 192, 256, 180], [99, 114, 121, 123, 111, 68, 76, 126, 133, 79], [110, 107, 137, 116, 97, 76, 108, 127, 138, 102], [177, 153, 214, 180, 132, 106, 123, 154, 195, 152]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #6 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[7, 6], [5, 0], [10, 4], [5, 3]]
b = [[7, 1, 7], [0, 5, 0]]
expected = [[49, 37, 49], [35, 5, 35], [70, 30, 70], [35, 20, 35]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #7 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[5, 6, 7, 3, 3, 10, 0, 0, 6], [2, 0, 8, 9, 5, 3, 4, 0, 5], [0, 6, 2, 0, 2, 6, 0, 5, 2], [10, 8, 0, 1, 5, 0, 8, 4, 5], [10, 4, 10, 9, 0, 3, 10, 0, 10]]
b = [[9, 6, 4, 6, 6, 0, 8, 2], [9, 7, 9, 1, 8, 0, 7, 0], [4, 3, 8, 1, 10, 0, 4, 9], [9, 6, 1, 1, 4, 10, 4, 7], [0, 1, 0, 6, 5, 10, 3, 6], [7, 5, 7, 7, 3, 1, 3, 6], [2, 8, 3, 10, 8, 10, 6, 7], [4, 9, 1, 5, 2, 0, 4, 8], [7, 1, 9, 1, 7, 1, 1, 9]]
expected = [[266, 170, 257, 140, 247, 76, 167, 226], [195, 147, 159, 125, 229, 188, 137, 260], [138, 127, 135, 89, 120, 28, 96, 124], [238, 232, 186, 204, 260, 145, 224, 190], [358, 277, 306, 214, 387, 203, 263, 351]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #8 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[6, 4, 6, 9, 3]]
b = [[3, 10, 8, 5], [8, 7, 1, 6], [7, 7, 5, 7], [6, 0, 6, 7], [4, 3, 6, 6]]
expected = [[158, 139, 154, 177]]
result = matmult.mult_matrix(a,b)
if not check_equality(expected,result):
  raise Exception('Matrix Case #9 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



print('Matrix multiplication tests completed successfully')


a = [[4]]
b = [[1]]
expected = 3.0
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #0 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[10, 4, 10, 1, 1, 0, 8]]
b = [[0, 8, 8, 2, 0, 9, 1]]
expected = 15.874507866387544
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #1 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[7, 6, 5, 4, 0, 7, 4, 5, 4]]
b = [[7, 10, 0, 2, 8, 1, 2, 2, 6]]
expected = 12.727922061357855
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #2 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[5, 2]]
b = [[3, 4]]
expected = 2.8284271247461903
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #3 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[5, 9, 0, 6, 2, 9, 5]]
b = [[9, 2, 8, 3, 0, 5, 6]]
expected = 12.609520212918492
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #4 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[10, 9]]
b = [[1, 6]]
expected = 9.486832980505138
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #5 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[2, 10, 9, 2, 8]]
b = [[9, 4, 7, 1, 7]]
expected = 9.539392014169456
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #6 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[8, 8, 9]]
b = [[5, 4, 6]]
expected = 5.830951894845301
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #7 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[3, 3, 5, 4]]
b = [[2, 6, 7, 3]]
expected = 3.872983346207417
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #8 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



a = [[6, 5, 5]]
b = [[8, 3, 10]]
expected = 5.744562646538029
result = matmult.euclidean_dist(a,b)
if abs(result - expected) > 0.001:
  raise Exception('Euclidean Case #9 Failed:\n a = ' + str(a) + '\nb = ' + str(b) + '\n result = ' + str(result))



print('Euclidean distance tests completed successfully')