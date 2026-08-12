import numpy as np

x = np.array([2, 3])

W = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

b = np.array([1, 1, 1])

z = W @ x + b

print("Input:", x)
print("Weight matrix:\n", W)
print("Weighted sum:", z)