
import pandas as pd
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print(diamonds.head())
print("\n count,minimum,maximum price for each cut of diamonds DataFrame:")
print(diamonds.groupby('cut').price.agg(['count','min','max']))
