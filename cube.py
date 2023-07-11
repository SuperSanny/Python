def cube(x):
    z = x * x * x
    return z


print("Enter the number to find cube : ")
n = int(input())
g = cube(n)
print("Cube of ", n, " is ", g)
