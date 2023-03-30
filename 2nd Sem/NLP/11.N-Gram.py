from digitToWord import digitToWord

def generate_ngram(text, ngram):
    words = text.split()
    if len(words) < ngram:
        ngram = len(words) - 1
    output = []

    for i in range(len(words) - ngram):
        output.append(words[i:i+ngram])
    return output

text = 'this is a very good book to study'
print("Given text:",text,sep="\n", end="\n\n")

n = 2

if n == 0:
    print("\nN must be greater than 0\n")
    exit()
else :
    word_for_n = digitToWord(n)
    print(f"\n{word_for_n}-gram Model for given text :\n")
    
    

generated_ngram = generate_ngram(text, n)


for i in generated_ngram:
    print(f"{i[len(i)-1]} | ", end="")
    for j in range(0, len(i)-1):
      print(i[j], end=" ")
    print("\n")