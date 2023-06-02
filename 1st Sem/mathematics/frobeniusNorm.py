import numpy as np
from numpy import linalg as LA

dimension = int(input("Enter the dimension of matrix :"))

print("Enter the values of  vector : ")
list1 = [int(input()) for i in range(dimension ** 2)]

array = np.array(list1)    
a = array.reshape((dimension, dimension))

print("Original array:")
print(a)

print("Frobenius norm :")
print(LA.norm(a, 'fro'))