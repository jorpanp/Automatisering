import pandas as pd

data = pd.read_csv('data.csv')
summary = data.describe()
print(summary)

data.to_excel('summary.xlsx')