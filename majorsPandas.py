import pandas as pd
from pandasql import sqldf
import matplotlib.pyplot as plt

# Demos running SQL queries on a CSV file

df = pd.read_csv("degrees-that-pay-back.csv")
df[df.columns[1:]] = df[df.columns[1:]].replace('[\$,]', '', regex=True).astype(float)

print(sqldf("""
            SELECT Undergraduate_Major, Starting_Median_Salary 
            FROM df 
            ORDER BY Starting_Median_Salary DESC;
            """))