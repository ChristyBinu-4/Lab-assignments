# Question 11: Creating an identity matrix of order 4
import numpy as np

rows = 4
columns = 4
identityMatrix = []

for i in range(rows):
    for j in range(columns):
        if i == j :
            identityMatrix.append(1)
        else :
            identityMatrix.append(0)

identityMatrix = np.array(identityMatrix)
identityMatrix = identityMatrix.reshape(rows,columns)
print(identityMatrix)