from nltk import word_tokenize

text = ['this is a very good book to study',
        'This is second sentence',
        'This is third sentence']

#print("Input text: ", text, "\n")

data = []
for sentence in text :
    sentenceTokens = word_tokenize(sentence)
    for word in sentenceTokens:
        if word not in  data:
            data.append(word)

print(data)            