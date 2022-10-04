from math import sqrt


def mult_scalar(matrix, scale):
	for row in range(len(matrix)):
		for element in range(len(matrix[row])):
			matrix[row][element] = matrix[row][element] * scale
	return matrix

''' [ 1 2 3 ] 	[ 7 8 ]
	[ 4 5 6 ]   [ 9 10 ]
	            [ 11 12 ]
	Step 1:
	Get row 1 of a, get column 1 of b
	Do row 1[0] x column 1 [0]
'''
def mult_matrix(a, b):
	if len(a) != len(b[0]): #if the number of rows in a does not equal the number of columns in b 
		return None
	dotProduct = 0
	newMatrix = []
	for row in range(len(a)):
		newMatrix.append([])
		for column in range(len(b[0])):
			for element in range(len(a[row])):
				dotProduct += a[row][element] * b[element][column]
			newMatrix[row].append(dotProduct)
			dotProduct = 0
	return newMatrix
	
def euclidean_dist(a,b):
	if len(a[0]) != len(b[0]) or len(a) !=1 or len(b) !=1:
		return None 
	#list comprehension, sums up all the squared differences and square roots the sum
	return sqrt(sum([(a[0][i]-b[0][i])**2 for i in range(len(a[0]))])) 

print(mult_matrix([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]]))