#Question 8:  Calculate L1 Norm of a vector.
import numpy as np

def l1_norm(vector):
    norm = 0
    for element in vector:
        norm += abs(element)
    return norm


print("Enter the values of  vector : ")
list1 = [int(input()) for i in range(3)]
    
vector1 = np.array(list1)

resultVector1 = l1_norm(list1)

print("The L1 norm of vector is : ", resultVector1)