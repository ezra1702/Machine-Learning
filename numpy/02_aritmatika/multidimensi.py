import numpy as np

multidimensi_a = np.array([[1, 2, 3], [4, 5, 6]])
multidimensi_b = np.array([[7, 8, 9], [10, 11, 12]])
print("\t====== Array multidimensi a dan b untuk operasi aritmatika: =====")
print(f"Array multidimensi a:\n{multidimensi_a}")
print(f"Array multidimensi b:\n{multidimensi_b}")   

print("\nOperasi Aritmatika pada Array Multidimensi:")
c = multidimensi_a + multidimensi_b
print(f"Penjumlahan a + b:\n{c}")
d = multidimensi_a - multidimensi_b
print(f"Pengurangan a - b:\n{d}")       
e = multidimensi_a * multidimensi_b
print(f"Perkalian a * b:\n{e}")
f = multidimensi_a / multidimensi_b
print(f"Pembagian a / b:\n{f}")
g = multidimensi_a % multidimensi_b
print(f"Sisa bagi a % b:\n{g}")
h = multidimensi_a ** 2
print(f"Pangkat a ** 2:\n{h}")
i = multidimensi_a // 2
print(f"Pembagian floor a // 2:\n{i}")