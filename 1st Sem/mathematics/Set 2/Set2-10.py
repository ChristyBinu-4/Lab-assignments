# Question 10: Define a 3 x 3 square matrix, Extract the main diagonal as vector.
# Create diagonal matrix from that extracted vector 
import numpy as np

def MatrixMaker(rows, columns):
  a = [int(input("=>")) for i in range(rows * columns)]
  a = np.array(a)
  a = a.reshape(rows, columns)
  return a

rows = 3
columns = 3

print(f"Enter the elements of the {rows}x{columns} matrix")
matrix_1 = MatrixMaker(rows, columns)

# extracting vector and making diagonal matrix
diagonalMatrix = [] 

#extracting vector using loop that  only iterates the diagonal elements 
vector = [matrix_1[i][j] for i, j in zip(range(rows) ,range(columns))]
vector = np.array(vector) #converting to vector

#making diagonal matrix using vector
for i in range(rows):
  for j in range(columns):
    if i == j :  diagonalMatrix.append(vector[i])    
    else : diagonalMatrix.append(0)
#You can use a single line code for making diagonal matrix 
#diagonalMatrix = [matrix[i][j] if i==j else 0  for i, j in  [(i, j) for i in range(rows) for j in range(columns)]]   
diagonalMatrix = np.array(diagonalMatrix)
diagonalMatrix = diagonalMatrix.reshape(rows, columns)

#printing all values
print("Matrix \n", matrix_1)
print("Vector \n",vector)
print("Diagonal Matrix \n",diagonalMatrix)