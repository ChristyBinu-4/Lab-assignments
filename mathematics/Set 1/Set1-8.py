#Question 8: Calculate L1, L2, Max Norms of a vector.
import numpy as np
from numpy.linalg import norm
from math import inf

print("Enter the values of  vector : ")
list1 = [int(input()) for i in range(3)]
    
vector1 = np.array(list1)

resultVector1 = norm(list1, 1)
resultVector2 = norm(list1, 2)
resultVector3 = norm(list1, inf)

print("The L1 norm of vector is : ", resultVector1)
print("The L2 norm of vector is : ", resultVector2)
print("The Max norm of vector is : ", resultVector3)