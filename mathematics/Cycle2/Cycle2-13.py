import numpy as np
from numpy.linalg import det 
from math import sqrt


matrix = [2, 3, 5, 1, 7, 8, 9, 7, 2]
matrix = np.array(matrix)
row = int(sqrt(len(matrix)))
matrix = matrix.reshape(row, row)
print(matrix)

