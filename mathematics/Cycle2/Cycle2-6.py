# Question 6 : Find the product of two matrices
import numpy as np

def MatrixMaker(rows, columns):
  a = []
  for i in range(rows):
    for j in range(columns):
      a.append(int(input(">")))
  a = np.array(a)
  a = a.reshape(rows, columns)
  return a

rows = int(input("Enter the number of rows in first Matrix : "))
columns = int(input("Enter the number of columns in first Matrix : "))

column_2 = int(input("Enter the number of columns in Second Matrix : "))

print(f"Enter the elements of the first {rows} x {columns} matrix")
matrix_1 = MatrixMaker(rows, columns)

print(f"Enter the elements of the second {columns} x {column_2} matrix")
matrix_2 = MatrixMaker(columns, column_2)

print("first Matrix \n",matrix_1)
print("Second Matrix \n", matrix_2)

result = []

for i in range(rows):
  for j in range(column_2):
    sum = 0
    for k in range(columns):
        sum += matrix_1[i][k] * matrix_2[k][j]
    result.append(sum)
result = np.array(result)
result = result.reshape(rows, column_2)

print("Resultant matrix after multiplication is:\n", result)