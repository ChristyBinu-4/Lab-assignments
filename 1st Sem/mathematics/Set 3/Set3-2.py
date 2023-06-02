#Question 2: Print Rank of a matrix
import numpy as np

def rank(matrix):
    
    num_rows, num_cols = matrix.shape
    rank = min(num_rows, num_cols)

    for col in range(rank):
        if matrix[col, col] != 0:
            for row in range(col + 1, num_rows):
                factor = matrix[row, col] / matrix[col, col]
                matrix[row, col] -= factor * matrix[col, col]
        else:
            reduce_rank = True
            for row in range(col + 1, num_rows):
                if matrix[row, col] != 0:
                    matrix[[col, row]] = matrix[[row, col]]
                    reduce_rank = False
                    break
            if reduce_rank:
                rank -= 1
                if col < num_cols - 1:
                    matrix[:, col] = matrix[:, rank]

    return rank


order = 3

print("Enter elements in matrix : ")
matrix = [[int(input("=>")) for j in range(order)] for i in range(order)]
matrix = np.array(matrix)

print("Matrix : ", matrix, sep='\n')

rank = rank(matrix)
print("Rank of matrix is : ", rank)