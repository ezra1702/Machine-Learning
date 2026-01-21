import numpy as np

# membuat vector 
a = np.array([1, 2.3, 3.1])
b = np.array([4, 5.2, 6.2])
print(f"====== vector basic ======\n{a}\n{b}\n")

# membuat vectpr dengan arange
vector_arrange = np.arange(0, 10, 3.14)
print(f"====== vector arange ======\n{vector_arrange}\n")

# membuat linspace (linspace itu untuk membuat vektor dengan jarak tertentu)
linspace_arr = np.linspace(0, 10, 3)  # 3 elemen dari 0 sampai 10
print(f"====== vector linspace ======\n{linspace_arr}\n")

# array multidimensi/matrix
matrix_2d_x = np.array([[i for i in range(3)], [4, 5, 6]])
matrix_2d_y = np.array([[1, 2, 3], [4, 5, 6]])
print(f"====== matrix 2d ======\n{matrix_2d_x}\n")
print(f"{matrix_2d_y}\n")

# matriks dengan nilai nol
matrix_zeros = np.zeros((3, 4))
print(f"====== matrix zeros ======\n{matrix_zeros}\n")

# matiriks dengan nilai satu
matrix_ones = np.ones((2, 5))
print(f"====== matrix ones ======\n{matrix_ones}\n")


#matrix identitas
matrix_identity = np.identity(5)
matrix_identity_2 = np.eye(4)
print(f"====== matrix identity ======\n{matrix_identity}\n")
print(f"====== matrix identity (eye) ======\n{matrix_identity_2}\n")



