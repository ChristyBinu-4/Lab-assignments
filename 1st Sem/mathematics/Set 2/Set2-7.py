# Question 7:Find vector matrix multiplication 
import numpy as np
from time import sleep

def MatrixMaker(rows, columns):
  a = [int(input("=>")) for i in range(rows * columns)]
  a = np.array(a)
  a = a.reshape(rows, columns)
  return a

rows = int(input("Enter the number of rows in Matrix : "))
columns = int(input("Enter the number of columns in Matrix : "))

if rows > 3 or columns > 3 :
  sleep(2)
  print("Vectors can only have maximum elements of 3")
  sleep(2)
  print("Please rerun the program")
  exit()

column_2 = 1 #defining the columns in a vector space

print(f"Enter the elements of the {rows} x {columns} matrix: ")
matrix_1 = MatrixMaker(rows, columns)

print(f"Enter the elements of the Vector: ")
matrix_2 = MatrixMaker(columns, column_2)

print("Matrix \n",matrix_1)
print("Vector \n", matrix_2)

result = []

for i in range(rows):
    sum = 0
    column_2 -= 1 # for adjusting into the index of matrix
    for k in range(columns):
        sum += matrix_1[i][k] * matrix_2[k][column_2]
    result.append(sum)
result = np.array(result)
result = result.reshape(rows, column_2)

print("Resultant matrix after multiplication is:\n", result)