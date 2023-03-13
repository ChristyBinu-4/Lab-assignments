#Question 7: Perform vector Scalar Multiplication
import numpy as np

print("Enter the  values of first vector : ")
list1 = [int(input()) for i in range(3)]

scalar = int(input("Enter the scalar value : "))
vector1 = np.array(list1)

resultVector = vector1 * scalar

print("The resultant vector is : ", resultVector)