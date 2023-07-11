# Python program to Print all Prime Numbers in an interval.

a = int(input("Enter first number : "))
b = int(input("Enter last number : "))
print("All Prime number between ", a, "and", b)
for i in range(a,b):
	if(a%2!=0):
		print(a, end=" ")


