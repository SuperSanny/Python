import pandas as pd
import matplotlib as mp
import matplotlib.pyplot as pt

df = pd.read_csv(r"G:\temp.csv")


# (A) create line plot

# new_df = df.plot.line()
# mp.pyplot.show()

# (B) plot line graph between two columns

new_df = pd.DataFrame(df)
# new_df[['Day', 'Tempreture']].plot.line()

# (C) create bar plot
# new_df.plot.bar()

# (D) stacked bar
# new_df.plot.bar(stacked=True)

# print(df)


# (E) set the bars hori..
# new_df.plot.barh();



# (F) Generate histogram
# new_df.plot.hist()

# (G) Add stacked hist
# new_df.plot.hist(stacked=True)

# (H) add cumulative frequency hist
# new_df.plot.hist(orientation="horizontal", cumulative=True)

# create boxplot
# df.boxplot()


# new_df.plot.area(stacked=True)
# pt.show()


x = new_df['Windspeed']
x.plot.pie()
pt.show()

y = new_df['Tempreture']
y.plot.pie()
pt.show()
mp.pyplot.show()



