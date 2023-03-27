import spacy

# nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load('en_core_web_md')

nlp = spacy.load('en_core_web_lg')
text = "England won the 2019 world cup vs The 2019 world cup"

# text = open(r"2nd Sem\NLP\aliceInWonderLand.txt")
# text = text.read()

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)