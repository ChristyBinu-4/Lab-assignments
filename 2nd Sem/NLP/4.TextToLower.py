from nltk import word_tokenize

text = open(r"2nd Sem\NLP\aliceInWonderLand.txt")
text = text.read()

tokenized_text = word_tokenize(text)
textString = ""

for token in tokenized_text:
    textString += token.lower() + " "

print("Input text :", text, sep="\n",end="\n\n")
print("Converted Lower case text:", textString, sep="\n", end='\n\n')