#Question 10:  Calculate Max Norm of a vector.
import numpy as np

def max_norm(vector):
    norm = 0
    for element in vector:
        if abs(element) > norm:
            norm = abs(element)
    return norm

print("Enter the values of  vector : ")
list1 = [int(input()) for i in range(3)]
    
vector1 = np.array(list1)

resultVector1 = max_norm(list1)

print("The Max norm of vector is : ", resultVector1)