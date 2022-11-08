import numpy as np
from numpy.linalg import norm

list1 = []


print("Enter the values of  vector : ")
for i in range(3):
    value = int(input())
    list1.append(value)
    
vector1 = np.array(list1)

resultVector = norm(list1,2)

print("The L2 norm of vector is : ", resultVector)