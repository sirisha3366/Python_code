import pandas as pd
data = pd.read_csv("nba.csv",index_col ="Name")
first = data[["Age", "College", "Salary"]]
print(first)