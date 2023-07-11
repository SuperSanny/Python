# Write a Python program to do the following operations: Library: NumPy
# a) Dot and matrix product of two arrays
# b) Compute the Eigen values of a matrix
# c) Solve a linear matrix equation such as 3 * x0 + x1 = 9, x0 + 2 * x1 = 8
# d) Compute the multiplicative inverse of a matrix
# e) Compute the rank of a matrix
# f) Compute the determinant of an array

# a) Dot and matrix product of two arrays

import numpy as np

# Dot product of two array

a = np.array([1, 7, 8, 9])
b = np.array([2, 3, 4, 6])
print("Dot Product : ", np.dot(a, b))

# Matrix element multiplication

a = np.array([[1, 2], [7, 9]])
b = np.array([[3, 7], [8, 2]])
print("Elements Multiplication of matrix : \n", np.multiply(a, b))

# Matrix multiplication

print("Multiplication of matrix : \n", np.matmul(a, b))

# b) Compute the Eigen values of a matrix

# Eigen value of Matrix

a = np.array([[2, -3, 0], [2, -5, 0], [0, 0, 3]])
eigenValues,eigenVectors = np.linalg.eig(a)
print("Eigen Values : ", eigenValues, "\nEigen Vectors : \n", eigenVectors)


# c) Solve a linear matrix equation such as 3 * x0 + x1 = 9, x0 + 2 * x1 = 8

# Linear matrix equation

a = np.array([[3, 1], [1, 2]])
b = np.array([[9], [8]])
a_inv = np.linalg.inv(a)
e = np.matmul(a_inv,b)
print("Linear Equation : \n",e)

# d) Compute the multiplicative inverse of a matrix

# Inverse of Matrix

a = np.array([[5, 6], [-1, 2]])
print("Inverse of Matrix :\n",np.linalg.inv(a))

# e) Compute the rank of a matrix

a = np.array([[1, 2, 3], [2, 1, 4], [3, 0, 5]])
b = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
print("Rank of Matrix : ",np.linalg.matrix_rank(a))
print("Rank of Matrix : ",np.linalg.matrix_rank(b))

# f) Compute the determinant of an array

a = np.array([[-1, 1, 2], [3, -1, 1], [-1, 3, 4]])
print("Determinant of Matrix : ",round(np.linalg.det(a)))
print("Rank of Matrix : ",np.linalg.matrix_rank(a))
print("Inverse of Matrix :\n",np.linalg.inv(a))


