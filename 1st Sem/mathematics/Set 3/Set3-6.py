#Question 6: Define 5 * 2 matrix data set, split it into x and y components and plot dataset as scatterplot 
import matplotlib.pyplot as plt
import numpy as np

print("Enter the elements in the matrix")
matrix = np.array([[int(input("=>")) for j in range(2)] for i in range(5)])

x,y=np.split(matrix,2,axis=1)

plt.scatter(x, y)
plt.show()
