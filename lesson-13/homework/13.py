import numpy as np

matrix = np.random.random((3, 3))
vector = np.random.random((3, 1))
matrix_vector_product = np.zeros((3, 1))
for i in range(matrix.shape[0]):
    for j in range(vector.shape[0]):
        matrix_vector_product[i] += matrix[i, j] * vector[j]

print("3x3 Matrix:\n", matrix)
print("3-element Column Vector:\n", vector)
print("Matrix-Vector Product:\n", matrix_vector_product)