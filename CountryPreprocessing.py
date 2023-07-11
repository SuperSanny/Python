import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from seaborn.distributions import distplot

df = pd.read_csv("Countries.csv")

new_df = df.head()
print(new_df)

new_df = df.shape
print(new_df)

new_df = df.isnull().sum()
print(new_df)

#Analyse the distribution of data in birthrate

fig, ax = plt.subplots(figsize = (8, 8))
sns.displot(df.Birthrate)
plt.show()

# Filling missing values with mean

df['Birthrate'].fillna(df['Birthrate'].mean(), inplace = True)

fig,ax = plt.subplots(figsize = (8, 8))
sns.displot(df.Birthrate)
plt.show()

