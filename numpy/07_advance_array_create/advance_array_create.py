import numpy as np

# Membuat matrix dengan tipe data tertentu
int_matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int32)
print("Integer Matrix:\n", int_matrix)
float_matrix = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.float64)
print("\nFloat Matrix:\n", float_matrix)

# Membuat array dengan menggunakan functon
def kuadrat(baris, kolom)  :
    return kolom     ** 2

custom_array = np.fromfunction(kuadrat, (3, 4), dtype=int) #kuadrat, ukuran matrix, tipe data

print("\nCustom Array:\n", custom_array)


# membuat array atau matrix dengan menggunakan iterable
iterable = (x*x for x in range(6))  # generator expression

iterable_array = np.fromiter(iterable, dtype=int, count=6) # iterable, tipe data, jumlah elemen
print("\nIterable Array:\n", iterable_array)