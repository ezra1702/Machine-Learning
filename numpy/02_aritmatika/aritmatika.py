import numpy as np

a = np.arange(1, 10, 2)
b = np.arange(10, 1, -2)
print("\t====== Array a dan b untuk operasi aritmatika: =====")
print(f"Array a: {a}")
print(f"Array b: {b}")

print("\nOperasi Aritmatika:")
c = a + b
print(f"Penjumlahan a + b: {c}")
d = a - b
print(f"Pengurangan a - b: {d}")
e = a * b
print(f"Perkalian a * b: {e}")
f = a / b
print(f"Pembagian a / b: {f}")
g = a % b
print(f"Sisa bagi a % b: {g}")
h = a ** 2
print(f"Pangkat a ** 2: {h}")
i = a // 2
print(f"Pembagian floor a // 2: {i}")