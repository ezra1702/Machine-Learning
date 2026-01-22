import numpy as np

matrix = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9], 
                   [10, 11, 12]])
print("Matrix berukuran {}".format(matrix.shape)) # output: 4 baris, 3 kolom


# Transpose matrix
transprose_matrix = np.transpose(matrix)
print("\nTranspose Matrix:\n{}".format(transprose_matrix))
print("Matrix Transpose berukuran {}".format(transprose_matrix.shape)) # output: 3 baris, 4 kolom


# Reshape matrix 
reshaped_matrix = np.reshape(matrix, (6,2)) # mengubah matrix menjadi 2 baris dan 6 kolom
print("\nReshaped Matrix (2x6):\n{}".format(reshaped_matrix))
print("Matrix Reshape berukuran {}".format(reshaped_matrix.shape)) # output: 2 baris, 6 kolom


# Flatten matrix
flattened_matrix = np.ravel(matrix) # mengubah matrix menjadi 1 dimensi
print("\nFlattened Matrix:\n{}".format(flattened_matrix))
print("Matrix Flatten berukuran {}".format(flattened_matrix.shape)) # output: 12 elemen dalam 1 dimensi

# resize matrix
resized_matrix = np.resize(matrix, (6, 2)) # mengubah ukuran matrix menjadi 5 baris dan 4 kolom
print("\nResized Matrix (5x4):\n{}".format(resized_matrix))
print("Matrix Resized berukuran {}".format(resized_matrix.shape)) # output: 5 baris, 4 kolom