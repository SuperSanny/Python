# Perform the following operation on a dataset using pandas in python

#     a. Display the whole dataset
#     b. Display the first five rows
#     c. Display any number of rows from the beginning
#     d. Display the last five rows
#     e. Display any number of rows from the last
#     f. Display any set of rows
#     g. Display specific columns based on column name and index
#     h. Display all the rows based on a specific value

import pandas as pd

ds = pd.read_csv("Datasheet.csv")
print("\nDisplay the whole dataset\n")
print(ds)

print("\nDisplay the first five rows\n")
print(ds.head())

print("\nDisplay any number of rows from the beginning\n")
print(ds.head(3))

print("\nDisplay the last five rows\n")
print(ds.tail())

print("\nDisplay any number of rows from the last\n")
print(ds.tail(3))

print("\nDisplay any set of rows\n")
print(ds.loc[3:5])

print("\nDisplay specific columns based on column name and index\n")
print(ds.iloc[:, [0, 3]])

print("\nDisplay all the rows based on a specific value\n")
ds.set_index("Course", inplace=True)
print(ds.loc[["BCA", "MCA"]])
