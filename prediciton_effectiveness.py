import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt
import numpy as np

# Demos running SQL queries on a CSV file

twenty19 = pd.read_csv("2019.csv")
twenty19Projections = pd.read_csv("2019projections.csv")

for i in range(0, len(twenty19.index), 1):
    diff = (twenty19Projections.Proj - twenty19Projections.Actual)/twenty19Projections.Proj * 100
    twenty19Projections['Diff'] = diff

d = np.polyfit(twenty19Projections['Week'],twenty19Projections['Diff'],1)
f = np.poly1d(d)
twenty19Projections.insert(6,'Treg', f(twenty19Projections['Week']))
ax = twenty19Projections.plot(y='Diff', x='Week', kind = 'scatter')
ax = twenty19Projections.plot(x='Week', y='Treg', color='Red', legend=False, ax=ax)
ax.set_ylabel("% Different")
plt.yticks(np.arange(min(twenty19Projections['Diff']), max(twenty19Projections['Diff'])+1, 50.0))
plt.show()
