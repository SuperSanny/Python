# 3. Implement the duplicate data handling (data-cleaning) using python
# a) Remove duplicates
# b) Print datatypes of all columns
# c) Print datatype of a particular column
# d) Change datatype of temperature into float

import pandas as pd

ds = pd.read_csv("Datasheet.csv")

print(ds)
print("\n Identifying Duplicates\n")
print(ds.duplicated())

print("\nRemove duplicates\n")
print(ds.drop_duplicates())

print("\nPrint datatypes of all columns\n")
print(ds.dtypes)

print("\nPrint datatype of a particular column\n")
print(ds.Course.dtypes)

print("\nChange datatype of temperature into float\n")
print(ds.Age.astype(float).dtypes)
