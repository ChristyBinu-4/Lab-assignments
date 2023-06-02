from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

text = input("enter any text:\n")

word_stemmer = PorterStemmer()
stemmedText = word_stemmer.stem(text)
print("\nStem of text: ", stemmedText)

word_Lemmatizer = WordNetLemmatizer()
lemmatizedText = word_Lemmatizer.lemmatize(text)
print("\nlemma of text: ", lemmatizedText)

