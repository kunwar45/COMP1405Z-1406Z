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
	if (len(a[0]) != len(b)):
		return None

	resultMatrix = []

	for i in range(len(a)):
		row = []
		for j in range(len(b[0])):
			row.append(0)
		resultMatrix.append(row)

	for i in range(len(a)):
		for j in range(len(b[0])):
			for k in range(len(b)):
				resultMatrix[i][j] += a[i][k] * b[k][j]

	return resultMatrix
	
def euclidean_dist(a,b):
	sum = 0

	for i in range (len(a[0])):
		sum += ((a[0][i] - b[0][i]) ** 2)
	return math.sqrt(sum)
