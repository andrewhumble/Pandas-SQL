import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt
import numpy as np

# Demos running SQL queries on a CSV file

df = pd.read_csv("2018.csv")

"""
Filtering Methods:
    1. Filters out QBs
    2. Filters out players older than 30
df = df.set_index("Pos")
df = df.drop("QB", axis=0)
df = df[df.Age > 30]
"""

for i in range(0, len(df.index), 1):
    totalTDs = df["RushingTD"] + df["PassingTD"] + df["ReceivingTD"]
    df["TotalTD"] = totalTDs

d = np.polyfit(df["TotalTD"], df["FantasyPoints"], 1)
f = np.poly1d(d)
df.insert(6, "Treg", f(df["TotalTD"]))
ax = df.plot(y="FantasyPoints", x="TotalTD", kind="scatter")
df.plot(x="TotalTD", y="Treg", color="Red", legend=False, ax=ax)
plt.show()
