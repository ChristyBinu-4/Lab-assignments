#Question 5: Print Eigen Values and eigen vectors of a matrix and reconstruct the matrix
import numpy as np 
from numpy import dot, diag
from numpy.linalg import eig, inv

order = 3
print("Enter the elements in the matrix")
matrix = np.array([[int(input("=>")) for j in range(order)] for i in range(order)])
print(matrix)

eigenValue, eigenVector = eig(matrix)

InverseEigen = inv(eigenVector)

vectorDiagonal = diag(eigenValue)

rematrix = eigenVector.dot(vectorDiagonal).dot(InverseEigen)

print("eigen value of matrix is : ", eigenValue, sep="\n")
print("eigen vector of matrix is : ", eigenVector, sep="\n")
print("Reconstructed matrix is :", rematrix, sep="\n")