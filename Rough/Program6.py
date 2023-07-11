# 6.Perform visualization techniques on the given dataset
# a) Display the dataframe
# b) Create Line plot
# c) Plot line graph between 2 columns
# d) Create Bar plot
# e) Plot stacked bars
# f) Set the bars horizontally
# g) Generate Histogram
# h) Plot stacked histogram
# i) Add a cumulative frequency in the histogram
# j) Create Boxplot
# k) Create unstacked area plot
# l) Create a dataframe with 3 columns and then generate pie chart for each column
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as pt

ds = pd.read_csv("score.csv")

df = pd.DataFrame(ds)

print("\nDisplay the dataframe\n")
print(df)

print("\nCreate Line plot\n")
df.plot()
pt.show()

print("\nPlot line graph between 2 columns")
df[['Hours', 'Scores']].plot.line()
pt.show()

print("\nCreate Bar plot\n")
df.plot.bar()
pt.show()

print("\nPlot Stacked Bars\n")
df.plot.bar(stacked=True)
pt.show()

print("\nSet the bars horizontally\n")
df.plot.barh()
pt.show()

print("\nGenerate Histogram\n")
df.plot.hist()
pt.show()

print("\nPlot stacked histogram\n")
df.plot.hist(stacked=True)
pt.show()

print("\nAdd a cumulative frequency in the histogram\n")
df.plot.hist(orientation="horizontal", cumulative=True)
pt.show()

print("\nCreate Boxplot\n")
df.boxplot()
pt.show()

print("\nCreate unstacked area plot\n")
df.plot.area(stacked=False)

print("\nCreate a dataframe with 3 columns and the generate pie chart for each column\n")
x = df['Hours']
x.plot.pie()
pt.show()

y = df['Scores']
y.plot.pie()
pt.show()