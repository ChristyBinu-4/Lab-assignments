import numpy as np
#function to generate chess board as input and then recieve output to print

def Nqueen(n):
    def attackingAreas(board, row, column):
        #Checking column corresponding to that cell 
        for i in range(row, -1, -1):
            if board[i][column] == 1:
                return False
        #Checking upper diagonal corresponding to that cell
        for i,j in zip(range(row, -1, -1), range(column, -1, -1)):
            if board[i][j] == 1:
                return False
        #Checking lower diagonal corresponding to that cell
        for i, j in zip(range(row, -1, -1), range(column, n)):
            if board[i][j] == 1:
                return False
        return True
        

    def SolveNQueen(board, row) :
        if row == n:
            return True
        for i in range(n):
            if attackingAreas(board, row, i) is True :
                board[row][i] = 1
                if SolveNQueen(board, row + 1):
                    return True
                board[row][i] = 0
        return False


    board = [0 for i in range(n * n)]
    board = np.array(board)
    board = board.reshape(n, n)
    firstRowIndex = 0

    Output = SolveNQueen(board, firstRowIndex)
    return board

    
#read number of queens to be place in n * n chess board
n = int(input("Enter the n - queens to be placed in a n * n chess board => "))
if n >= 4:
    print(Nqueen(n))
else:
    print("N must be more than or equal to 4")