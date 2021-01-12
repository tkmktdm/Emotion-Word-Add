import itertools
'''
test =[]
noun = [[['Linux', 'NOUN', -1], ['比べる', 'VERB']], [['Windows', 'NOUN'], ['ゴミ', 'NOUN']]]#, [['Windows', 'NOUN'], ['ゴミ', 'NOUN']], [['映画', 'NOUN', 1], ['面白い', 'ADJ']]
for n in noun:
    for splits in n:
    #print(n)
        test.append(splits)
#print(noun)
print(test)
#noun = list(itertools.chain.from_iterable(noun))
#print(noun)
'''
worddic = [[None, None, None], ['白米', 'NOUN', 1], ['映画', 'NOUN', 1]]
text = [[['白米', 'NOUN', -1]], [['麺', 'NOUN', -1]]]
new_dic = []
text = list(itertools.chain.from_iterable(text))

existword = []
newword = []
wordrmdic = []
for i in text:
    #new = [i for w in worddic if i[0]==w[0]]
    exist = [i for w in worddic if i[0]==w[0]]
    print(exist)
    if exist != []:
        existword.append(exist)

# worddicから被っている単語を見つけて取り出す
for w in worddic:
    exlist = list(itertools.chain.from_iterable(existword))
    for i in exlist:
        if i[0]==w[0]:
            worddic.remove(w)
            wordrmdic.append(w)

print('-----------')
for i in text:
    exlist = list(itertools.chain.from_iterable(existword))
    for e in exlist:
        if i[0] == e[0]:
            print(e)
        else:
            print(i)
            newword.append(i)
    #new = [i for e in existword if i[0]!=e[0]]
    #print(new)
    #if new != []:
    #    newword.append(new)
print('====================')
#print(existword)
#print(newword)
worddic.append(newword)
    #if i[0] in worddic:
    #    print(i)
    #else:
    #    print('ng')

#print(set(worddic) - set(text))
#if text in worddic:
#    print('if')

    #a = [print(i) if i[0] == word[0] else print('else') for i in text]
    #new_dic.append([print(i) if i[0] == word[0] else print('else') for i in text])
    #for i in text:
    #    print(i)
    #print(word)
    #print('word')
    #print(text[0])
    #print('text')
    #if word[0] == text[0]:
    #    print(text)
    #    print('text ue')

#for w in text:
#    for splits in w:
#        print(splits)

        #print(splits)
        #print(worddic)
        #new_dic = [splits if splits[0] == dic[0] else dic for dic in worddic]
        #new_dic.append([splits if splits[0] == dic[0] else dic for dic in worddic])
#t = list(itertools.chain.from_iterable(text))
#print(t)
#new_dic.append([s if s[0] == dic[0] else dic for dic in worddic for s in t])
#print(worddic)

ori = [[None, None, None], ['映画', 'NOUN', 1]]
tests =[['麺', 'NOUN', -1], ['Linux', 'NOUN', -1], ['Windows', 'NOUN', 0], ['ゴミ', 'NOUN', 0]]
#tests = list(itertools.chain.from_iterable(tests))
for tas in tests:
    ori.append(tas)
print(ori)