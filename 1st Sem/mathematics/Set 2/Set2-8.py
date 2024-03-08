# Question 8: Perform scalar - matrix multiplication
import numpy as np

def MatrixMaker(rows, columns):
  a = [int(input("=>")) for i in range(rows * columns)]
  a = np.array(a)
  a = a.reshape(rows, columns)
  return a

rows = int(input("Enter the number of rows in  Matrices : "))
columns = int(input("Enter the number of columns in Matrices : "))

print(f"Enter the elements of the first {rows}x{columns} matrix")
matrix_1 = MatrixMaker(rows, columns)

scalar_value = int(input("Enter any scalar value : "))

print("first matrix \n", matrix_1)
print("Scalar value \n", scalar_value)

print("Resultant matrix is \n",matrix_1 * scalar_value)