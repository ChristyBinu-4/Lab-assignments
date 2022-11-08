import numpy as np

list = []


print("Enter the  values of first vector : ")
for i in range(3):
    value = int(input())
    list.append(value)
scalar = int(input("Enter the scalar value"))

vector1 = np.array(list)


resultVector = vector1 * scalar

print("The resultant vector is : ", resultVector)