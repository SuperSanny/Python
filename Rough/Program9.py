import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import fpgrowth
from mlxtend.frequent_patterns import association_rules

dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', ' Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'IceCream', 'Eggs']]

print("\nDisplay all dataset\n")
print(dataset)

te = TransactionEncoder()
te_arr = te.fit(dataset).transform(dataset)

print("\nDisplay TransactionEncoder Table\n")
print(te_arr);

df = pd.DataFrame(te_arr)
print("\nDisplay DataFrame\n")
print(df)

print("Display values with its columns")
print(pd.DataFrame(te_arr, columns=te.columns_))

frequent_itemsets = fpgrowth(df, min_support=0.6, use_colnames=True)

print("\n Display Frequent Patterns\n")
print(frequent_itemsets)

rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.8)

print("\n Display association rules\n")
print(rules)
