#Question 14: Print the determinant of the matrix
import numpy as np
from math import sqrt

def determinant2D(matrix):
  determinant = 0
  diagonal1 = 1 
  diagonal2 = 1
  for i in range(2):
    for j in range(2):
      if i == j :
        diagonal1 *= matrix[i][j]
      else :
        diagonal2 *= matrix[i][j]

  determinant = diagonal1 - diagonal2
  return determinant

def determinantOfMatrix(matrix, dimension):
  if(dimension < 3):
    determinant = determinant2D(matrix)
  else:
    determinant = 0
    for k in range(len(matrix[0])):
      array = []
      for i in range(dimension):
        for j in range(dimension):
            if i == 0 or j == k:
              continue
            else :
              array.append(matrix[i][j])
      array = np.array(array)
      dimension2 = int(sqrt(len(array)))
      array = array.reshape(dimension2, dimension2)
      if k % 2 == 0 :
        determinant += matrix[0][k] * determinantOfMatrix(array, dimension2)
      else :
        determinant -= matrix[0][k] * determinantOfMatrix(array, dimension2)
  return determinant

dimension = int(input("Enter the no.of rows or columns in Matrix : "))
print('Enter the values of matrix')
matrix = [int(input()) for i in range(dimension**2)]
matrix = np.array(matrix)
matrix = matrix.reshape(dimension, dimension)

print("Elements of matrix:\n",matrix)
print("determinant of matrix:\n",determinantOfMatrix(matrix, dimension))