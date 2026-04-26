import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = a + b
print(c)

d = a.dot(b)
print(d)

A = np.matrix([a, b, [7, 8, 9]])
e = np.linalg.det(A)
print(e)
