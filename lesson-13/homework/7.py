import numpy as np

mat = np.random.random((5, 5))
mean = mat.mean()
std = mat.std()

norm_mat = (mat - mean) / std

print("Random Matrix:\n", mat)
print("Normalized Matrix:\n", norm_mat)