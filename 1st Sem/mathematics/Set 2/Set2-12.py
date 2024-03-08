# Question 12: Find transpose of a matrix
import numpy as np

def MatrixMaker(rows, columns):
  a = [int(input("=>")) for i in range(rows * columns)]
  a = np.array(a)
  a = a.reshape(rows, columns)
  return a

rows = int(input("Enter the number of rows in  Matrix : "))
columns = int(input("Enter the number of columns in Matrix : "))

print(f"Enter the elements of the first {rows}x{columns} matrix")
matrix_1 = MatrixMaker(rows, columns)

transpose = []
for i in range(columns):
    for j in range(rows):
        transpose.append(matrix_1[j][i])
transpose = np.array(transpose)
transpose = transpose.reshape(columns,rows)

print("Matrix :", matrix_1, sep="\n")
print("Transpose of matrix :", transpose, sep="\n")