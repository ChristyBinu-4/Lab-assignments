#Question 2: Print Rank of a matrix
import numpy as np

order = 3

print("Enter elements in matrix : ")
matrix = [[int(input("=>")) for j in range(order)] for i in range(order)]
matrix = np.array(matrix)

print("Matrix : ", matrix, sep='\n')

rank = np.linalg.matrix_rank(matrix)
print("Rank of matrix is : ", rank)