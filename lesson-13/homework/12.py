import numpy as np
A = np.random.random((3, 4))
B = np.random.random((4, 3))
product_matrix = np.zeros((3, 3))
for i in range(A.shape[0]):
    for j in range(B.shape[1]):
        for k in range(A.shape[1]):
            product_matrix[i, j] += A[i, k] * B[k, j]

print("Matrix A (3x4):\n", A)
print("Matrix B (4x3):\n", B)
print("Matrix Product A · B (3x3):\n", product_matrix)