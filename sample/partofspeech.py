import MeCab
def mecab_list(text):
    tagger = MeCab.Tagger("-Ochasen")
    wakati = MeCab.Tagger('-Owakati')
    tagger.parse('')
    node = tagger.parseToNode(text)
    word_class = []
    word_noun = []
    word_adjective = []

    re = 0
    wm = wakati.parse(text)
    ww = wm.split(' ')

    while node:
        word = node.surface
        wclass = node.feature.split(',')
        #print(wclass)
        if wclass[0] != u'BOS/EOS':
            if wclass[0] == '名詞':
                if wclass[1] == '一般' and wclass[6] != '*':
                    word_noun.append([wclass[6],wclass[0],0])
                elif wclass[1] == '固有名詞' and wclass[6] != '*':
                    word_noun.append([wclass[6],wclass[0],0])
                elif wclass[1] == '形容動詞語幹':
                    word_adjective.append([wclass[6], '形容詞',0])
                elif wclass[6] == '*':
                    text = ww[re-1]
                    word_noun.append([text, wclass[0], 0])

            if wclass[0] == '動詞':
                if wclass[6] == '比べる':
                    if word_noun[-2][0] != '=':
                        back = word_noun[-1]
                        back2 = word_noun[-2]
                        hikaku = ['>', back2[0], back[0]]
                        word_noun.append(hikaku)
                    #reverve = node.reverse
                    #print(reverve.surface)
                    
                word_adjective.append([wclass[6], '動詞',0])
            
            if wclass[1] == '並立助詞' or wclass[1] == '接続助詞':
                nextWord = node.next
                #print(test.surface)
                word_noun.append(['=',nextWord.surface,0])


            if wclass[0] == '形容詞':
                word_adjective.append([wclass[6],wclass[0],0])
                if wclass[4] == '形容詞・アウオ段':
                    if wclass[6] == 'ない':
                        del word_adjective[-1]
                        nai = word_adjective[-1]
                        nai[-1] = -1
                        del word_adjective[-1]
                        word_adjective.append(nai)
                    else:
                        del word_adjective[-1]

            if wclass[0] == '助動詞':
                if wclass[6] == 'ない':
                    auxiliary = word_adjective[-1]
                    auxiliary[-1] = -1
                    del word_adjective[-1]
                    word_adjective.append(auxiliary)

            if wclass[6] == None:
                word_class.append((word,wclass[0],wclass[1],wclass[2],""))
            else:
                word_class.append((word,wclass[0],wclass[1],wclass[2],wclass[6]))
        
        node = node.next
        re +=1

    return word_noun, word_adjective
    #return word_class
#word_n, word_a = mecab_list('とても美しくないし便利じゃないし、きたないです。でもやっぱりきりんさんがいいです。もうしわけないけど、いいところはひとつもないです。そして使えない')
#word_n, word_a = mecab_list('イス。windows、ウィンドウズはリナックスに比べてユーアイが使えないよね')
word_n, word_a = mecab_list('ハンバーガーとポテトはナゲットに比べておいしいと思った。')
#word_n, word_a = mecab_list('ハンバーガーとポテトはナゲットに比べておいしくないと思った。')
#word_n, word_a = mecab_list('ハンバーガーと比べてポテトがおいしいと思った。')
#word_n, word_a = mecab_list('雨が降ったから祭りがなくなって悲しい')

#print(word_n)
#print(word_a)

'''number = 0
x = 11
y = 2
word_n[-1][-1] = 1
kns = []
ens = []
for i in word_n:
    if i[0] in '=' and word_n[number-1][0] != '>':
        kns.append([word_n[number-1][0],i[1]])
        word_n.remove(i)
    elif i[0] in '=' and word_n[number-1][0] == '>': 
        i[0] = word_n[number-1][1]
        ens.append(i)
        word_n.remove(word_n[number-1])
    number += 1

for i in ens:
    for n in i:
        for a in word_n:
            if n == a[0] and '名詞' == a[1]:
                a[-1] = y
#print(word_n)
count = 0
emo = 0
for i in kns:
    for n in reversed(i):
        #print(n)
        for a in word_n:
            if n == a[0] and count == 0:
                emo = a[-1]
                count +=1
            elif n == a[0] and count != 0:
                a[-1] = emo
            if n == a[0] and '名詞' != a[1]:
                word_n.remove(a)'''

#print(word_n)


def equal(word_n):
    number = 0
    kns = []
    ens = []
    for i in word_n:
        if i[0] in '=' and word_n[number-1][0] != '>':
            kns.append([word_n[number-1][0],i[1]])
            word_n.remove(i)
        elif i[0] in '=' and word_n[number-1][0] == '>': 
            i[0] = word_n[number-1][1]
            ens.append(i)
            word_n.remove(word_n[number-1])
        number += 1
    return kns, ens

def speechAdd(kns, ens, emotion_score):
    for i in ens:
        for n in i:
            for a in word_n:
                if n == a[0] and '名詞' == a[1]:
                    a[-1] = emotion_score
    return word_n
    #return emotionAdd(kns)
    #return 

def emotionAdd(kns):
    count = 0
    emo = 0
    for i in kns:
        for n in reversed(i):
            for a in word_n:
                if n == a[0] and count == 0:
                    emo = a[-1]
                    count +=1
                elif n == a[0] and count != 0:
                    a[-1] = emo
                if n == a[0] and '名詞' != a[1]:
                    word_n.remove(a)
    return word_n

emotion_score = 1 #本番環境で値は変える
kns, ens = equal(word_n)
emo_word = speechAdd(kns, ens, emotion_score)
print(emo_word)

