import itertools

worddic = [[None, None, None], ['白米', 'NOUN', 1], ['映画', 'NOUN', 1]]
text = [[['白米', 'NOUN', -1]], [['麺', 'NOUN', -1]]]
new_dic = []
text = list(itertools.chain.from_iterable(text))

existword = []
newword = []
updateword = []
# existである入力された単語をまとめる
for i in text:
    exist = [i for w in worddic if i[0]==w[0]]
    if exist != []:
        existword.append(exist)

# worddicから被っている単語を見つけて取り出す
for w in worddic:
    exlist = list(itertools.chain.from_iterable(existword))
    for i in exlist:
        if i[0]==w[0]:
            worddic.remove(w)
            updateword.append(w)

# 辞書に存在しない単語をまとめる
for i in text:
    exlist = list(itertools.chain.from_iterable(existword))
    for e in exlist:
        if i[0] != e[0]:
            newword.append(i)

# 辞書の感情値の更新がある場合は更新させる
for e,r in zip(existword, updateword):
    e = list(itertools.chain.from_iterable(e))
    if e[0] == r[0]:
        emopn = e[-1] + r[-1]
        if emopn == 0:
            r[-1] = 0
        elif emopn > 0:
            r[-1] = 1
        elif emopn < 0:
            r[-1] = -1

# 辞書に追加
worddic.append(newword)
worddic.append(updateword)
print(worddic)
