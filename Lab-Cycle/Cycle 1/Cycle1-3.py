#Question 3: String pattern matching

string = input("Enter the string: ")
pattern = input("Enter the pattern to be searched: ")

stringArray = []
patternArray = []

for i in string :
  stringArray.append(i)

for j in pattern :
  patternArray.append(j)

patternIndex = 0
stringIndex = 0 
start = stringIndex

while stringIndex < len(stringArray):  

  if stringArray[stringIndex] == patternArray[patternIndex] :
    stringIndex += 1
    patternIndex += 1
  else :
    stringIndex = start + 1
    start = stringIndex
    patternIndex = 0

# printing location of founded pattern
  if patternIndex == len(patternArray):
    print(f"\nGiven pattern found in string from position: \n{start} to {stringIndex - 1}")
    patternIndex = 0


if patternIndex == 0:
  print("\nGiven pattern is not found in the string")