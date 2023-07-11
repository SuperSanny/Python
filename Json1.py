import json

x = '{"Name":"Sanny Kumar", "Age":23, "City":"Chhapra"}'

y = json.loads(x)

print("Name : ",y["Name"]," Age : ",y["Age"]," City : ",y["City"])

z = json.dumps(x)

print(z)

print(json.dumps({"Name": "Sanny Kumar", "Age": 23}))
print(json.dumps(["Apple", "Orange"]))
print(json.dumps(("Book", "Pen")))
print(json.dumps("Hello World"))
print(json.dumps(41))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))