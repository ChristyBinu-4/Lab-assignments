from nltk import word_tokenize

text = open(r"C:\Users\91703\Documents\PG docs\Lab-assignments\2nd Sem\NLP\aliceInWonderLand.txt")
textString = ""

for i in text:
  textString += i

text_tokenized = word_tokenize(textString)

token_list = {}

for i in text_tokenized:
  if i not in token_list:
    token_list[i] = 1
  else :
    token_list[i] += 1

for word in token_list:
  print('{:<13}  {:<12} '.format(word, token_list[word]))