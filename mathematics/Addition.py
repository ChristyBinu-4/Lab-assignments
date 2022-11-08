import numpy as np

list1 = []
list2 = []

print("Enter the  values of first vector : ")
for i in range(3):
    value = int(input())
    list1.append(value)

print("Enter the values of second vector : ")
for i in range(3):
    value = int(input())
    list2.append(value)
    
vector1 = np.array(list1)
vector2 = np.array(list2)

print("The resultant vector is : ", vector1 + vector2)