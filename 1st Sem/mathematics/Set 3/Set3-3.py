#Question 3: Calculate sparsity of matrix
import numpy as np

def sparcity0fMatrix(matrix):

  count = 0
  for row in matrix:
    for element in row :
      if element == 0:
         count += 1

  rows = len(matrix)
  columns = len(matrix[0])
  TotalElements = rows * columns 

  sparcity = count / TotalElements

  return sparcity

rows = int(input("Enter the number of rows : "))
columns = int(input("Enter the number of columns : "))

print("Enter elements in matrix : ")
matrix = [[int(input("=>")) for j in range(columns)] for i in range(rows)]
matrix = np.array(matrix)
print(matrix)

sparcity = sparcity0fMatrix(matrix)
print("\nSparcity of given matrix is : ", sparcity)


if sparcity > 0.5 :
  print("The given Matrix is a sparse matrix")
else :
  print("The given matrix is not sparse matrix")