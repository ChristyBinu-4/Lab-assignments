#Question 2: Capitalize first and last letter of a string

print("\nGive input to Capitalize first and last letter of String",end="\n\n")
inputString = input("Enter the String to be converted : ")

stringLength = len(inputString)
outputString = ""

for i in range(stringLength):

  if i == 0 or i == stringLength - 1:
    outputString += inputString[i].capitalize()
  else:
    outputString += inputString[i]

print("Output : ", outputString)