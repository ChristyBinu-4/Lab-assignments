import pandas as pd

def truthTable(DataColumn):
  categories = [DataColumn[0]]

  lengthOfColumn = len(DataColumn)

  for i in range(1,lengthOfColumn):
    if DataColumn[i] != DataColumn[i-1]:
      categories.append(DataColumn[i])

  return categories

def dataConverter(DataColumn, categories) :

    lengthOfCategories = len(categories)
    lengthofColumn = len(DataColumn)

    for i in range(lengthOfCategories):
      for j in range(lengthofColumn):
        if DataColumn[j] == categories[i]:
          DataColumn[j] = i


    return DataColumn


df = pd.read_csv("Lab-assignments/ASKR/iris.csv")
df_copy = df.copy()


categories = truthTable(df_copy['Species'])
df_copy['Species'] = dataConverter(df_copy['Species'],categories)

print("\non the below dataset : \n")

for (number,item) in enumerate(categories):
  print(number," represents ", item)

print("\n",df_copy.to_string())
