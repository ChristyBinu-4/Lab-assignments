import numpy as np
from numpy.linalg import norm

print("Enter the values of  vector : ")
list1 = [int(input()) for i in range(3)]

vector1 = np.array(list1)

resultVector = norm(list1,2)

print("The L2 norm of vector is : ", resultVector)