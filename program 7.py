import pandas as pd
pd.set_option('display.max_rows',50)
pd.set_option('display.max_columns',50)
diamonds = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/diamonds.csv')
print("First 5 rows: ")
print(diamonds.head())
