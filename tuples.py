my_tuple = (1, 8.5, 700, "Hello World!", 'S', "78S", [1, 8, 9])
print(my_tuple)
print(my_tuple[4])
print(my_tuple[-1])
print(my_tuple[3][6])
print(my_tuple[-1][-1])
print("Length of tuples", len(my_tuple))

my_tuple1 = 65, 78.01, "Boy", 'A', [7, "Hello"]

print(my_tuple+my_tuple1)

print(my_tuple * 2)

print(50 in my_tuple)
print(65 not in my_tuple1)
print(65 in my_tuple1)

print("Elements in the tuple are : ")
for i in my_tuple1:
    print(i)