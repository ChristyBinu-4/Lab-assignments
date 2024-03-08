#Question 6: Find dot product of two vectors
import numpy as np

print("Enter the  values of first vector : ")
list1 = [int(input()) for i in range(3)]

print("Enter the values of second vector : ")
list2 = [int(input()) for i in range(3)]
    
vector1 = np.array(list1)
vector2 = np.array(list2)

resultVector = np.dot(vector1,vector2)

print("The resultant vector is : ", resultVector)