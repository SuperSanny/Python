n = int(input("Enter size of array :"))
a = []

for i in range(0, n):
    a.append(int(input()))

large = a[0]
for i in range(0, n):
    if a[i] > large:
        large = a[i]

print("Largest Element is :", large)