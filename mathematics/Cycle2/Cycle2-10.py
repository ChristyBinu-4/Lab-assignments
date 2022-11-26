# Question 10: Define a 3 x 3 square matrix, Extract the main diagonal as vector.
# Create diagonal matrix from that extracted vector 
import numpy as np

def MatrixMaker(rows, columns):
  a = []

  for i in range(rows*columns):
      a.append(int(input(">")))
  a = np.array(a)
  a = a.reshape(rows, columns)
  return a

rows = 3
columns = 3

print(f"Enter the elements of the first {rows}x{columns} matrix")
matrix_1 = MatrixMaker(rows, columns)

# extracting vector and making diagonal matrix
vector = []
diagonalMatrix = [] 

#extracting vector using loop
for i in range(rows):
  for j in range(columns):
    if i == j : #checking the diagonal element
      vector.append(matrix_1[i][j])
vector = np.array(vector) #converting to vector

#making diagonal matrix using vector
for i in range(rows):
  for j in range(columns):
    if i == j :  diagonalMatrix.append(vector[i])    
    else : diagonalMatrix.append(0)
diagonalMatrix = np.array(diagonalMatrix)
diagonalMatrix = diagonalMatrix.reshape(rows, columns)

#printing all values
print("Matrix \n", matrix_1)
print("Vector \n",vector)
print("Diagonal Matrix \n",diagonalMatrix)