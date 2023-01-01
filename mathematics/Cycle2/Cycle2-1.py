#Question 1: Define Matrix 

import numpy as np 

rows = int(input("enter the number of rows in Matrix "))
columns = int(input("enter the number of columns in Matrix "))

print(f"Enter the elements of the {rows}x{columns} matrix")
a = [int(input("=>")) for i in range(rows*columns)]
a = np.array(a)
a = a.reshape(rows, columns)
print (a)




