Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
words = ['cat', 'rat', 'mat']
for w in words:
    print(w,len(w),end=',')

cat 3,rat 3,mat 3,
users = {'name': 'Sanny Kumar', 'Mob.No.': 9523556280, 'Address': 'Garkha'}
users
{'name': 'Sanny Kumar', 'Mob.No.': 9523556280, 'Address': 'Garkha'}
for user,add in users.copy().items():
    if add == 'Garkha':
        print('valid')

        
valid
for user,add in users.copy().items():
    if add == 'Chhapra':
        print('valid')
    else:
        print('Invalid')

        
Invalid
Invalid
Invalid
for user,add in users.copy().items():
    if add == 'Chhapra':
        del users[user]

        
active_user = {}
for user,add in users.item():
    if add == 'Garkha':
        active_user[user] = add

        
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    for user,add in users.item():
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
for user,add in users.items():
    if add == 'Garkha':
        active_user[user] = add

        
active_user
{'Address': 'Garkha'}
for user in users.items():
    print(user)

    
('name', 'Sanny Kumar')
('Mob.No.', 9523556280)
('Address', 'Garkha')
for user in users:
    print(user)

    
name
Mob.No.
Address
for i in range(10):
    print(i)

    
0
1
2
3
4
5
6
7
8
9
list(range(5,10))
[5, 6, 7, 8, 9]
list(range(0,10,2))
[0, 2, 4, 6, 8]
sum(range(5))
10
0+1+2+3+4
10
for n in range(2,10):
    for x in range(2,n):
        if n%x == 0:
            print(n, ' == ', x, '*', n//x)
            break
    else:
        print(n,' is a prime number')

        
2  is a prime number
3  is a prime number
4  ==  2 * 2
5  is a prime number
6  ==  2 * 3
7  is a prime number
8  ==  2 * 4
9  ==  3 * 3
while True:
    pass

Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    while True:
KeyboardInterrupt



def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

        
case 401 | 403 | 404:
    
SyntaxError: invalid syntax
case 401 | 403 | 404:
    
SyntaxError: invalid syntax
