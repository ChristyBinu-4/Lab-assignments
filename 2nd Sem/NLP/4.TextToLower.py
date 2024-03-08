text = open("aliceInWonderLand.txt")
text = text.read()

textString = text.lower()

print("Input text :", text, sep="\n",end="\n\n")
print("Converted Lower case text:", textString, sep="\n", end='\n\n')