import numpy as np
from numpy.linalg import norm
from numpy import inf

print("Enter the values of  vector : ")
list1 = [int(input()) for i in range(3)]
    
vector1 = np.array(list1)

resultVector = norm(list1,inf)

print("The  of vector is : ", resultVector)