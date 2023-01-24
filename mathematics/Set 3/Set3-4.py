import numpy as np 
from numpy.linalg import eig

order = 3
print("Enter the elements in the matrix")
matrix = np.array([[int(input("=>")) for j in range(order)] for i in range(order)])
print(matrix)


eigenValue, eigenVector = eig(matrix)
eigenValue = np.array(eigenValue)
eigenVector = np.array(eigenVector)

print("Eigen value of a matrix : ", eigenValue, sep='\n')
print("Eigen vector of a matrix : ", eigenVector, sep='\n')
