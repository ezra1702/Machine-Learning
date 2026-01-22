import numpy as np


a = np.array([1,2,3])
b = np.array([4,5,6])

aMat = np.zeros((2,3))
bMat = np.ones((2,3))

# stacking matrix, menumpuk matrix

c = np.hstack((a,b))
d = np.vstack((a,b))

cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat))
print("Array a:", a)
print("Array b:", b)
print("\nHasil Horizontal Stacking (a dan b):", c)
print("Hasil Vertical Stacking (a dan b):\n", d)

print("\nArray aMat:", aMat)