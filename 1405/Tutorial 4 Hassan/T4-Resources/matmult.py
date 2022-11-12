from math import sqrt

def mult_scalar(matrix, scale):
	for row in range(len(matrix)):
		for element in range(len(matrix[row])):
			matrix[row][element] = matrix[row][element] * scale
	return matrix

def mult_matrix(a, b):
	if (len(a) != len(b[0])) and (len(b) != len(a[0])): #if the number of rows in a does not equal the number of columns in b 
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