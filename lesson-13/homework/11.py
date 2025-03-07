import numpy as np

matrix1 = np.random.random((4, 4))
transpose_matrix = matrix1.T

print("Original 4x4 Matrix:\n", matrix1)
print("Transposed Matrix:\n", transpose_matrix)
matrix2 = np.random.random((3, 3))
determinant = np.linalg.det(matrix2)

print("3x3 Matrix:\n", matrix2)
print("Determinant of the 3x3 Matrix:", determinant)