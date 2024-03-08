# Question 9: Define a 3 x 3 square matrix and Calculate lower and upper triangular matrix from it.
import numpy as np

def MatrixMaker(rows, columns):
  a = [int(input("=>")) for i in range(rows * columns)]
  a = np.array(a)
  a = a.reshape(rows, columns)
  return a

rows = 3
columns = 3

print(f"Enter the elements of the first {rows}x{columns} matrix")
matrix_1 = MatrixMaker(rows, columns)

#upper triangular matrix
upperTriangle = []
upperTriangle = matrix_1.copy()
for i in range(rows):
  for j in range(columns):
    if i > j :
      upperTriangle[i][j] = 0 

#lower triangular matrix
lowerTriangle = []
lowerTriangle = matrix_1.copy()
for i in range(rows):
  for j in range(columns):
    if i < j:
      lowerTriangle[i][j] = 0 

print("Matrix \n", matrix_1)
print("Upper triangular matrix \n",upperTriangle)
print("Lower triangular matrix \n",lowerTriangle)