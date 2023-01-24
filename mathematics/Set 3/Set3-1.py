#Question 1: Create an orthogonal matrix and check Qtranspose * Q = Q * Qtranspose = Identity Matrix
import numpy as np


def product(matrix_1, matrix_2):
  product = []

  row = len(matrix_1)
  column1 = len(row)
  column2 = len(matrix_2[0])

  for i in range(row):
    for j in range(column2):
      sum = 0
      for k in range(column1):
          sum += matrix_1[i][k] * matrix_2[k][j]
      product.append(sum)

  product = np.array(product)
  product = product.reshape(row, column2)
  
  return product


def transpose(matrix):
  transpose = []

  rows = len(matrix)
  columns = len(rows)

  for i in range(columns):
      for j in range(rows):
          transpose.append(matrix[j][i])

  transpose = np.array(transpose)
  transpose = transpose.reshape(columns,rows)
  return transpose


matrix = np.array([
    [1/3,2/3, -2/3],
    [-2/3,2/3,1/3],
    [2/3,1/3,2/3]])
print("Matrix :", matrix, sep="\n")

transpose = transpose(matrix)
print("Transpose of matrix :", transpose, sep="\n")

