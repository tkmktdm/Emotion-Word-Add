# https://megagonlabs.github.io/ginza/
from ginza import *
import spacy

nlp = spacy.load('ja_ginza')

doc = nlp('この映画も食べ物もよかった')
doc = nlp('映画は良かったけど食べ物はおいしくなかった')
doc = nlp('白米は麺と比べておいしい')
doc = nlp('WindowsはLinuxに比べてUIがゴミだよね')
doc = nlp('ゴミだよね、WindowsはLinuxに比べてUI')
doc = nlp('Linuxと比べるとWindowsはゴミだよね')
doc = nlp('映画とっても面白くない')
doc = nlp('おいしくないし、見た目もきたない、もう行きたくない')
doc = nlp('パンおいしくない')
#doc = nlp('Linux使えよ')


snlist = []
for sent in doc.sents:
    for token in sent:
        #print(token.i, token.orth_, token.lemma_, token.pos_, 
        #      token.tag_, token.dep_, token.head.i)
        snlist.append([token.i, token.orth_, token.lemma_, token.pos_, token.tag_, token.dep_, token.head.i])
#print(snlist[1])
d = []
n = []
#snlist = [s[3]='NOUN' if s in 'PROPN' else print('ok') for s in snlist]
print(snlist)
for s in snlist:
    if s[3] in 'PROPN':
        s[3] = 'NOUN'

for s in snlist:
    if s[0] != s[-1] and 'NOUN' in s:
        nulldic = [s[2:4], snlist[s[-1]][2:4]]
        
        d.append(nulldic)
    if s[0] != s[-1] and s[3] == 'ADJ' and s[2] == 'ない':
        no = [s[2:4], snlist[s[-1]][2:4]]
        #print('no')
        #print(no)
        n.append(no)

for sub in d:
    #print(sub)
    if sub[0][-1] == sub[1][-1]:
        #名詞同士が入ってる際に感情値がついているものであれば値を参照する
        print(sub[0][-1])
        
    else:
        #感情分析にかける
        if sub[0][-1] == 'NOUN':
            print(sub[1][0])
            sub[0].append(1)
        else:
            print(sub[0][0])
            print(sub[0])
            sub[-1].append(1)
            
        #print(s)
    print(sub)

#for ent in doc.ents:
#    print(ent.text, ent.start_char, ent.end_char, ent.label_)

