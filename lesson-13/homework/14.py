import numpy as np

A = np.random.random((3, 3))
b = np.random.random((3, 1))
A_inv = np.linalg.inv(A)

x = np.dot(A_inv, b)

print("Matrix A (3x3):\n", A)
print("Column Vector b (3x1):\n", b)
print("Inverse of Matrix A (3x3):\n", A_inv)
print("Solution Vector x (3x1):\n", x)