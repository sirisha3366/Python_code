# python code demonstrate creating
#dataframe from dict array/lists
#by default address
import pandas as pd
data = {'Name':['Tom', 'nick', 'krish', 'jack'], 'Age':[20,21,19,18]}
df = pd.DataFrame(data)
print(df)