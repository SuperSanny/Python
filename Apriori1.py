dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple','Corn','Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Kidney Beans', 'Yogurt'],
           ['Onion', 'Onion', 'Kidney Beans', 'IceCream', 'Eggs','Corn']]

print(dataset)

# Convert to pandas dataframe
import pandas as pd
from mlxtend.preprocessing import TransactionEncoder

te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
print(te_ary)

# dataframe
df = pd.DataFrame(te_ary)
print(df)

# Display Column names

df = pd.DataFrame(te_ary, columns=te.columns_)
print(df)

from mlxtend.frequent_patterns import apriori

frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)
print(frequent_itemsets)

# Genertating association rules

from mlxtend.frequent_patterns import association_rules

rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.8)
print(rules)
