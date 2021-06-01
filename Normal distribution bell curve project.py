import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
df = pd.read_csv("mobileData.csv")
read_list = df["Avg Rating"].to_list()
mean = statistics.mean(read_list)
median = statistics.median(read_list)
mode = statistics.mode(read_list)

print("Mean Of this Data is",mean)
print("Median Of this Data is",median)
print("Mode Of this Data is",mode)


fig=ff.create_distplot([df["Avg Rating"].tolist()],["rating"], show_hist=False)
fig.show()

