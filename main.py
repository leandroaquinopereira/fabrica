import pandas as pd
import numpy as np

df_prod = pd.read_excel('files/master.xlsx', engine='openpyxl')
df_branch = pd.read_excel('files/branch.xlsx', engine='openpyxl')

compare_values = df_prod.values == df_branch.values

print(compare_values)