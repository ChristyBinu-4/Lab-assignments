from nltk import word_tokenize
from string import punctuation

text = open("aliceInWonderLand.txt")
text = text.read()

tokenized_text = word_tokenize(text)
textString = ""

for token in tokenized_text:
    if token not in punctuation:
        textString +=  " " + token 

print(textString)
