# https://megagonlabs.github.io/ginza/
from ginza import *
import spacy

nlp = spacy.load('ja_ginza')
#doc = nlp('鬼滅の刃最高だったわ 分かるこの映画やばいよね')
#doc = nlp('映画 良かった 分かる 映画 やばい')
#doc = nlp('鬼滅刃面白い')
doc = nlp('この映画も食べ物もよかった')
#doc = nlp('この店やばくない？ めちゃくちゃごはんが不味いよね')
#doc = nlp('店 やばい ごはん 不味い') #ok
doc = nlp('おいしくないし、見た目もきたない、もう行きたくない')
snlist = []
for sent in doc.sents:
    for token in sent:
        print(token.i, token.orth_, token.lemma_, token.pos_, 
              token.tag_, token.dep_, token.head.i)
        snlist.append([token.i, token.orth_, token.lemma_, token.pos_, token.tag_, token.dep_, token.head.i])
print(snlist[1])

for ent in doc.ents:
    print(ent.text, ent.start_char, ent.end_char, ent.label_)

#doc = nlp('あきらめたらそこで試合終了だ')
#token = doc[4]

#print(token)
#print(token.vector)
#similarity_doc = token.similarity(doc)
#print(similarity_doc)
#print(token.vector.shape)


#word1 = nlp('おむすび')
#word2 = nlp('おにぎり')
#word3 = nlp('カレー')

#print(word1.similarity(word2))
#0.8016603151410209
#print(word1.similarity(word3))
#0.5304326270109458'''


from spacy import displacy
displacy.serve(doc, style='dep', options={'compact':True})

#http://localhost:5000/
 