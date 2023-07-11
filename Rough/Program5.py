# 5.Perform slicing on the given CSV file.
# a) Slice the index 0 to 7
# b) Slice the last 7 records
# c) Slice the first 10 records
# d) Slice by column name
# e) Slice by any 2 column names
# f) List all the column names

import pandas as pd

ds = pd.read_csv('Datasheet.csv')
print(ds)

print("\nSlice the index 0 to 7\n")
print(ds.head(8))

print("\nSlice the last 7 records\n")
print(ds.tail(7))

print("\nSlice the first 10 records\n")
print(ds.head(10))

print("\nSlice by column name\n")
print(ds[["Age"]])

print("\nSlice by any 2 column names\n")
print(ds[["Name", "Age"]])

print("\nList all the column names\n")
print(ds.columns)