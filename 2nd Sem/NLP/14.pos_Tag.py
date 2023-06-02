from nltk import word_tokenize
from nltk.tag import pos_tag

pos_dict = {
'CC': 'coordinating conjunction',
'CD': 'cardinal digit', 
'DT': 'determiner',
'EX': 'existential',  
'FW': 'foreign word', 
'IN': 'preposition/subordinating conjunction',
'JJ': 'adjective', 
'JJR': 'adjective, comparative',  
'JJS': 'adjective, superlative' ,
'LS': 'list marker' ,
'MD': 'modal ',
'NN': 'noun, singular' ,
'NNS': 'noun plural' ,
'NNP': 'proper noun, singular  ',
'NNPS': 'proper noun, plural ',
'PDT': 'predeterminer ',
'POS': 'possessive ending parent’s ',
'PRP': 'personal pronoun ',
'PRP$': 'possessive pronoun', 
'RB': 'adverb ',
'RBR': 'adverb, comparative ',
'RBS': 'adverb, superlative',
'RP': 'particle ',
'TO':  'to go ',
'UH': 'interjection ',
'VB': 'verb, base form'  ,
'VBD': 'verb, past tense' ,
'VBG': 'verb, gerund/present participle',
'VBN': 'verb, past participle  ',
'VBP': 'verb, sing. present, non-3d' ,
'VBZ': 'verb, 3rd person sing. present' ,
'WDT': 'wh-determiner ',
'WP': 'wh-pronoun ',
'WP$': 'possessive wh-pronoun',
'WRB': 'wh-adverb'
}

text = open(r"2nd Sem\NLP\aliceInWonderLand.txt")
text = text.read()

tokenized_text = word_tokenize(text)
parts_of_speech = pos_tag(tokenized_text)

for token in parts_of_speech:
    if token[1] in pos_dict:
        print('{:<13}  {:<12} '.format(token[0], pos_dict[token[1]]))

