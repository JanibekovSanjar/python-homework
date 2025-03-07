import numpy as np

random_array = np.random.random((10, 10))
min_value = random_array.min()
max_value = random_array.max()

print("Random Array:\n", random_array)
print("Minimum Value:", min_value)
print("Maximum Value:", max_value)