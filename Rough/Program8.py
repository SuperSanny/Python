dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', ' Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'IceCream', 'Eggs']]

print("\n Display all dataset\n ")
print(dataset)

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()

te_arr = te.fit(dataset).transform(dataset)

print("\nDisplay Data in true false form\n")
print(te_arr)

df = pd.DataFrame(te_arr)
print("\nDisplay DataFrame\n")
print(df)

print("Display values with its columns")
print(pd.DataFrame(te_arr, columns=te.columns_))

from mlxtend.frequent_patterns import apriori
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

print("\n Display Frequent Patterns\n")
print(frequent_itemsets)

from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.8)

print("\n Display association rules\n")
print(rules)

