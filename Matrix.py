# create of multidimensional array and find its shape and dimension

import numpy as np

# creation of multidimensional array
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Array : \n", a)
# Shape
b = a.shape
print("Shape : ", b)
# Dimension
c = a.ndim
print("Dimension : ", c)

# Create a matix full with zeros and ones

# Matrix full with zeros
x = np.zeros((2, 2))
print("Zeros :\n", x)

# Matrix full with ones
y = np.ones((2, 2))
print("Ones :\n", y)

# Reshape and flatten data in the array

# Matrix reshape
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [2, 7, 8, 6]])
print("Array :\n", a)
b = a.reshape(2, 4, 2)
print("Reshape Array :\n", b)

# Matrix flatten
c = a.flatten()
print("Flatten :\n", c)

# Append data vertically and horizontally

# Appending data vertically
x1 = np.array([[1, 2], [3, 4]])
y1 = np.array([[5, 6], [7, 8]])
v = np.vstack((x1, y1))
print("Vertically :\n", v)

# Appending data horizontally
x1 = np.array([[1, 2], [3, 4]])
y1 = np.array([[5, 6], [7, 8]])
h = np.hstack((x1, y1))
print("Horizontally :\n", h)

# Apply indexing and slicing on array

# Indexing
a = np.array([[1, 3, 5], [2, 6, 3], [9, 5, 1], [3, 1, 9]])
temp = a[[0, 0, 0], [0, 1, 2]]
print("Indexing :\n", temp)

# Slicing
i = a[:4, ::3]
print("Slicing :\n", i)

# Use statistical functions on array - Min, Max, Mean, Median and Standard Deviation

# Use min for finding minimun value of array

a = np.array([[1, 3, 5], [2, 6, 3], [9, 5, 1], [3, 1, 9]])
m = a.min()
print("Minimum value : ", m)

# Use max for finding maximum value of array

a = np.array([[1, 3, 5], [2, 6, 3], [9, 5, 1], [3, 1, 9]])
m = a.max()
print("Maximum value : ", m)

# Mean

a = np.array([1, 2, 4, 8])
d = a.mean()
print("Mean : ", d)

# Median

a = np.array([1, 2, 4, 8])
d = np.median(a)
print("Median : ", d)

# Standard Deviation

s = a.std()
print("Standard Deviation : ", s)