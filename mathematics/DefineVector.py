import numpy as np
list = []
print("Enter the values of vector : ")
for i in range(3):
    value = int(input())
    list.append(value)

vector1 = np.array(list)

print("The vector defined is : ",vector1)
