# getting data from specific columns
import pandas as pd
data = pd.read_csv(r'C:\pythoncode\Giants.csv')
df = pd.DataFrame(data, columns=['CEO', 'Established'])
print(df)