import numpy as np
import random

number = np.array([[random.randint(1, 100) for _ in range(5)] for _ in range(5)])
print(number)


# number[x, y] : x = baris, y = kolom

# Mengambil nilai
print("\nMengambil nilai pada array:")
print(f"Nilai pada baris ke-2, kolom ke-3: {number[1, 2]}")
print(f"Nilai pada baris ke-4, kolom ke-5: {number[3, 4]}")

max_value = number[:,2].max()
min_value = number.min()
print(f"\nNilai maksimum pada array: {max_value}")
print(f"Nilai minimum pada array: {min_value}")
# Slicing array
print("\nSlicing array:")
print(f"Baris ke-2: {number[1]}") # Mengambil seluruh elemen pada baris ke-2
print(f"Kolom ke-3: {number[:, 2]}") # Mengambil seluruh elemen pada kolom ke-3
print(f"Baris ke-2 sampai ke-4, kolom ke-3 sampai ke-5: {number[1:4, 2:5]}")

# Iterasi array per baris berurutan 
print("\nIterasi array:")
for x,y in enumerate(number, start=1):
    print(f"Baris ke-{x}: {y}")

# Implementasi iterasi untuk bubble sort
print("\nBubble Sort pada setiap baris array:")
for i in range(number.shape[0]):  # Iterasi untuk setiap baris
    for j in range(number.shape[1]-1):  # Iterasi untuk setiap elemen dalam baris
        for k in range(0, number.shape[1]-j-1):
            if number[i, k] > number[i, k+1]:
                # Tukar jika elemen ditemukan lebih besar
                number[i, k], number[i, k+1] = number[i, k+1], number[i, k]
    print(f"Baris ke-{i+1} setelah diurutkan: {number[i]}")