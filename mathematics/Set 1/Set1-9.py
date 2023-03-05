#Question 9:  Calculate L2 Norm of a vector.
import numpy as np

def l2_norm(vector):
    norm = 0
    for element in vector:
        norm += element**2
    return norm**0.5


print("Enter the values of  vector : ")
list1 = [int(input()) for i in range(3)]
    
vector1 = np.array(list1)

resultVector1 = l2_norm(list1)

print("The L2 norm of vector is : ", resultVector1)