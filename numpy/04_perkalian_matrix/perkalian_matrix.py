import numpy as np
import random

matrix_a = np.array([[random.randint(1, 3) for _ in range(2)] for _ in range(2)])
matrix_b = np.array([[random.randint(1, 3) for _ in range(2)] for _ in range(2)])
print(matrix_a)
print(matrix_b)

# Melakukan perkalian matrix
c1 = matrix_a.dot(matrix_b)

c2 = np.dot(matrix_a, matrix_b)

is_equal = np.array_equal(c1, c2)
print(f"\nHasil perkalian matrix a dan b (metode 1):\n{c1}")
print(f"\nHasil perkalian matrix a dan b (metode 2):\n{c2}")
print(f"\nApakah kedua metode menghasilkan array yang sama? {is_equal}")



