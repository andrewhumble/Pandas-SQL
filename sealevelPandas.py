import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt
import numpy as np

# Demos a linear regression plot

df = pd.read_csv("Source 2 Filtering - Valid Rows Only.csv")
d = np.polyfit(df['VLM'],df['Trend mm/yr'],1)
f = np.poly1d(d)
df.insert(6,'Treg', f(df['VLM']))
ax = df.plot(y='Trend mm/yr', x='VLM', kind = 'scatter')
df.plot(x='VLM', y='Treg', color='Red', legend=False, ax=ax)
plt.show()