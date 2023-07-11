# 4.Perform the following operations for the given CSV file.
# a) Display the column names
# b) Display the CSV file
# c) Display the maximum of 5 columns
# d) Display the columns as rows and rows as columns

import pandas as pd

ds = pd.read_csv("Datasheet.csv")

print("\nDisplay all Data\n")
print(ds)

print("\nDisplay the column names\n")
print(ds.columns)

print("\nDisplay the CSV file\n")
print(ds)

print("\nDisplay the maximum of 2 columns\n")
print(ds[['Name', 'Age']].max())

print("\nDisplay the columns as rows and rows as columns\n")
print(ds.transpose())
