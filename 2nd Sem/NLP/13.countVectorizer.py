from nltk import word_tokenize
import pandas as pd

text_array = ['Hello my name is james', 'this is my python notebook']
tokenized_text = []

for i in range(len(text_array)):
    tokenized_text.append(word_tokenize(text_array[i]))

uniqueWords = {}

for text in tokenized_text:
    for word in text:
        if word not in uniqueWords:
            uniqueWords[word] = []


for word in uniqueWords:
    for text in tokenized_text:
        if word in text:
            uniqueWords[word].append(1)
        else:
            uniqueWords[word].append(0)

df = pd.DataFrame(uniqueWords)       
print(df)