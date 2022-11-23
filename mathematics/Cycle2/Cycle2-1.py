#Question 1: Define Matrix 

import numpy as np 

rows = int(input("enter the number of rows in Matrix "))
columns = int(input("enter the number of columns in Matrix "))

a = []
print(f"Enter the elements of the {rows}x{columns} matrix")
for i in range(rows):
  for j in range(columns):
    a.append(int(input(">")))
a = np.array(a)
a = a.reshape(rows, columns)
print (a)




