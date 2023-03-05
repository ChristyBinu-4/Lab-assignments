#Question 4: Find the hadamard product of two matrices

import numpy as  np

def hadamardProduct(matrix1, matrix2) :
    resultantMatrix = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2)):
            row.append(matrix1[i][j] * matrix2[i][j])
        resultantMatrix.append(row)

    return resultantMatrix
        

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

result = hadamardProduct(matrix_1, matrix_2)
result = np.array(result)
print("Hadamard product of two matrices are:\n", result)