#Question 4: Find the hadamard product of two matrices
import numpy as np

def MatrixMaker(rows, columns):
  a = []
  for i in range(rows*columns):
      a.append(int(input(">")))
  a = np.array(a)
  a = a.reshape(rows, columns)
  return a

rows = int(input("Enter the number of rows in  Matrices : "))
columns = int(input("Enter the number of columns in Matrices : "))

print(f"Enter the elements of the first {rows}x{columns} matrix")
matrix_1 = MatrixMaker(rows, columns)

print(f"Enter the elements of the second {rows}x{columns} matrix")
matrix_2 = MatrixMaker(rows, columns)

print("first Matrix \n",matrix_1)
print("Second Matrix \n", matrix_2)

print("Hadamard product of two matrices are:\n", matrix_1 * matrix_2)