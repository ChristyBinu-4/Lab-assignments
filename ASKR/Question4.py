import pandas as pd 

df = pd.read_csv("data.csv")
col_array = []

df_copy = df.copy()


for columns in df_copy.columns:
    condition = str(type(df_copy[columns][0]))
    if condition == "<class 'str'>":
        continue
    else:
        df_copy[columns] = (df_copy[columns]-df_copy[columns].min())/(df_copy[columns].max()-df_copy[columns].min())

print(df.to_string(),"\n")
print(df_copy)