#Question2:Add two matrices

import numpy as np
rows = int(input("Enter the number of rows in  Matrices : "))
columns = int(input("Enter the number of columns in Matrices : "))

print(f"Enter the elements of the first {rows}x{columns} matrix")
matrix_1 = [[int(input("=>")) for j in range(columns)] for i in range(rows)]

print(f"Enter the elements of the second {rows}x{columns} matrix")
matrix_2 = [[int(input("=>")) for j in range(columns)] for i in range(rows)]

matrix_1 = np.array(matrix_1)
matrix_2 = np.array(matrix_2)

print("first Matrix \n",matrix_1)
print("Second Matrix \n", matrix_2)
print("Sum of Matrices\n",matrix_1 + matrix_2)