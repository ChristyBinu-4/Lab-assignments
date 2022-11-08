import numpy as np
from numpy import linalg as LA

list1 = []
n = int(input("Enter the number of values :"))
dimension = int(input("Enter the number of values :"))

print("Enter the values of  vector : ")
for i in range(n):
    value = int(input())
    list1.append(value)

array = np.array(list1)    
a = array.reshape((dimension, dimension))

print("Original array:")
print(a)

print("Frobenius norm :")
print(LA.norm(a, 'fro'))