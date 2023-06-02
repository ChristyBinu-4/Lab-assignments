import numpy as np
from math import sqrt, degrees, acos


def read_vector():
    vector = [int(input(f"{v} =>")) for v in ["i", "j", "k"]]
    vector = np.array(vector)
    return vector


def rootOfValueSquares(vector):
    sum = 0
    for value in vector:
        sum += value**2
    result = sqrt(sum)
    return result


print("Enter the values in  First vector : ")
vector1 = read_vector()
print(vector1)

print("Enter the values in Second vector : ")
vector2 = read_vector()
print(vector2)

dotProduct = np.dot(vector1, vector2)
d1 = rootOfValueSquares(vector1)
d2 = rootOfValueSquares(vector2)

cos = dotProduct / (d1 * d2)
angle = degrees(acos(cos))
print("The cosine similarity between vector is :", angle, sep="\n")
