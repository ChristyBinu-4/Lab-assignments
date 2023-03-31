from nltk import word_tokenize

text = 'this is a very good book to study'
print("Input text: ", text, "\n")

data = word_tokenize(text)

encoded = {}
count = -1

for i in data:
    if i not in encoded:
        count += 1
        encoded[i] = count
    
oneHotEncoding = []
print("One Hot encoding of text")


for i in data:
    array = []
    for j in encoded:
        if i == j:
            array.append(1)
        else:
            array.append(0)
    oneHotEncoding.append(array)

for i,j  in zip(oneHotEncoding,data):
    print(f'{j}\t{i}')