import numpy as np

matrix = np.random.random((5, 5))
row_sums = np.sum(matrix, axis=1)
column_sums = np.sum(matrix, axis=0)

print("5x5 Matrix:\n", matrix)
print("Row-wise Sums:\n", row_sums)
print("Column-wise Sums:\n", column_sums)