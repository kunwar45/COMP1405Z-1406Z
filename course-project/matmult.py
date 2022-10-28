import math

def mult_scalar(matrix, scale):
	resultMatrix = []

	for i in range(len(matrix)):
		row = []
		for j in range(len(matrix[0])):
			row.append(0)
		resultMatrix.append(row)

	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			resultMatrix[i][j] = matrix[i][j] * scale
	return resultMatrix

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
	sum = 0

	for i in range (len(a[0])):
		sum += ((a[0][i] - b[0][i]) ** 2)
	return math.sqrt(sum)
