from pandas import read_csv
from pandasql import sqldf
import matplotlib.pyplot as plt

# Demos running SQL queries on a CSV file
'''
Reads in two CSV files:
    1. 2018 NFL Statistics
    2. 2019 NFL Statistics
These stats seperate touchdowns into three categories: Rushing, Passing, and Receiving.

First, I loop through each CSV to aggregate the total TDs for each player and create a
new column in the dataframe to store those amounts. I then run an SQL query to list 
players with a combined total of 40 or more TDs across the two seasons in highest to 
lowest order.

'''

twenty18 = read_csv("2018.csv")
twenty19 = read_csv("2019.csv")

for i in range(0, len(twenty18.index), 1):
    totalTDs = twenty18['RushingTD'] + twenty18['PassingTD'] + twenty18['ReceivingTD']
    twenty18['TotalTD'] = totalTDs

for i in range(0, len(twenty19.index), 1):
    totalTDs = twenty19['RushingTD'] + twenty19['PassingTD'] + twenty19['ReceivingTD']
    twenty19['TotalTD'] = totalTDs

print(sqldf("""
            SELECT twenty18.Player AS Player, twenty18.Pos AS Positon, 
            twenty18.TotalTD AS "2018 TDs", twenty19.TotalTD AS "2019 TDs"
            FROM twenty18
            JOIN twenty19
            ON twenty18.Player = twenty19.player
            WHERE (twenty19.TotalTD + twenty18.TotalTD) >= 40
            ORDER BY twenty19.TotalTD + twenty18.TotalTD DESC;
            """))