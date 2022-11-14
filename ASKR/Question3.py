import pandas as pd 


columnName = []

df = pd.read_csv("data.csv")
print(df.to_string())

columnName = df.keys()

print("\nmax value of each column :")
for i in columnName:
    print(df[i].max())
print("\nmin value of each column : ")
for i in columnName:
    print(df[i].min())


print("Mean value of each column :",df.mean(),sep="\n")
