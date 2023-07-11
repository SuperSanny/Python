import numpy as np

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [5, 3, 2, 5]])
b = np.array([[4, 2, 1, 4], [6, 2, 6, 2], [1, 4, 6, 2]])

# Shape of array
print("First Array :\n",a)
print("Shape of First Array : ",a.shape)
print("Dimensions of First Array : ",a.ndim)
print("Size of First Array : ",a.size)
print("No. of Elements in First row : ",a.itemsize)
print(a.data)

print("All Elements Zero :\n",np.zeros((4, 4)))
print("All Elements One :\n",np.ones((4, 4)))
print("Arange Matrix \n",np.arange(10, 30, 2))

print("Create 2d Array : \n", np.arange(12).reshape(3, 4))
print("Create 3d Array : \n", np.arange(18).reshape(3, 2, 3))

print("Slicing Array :\n",a[1:3])
print("Slicing Array by STEP :\n",a[1,1:2:2])
print("View : \n",a.view())