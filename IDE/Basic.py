Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
2 + 2
4
17/5
3.4
17//5
3
5*2
10
5**2
25
5***2
SyntaxError: invalid syntax
width = 100
height = 500
width * height
50000
tax = 12.5/100
price = 100.50
price * tax
12.5625
price +_
113.0625
price +
SyntaxError: invalid syntax
price +_
213.5625
price +_
314.0625
cal = 100
cal +_
414.0625
cal +_
514.0625
round(_,2)
514.06
cal +_
614.06
cal +_
714.06
cal +_
814.06
cal +_
914.06
'spam eggs'
'spam eggs'
'don'\t'
SyntaxError: unexpected character after line continuation character
'don\'t'
"don't"
'"Yes," they said.'
'"Yes," they said.'
print('"Yes." they said.')
"Yes." they said.
s = "Sanny \nKumar'
SyntaxError: unterminated string literal (detected at line 1)
s = 'Sanny\nKumar'
s
'Sanny\nKumar'
print(s)
Sanny
Kumar
print('c:\Sanny\name')
c:\Sanny
ame
print(r'C:\sanny\name')
C:\sanny\name
print("""  Sanny Kumar
Name - Sanny Kumar
""")
  Sanny Kumar
Name - Sanny Kumar

print("""\
Sanny Kumar              My name is sanny kumar.
""")
Sanny Kumar              My name is sanny kumar.

'sa' + 2*'n' + 'y'
'sanny'
'sa' 'nny'
'sanny'
name = 'Sanny'
name + 'Kumar'
'SannyKumar'
name
'Sanny'
name +_
'SannySanny'
name +_
'SannySannySanny'
sanny ++
SyntaxError: invalid syntax
name
'Sanny'
name[0]
'S'
name[2]
'n'
name[-1]
'y'
name[-5]
'S'
name[0:2]
'Sa'
name[2:4]
'nn'
name[:3]
'San'
name[:3]
'San'
name[3:]
'ny'
name[-2:]
'ny'
name[-1:]
'y'
name[:-2]
'San'
name[:2]+name[2:]
'Sanny'
name[2:20]
'nny'
name[20:]
''
name[0] = "J"
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    name[0] = "J"
TypeError: 'str' object does not support item assignment
name[0] = 'J'
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    name[0] = 'J'
TypeError: 'str' object does not support item assignment
name
'Sanny'
'J' + name[1:]
'Janny'
name
'Sanny'
len(name)
5
len('Sanny Kuamr')
11
lists = [1, 5, 7, 8, 9]
lists
[1, 5, 7, 8, 9]
lists[0]
1
list[2:]
list[slice(2, None, None)]
lists[2:]
[7, 8, 9]
lists[-2:]
[8, 9]
lists[:]
[1, 5, 7, 8, 9]
lists + [2, -3, -6, -7]
[1, 5, 7, 8, 9, 2, -3, -6, -7]
5**3
125
lists[1] = 125
lists
[1, 125, 7, 8, 9]
lists.append(215)
lists
[1, 125, 7, 8, 9, 215]
lists.append(5**5)
lists
[1, 125, 7, 8, 9, 215, 3125]
lists
[1, 125, 7, 8, 9, 215, 3125]
lists[:] = []
lists
[]
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
[['a', 'b', 'c'], [1, 2, 3]]
x[0][1]
'b'
x[1][1]
2
a, b = 0, 1
a
0
b
1
while a<10:
    print(a)
    a, b = b, a+b

    
0
1
1
2
3
5
8
a
13
b
21
a
13
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

    
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
