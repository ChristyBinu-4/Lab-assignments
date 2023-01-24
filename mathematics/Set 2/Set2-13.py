#Question 13: Print the inverse of a matrix
import numpy as np
from numpy.linalg import inv, det

dimension = int(input("Enter the no.of rows or columns in Matrix : "))
print('Enter the values of matrix')

matrix = [int(input()) for i in range(dimension**2)]
matrix = np.array(matrix)
matrix = matrix.reshape(dimension, dimension)

determinant = det(matrix)

if determinant == 0:
  inverse = 'does not exist'
else:
  inverse = inv(matrix)
print("Matrix : \n", matrix)
print("Inverse of Matrix : \n", inverse)