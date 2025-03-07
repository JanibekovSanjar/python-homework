import numpy as np

matrix1 = np.random.random((5, 3))
matrix2 = np.random.random((3, 2))

rmatrix = np.dot(matrix1, matrix2)

print("5x3 Matrix:\n", matrix1)
print("3x2 Matrix:\n", matrix2)
print("Resulting 5x2 Matrix:\n", rmatrix)