import numpy as np


a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

c = a + b
print(c)  # [11 22 33 44]


vectors = np.array(
    [
        [1, 2, 3, 4],
        [10, 20, 30, 40],
        [-1, 0, 5, 2],
    ]
)

s = vectors.sum(axis=0)
print(s)
