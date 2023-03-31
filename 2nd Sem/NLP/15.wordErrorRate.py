from nltk import word_tokenize

reference = "What a bright day"
print("Reference Word : ", reference)

hypothesis = "What a light day"
print("hypothesis Word : ", hypothesis)

reference_tokenized =  word_tokenize(reference)
hypothesis_tokenized = word_tokenize(hypothesis)

sameWordCount = 0

for word in hypothesis_tokenized:
    if word in reference_tokenized:
        sameWordCount += 1

totalCount = len(reference_tokenized)
errorCount = len(reference_tokenized) - sameWordCount

print(totalCount, errorCount)

wordErrorRate = errorCount/totalCount

print("Word Error rate of given case : ", wordErrorRate)