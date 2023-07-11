import sklearn
sklearn.__version__

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score

data = pd.read_csv("heart.csv")
print(data.head())

#check if data is balanced

x = data['target']
ax = sns.countplot(x = x, data = data)
plt.show()

#preprocessing

for col in data.columns:
    print(f"{col}:{data[col].isnull().sum()}")

#changing from catogorical to binary

le = LabelEncoder()
data['target'] = le.fit_transform(data['target'])

y = data['target'].values.reshape(-1, 1)

x = data.drop(['target'], axis=1)
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Naive bayes

nb =GaussianNB()
nb.fit(x_train, y_train)
nbpred = nb.predict(x_test)

print("Accuracy : %.2f" %accuracy_score(y_test, nbpred))

cf_matrix_nb = confusion_matrix(y_test, nbpred).astype(int)
sns.heatmap(cf_matrix_nb, fmt = "d", annot = True)
plt.show()

print(classification_report(y_test,nbpred))