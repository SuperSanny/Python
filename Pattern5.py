n = 6
for i in range(1, n+1):
	for j in range(0, n-i+1):
		print(end=" ")
	c = 1
	for k in range(1, i+1):
		print(c, end="  ")
		c = c * (i - k) // k
	print("\n")