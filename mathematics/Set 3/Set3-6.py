import matplotlib.pyplot as plt
import numpy as np

print("Enter the elements in the matrix")
matrix = np.array([[int(input("=>")) for j in range(2)] for i in range(5)])

x,y=np.split(matrix,2,axis=1)

plt.scatter(x, y)
plt.show()
