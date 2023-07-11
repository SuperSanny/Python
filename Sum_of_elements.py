arr = [1, 3, 5, 7, 6, 4, 6]
sum = 0
for i in range(0, len(arr)):
    sum = sum + arr[i]

print("Sum of array elements : ", sum)

arr1 = []
sum1 = 0
n = int(input("Enter no. of elements : "))
print("Enter ", n, " elements : ")
for i in range(0, n):
    arr1.append(int(input()))

for i in range(0, n):
    sum1 = sum1 + arr1[i]

print("Sum of array elements : ", sum1)
