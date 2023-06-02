from nltk.corpus import stopwords
from nltk import word_tokenize

stopWords = stopwords.words('english')

text = open(r"2nd Sem\NLP\aliceInWonderLand.txt")
text = text.read()

tokenized_text = word_tokenize(text)

textString = []

for i in tokenized_text:
    if i not in stopWords:
        textString.append(i)

for text in textString:
    print(text, end = " ")