def mult_scalar(matrix, scale):
	for row in range(len(matrix)):
		for element in range(len(matrix[row])):
			matrix[row][element] = matrix[row][element] * scale
	return matrix

def mult_matrix(a, b):
	return [[]]
	
def euclidean_dist(a,b):
	return -1