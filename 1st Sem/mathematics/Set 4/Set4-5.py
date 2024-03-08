#Question 5: print given pattern
#1                      1
#1 2                   1 1 
#1 2 3                1 1 1
#1 2 3 4             1 1 1 1

#printing first pattern 
string = ""

for i in range(1, 5):
  string += str(i) + " "
  print(string)

#printing second pattern
for i in range(5):

  for j in range(5 - i):
    print(end=" ")

  for j in range(i):
    print(1,end=" ")
  print(end="\n")

