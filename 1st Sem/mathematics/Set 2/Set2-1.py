#Question 1: Define Matrix 

rows = int(input("enter the number of rows in Matrix "))
columns = int(input("enter the number of columns in Matrix "))

print(f"Enter the elements of the {rows}x{columns} matrix")
a = [[int(input("=>")) for j in range(columns)] for i in range(rows)]

#To print matrix in conventional order of matrix
for row in a :
  for element in row:
    print(element,end=" ")
  print('')



