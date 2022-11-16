import pandas as pd
df = pd.read_csv('online_retail.csv')
df.head() 
print(df)
df['LinePrice'] = df['Quantity'] * df['UnitPrice']
df.head()
print(df)