from nltk import word_tokenize

customDictionary = {
    'LOL': 'Laughing out loud',
    'ASAP': 'As soon as possible',
    'FYI': 'For your information',
    'G2G': 'Got to go',
    'FB': 'Facebook',
    'MSG': 'Message',
    'TTYL': 'Talk to you later',
    'IMO': 'In my opinion'
}

text = "Please call me ASAP"
tokenized_text = word_tokenize(text)

textString = " "
for word in tokenized_text:
    if word in customDictionary:
        textString += customDictionary[word] + " "
    else:
        textString += word +" "

print(textString)
