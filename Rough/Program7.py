# 7.Perform preprocessing for a country dataset.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.distributions import displot

ds = pd.read_csv("countries of the world.csv")

print("\nDisplay five rows\n")
print(ds.head())

print("\nDisplay the shape of dataset\n")
print(ds.shape)

print("\nDisplay total null values from columns\n")
print(ds.isnull().sum())

print("\nAnalyse the distribution of data in birthrate\n")
fig, ax = plt.subplots(figsize=(8, 8))
sns.displot(ds.Birthrate)
plt.show()

print("\nReplace the missing values with the median value\n")
ds["Birthrate"].fillna(ds['Birthrate'].median(), inplace=True)
print(ds.isnull().sum())

print("\nAgain analyse the distribution of data in birthrate")
fig, ax = plt.subplots(figsize=(8, 8))
sns.displot(ds.Birthrate)
plt.show()

print("\nFilling missing values with mean\n")
ds['Birthrate'].fillna(ds['Birthrate'].mode(), inplace=True)
fig, ax = plt.subplots(figsize=(8, 8))
sns.displot(ds.Birthrate)
plt.show()

print("\nFilling missing values with mode\n")
ds['Birthrate'].fillna(ds['Birthrate'].mode(), inplace=True)
fig, ax = plt.subplots(figsize=(8, 8))
sns.displot(ds.Birthrate)
plt.show()