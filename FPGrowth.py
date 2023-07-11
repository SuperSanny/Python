dataset = [['Milk', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Dill', 'Onion', 'Nutmeg', 'Kidney Beans', 'Eggs', 'Yogurt'],
           ['Milk', 'Apple', 'Kidney Beans', 'Eggs'],
           ['Milk', 'Unicorn', 'Corn', 'Kidney Beans', 'Yogurt'],
           ['Corn', 'Onion', 'Onion', 'Kidney Beans', 'IceCream', 'Eggs']]

import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)

print(te_ary)

#Dataframe

df = pd.DataFrame(te_ary)
print(df)

#Display columns name

df = pd.DataFrame(te_ary,columns=te.columns_)
print(df)

from mlxtend.frequent_patterns import fpgrowth
frequent_itemsets = fpgrowth(df, min_support=0.6, use_colnames=True)

print(frequent_itemsets)

#Generating association rules

from mlxtend.frequent_patterns import association_rules
rules = association_rules(frequent_itemsets,metric="confidence",min_threshold=0.8)
print(rules)