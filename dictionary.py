my_dict = {
    1: "One",
    2: "Two",
    3: "Three",
    "Name": "Sanny Kumar",
    "Age": "23"
}
print(my_dict)
print(my_dict[1])
print((my_dict.get('Age')))
print(my_dict['Name'])

my_dict['Age'] = 24
print(my_dict['Age'])

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
print(squares.pop(4))
print(squares)

print(squares.popitem())
print(squares)

squares.clear()
print(squares)

