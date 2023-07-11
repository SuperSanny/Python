# 2. Implement the missing data handling(data-cleaning) using python
#
#     a. Replace NaN values with zero
#     b. Use dictionary to specify NaN values of a column to same other value
#     c. Carry-forward/Carry-backward method to replace NaN value (forward fill, backward fill)
#     d. Use interpolation technique o replace NaN value
#     e. Drop all the rows containing any NaN value
#     f. Drop only the rows having all the values being NaN

import pandas as pd

ds = pd.read_csv("Datasheet.csv")

print("\nDisplay all Data\n")
print(ds)

print("\nReplace NaN values with zero\n")
print(ds.fillna(0))

print("\nUse dictionary to specify NaN values of a column to same other value\n")
print(ds.fillna({"Age": 24, "Course": "MCA"}))

print("\nCarry-forward/Carry-backward method to replace NaN value (forward fill, backward fill)\n")
print("Carry-forward\n")
print(ds.fillna(method="ffill"))

print("\nCarry-backward\n")
print(ds.fillna(method="bfill"))

print("\nUse interpolation technique o replace NaN value\n")
print(ds.interpolate())

print("\nDrop all the rows containing any NaN value\n")
print(ds.dropna())

print("\nDrop only the rows having all the values being NaN\n")
print(ds.dropna(how="all"))
