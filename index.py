import MeCab
import openpyxl
import pprint
import itertools

from Emotions import *
from Split_word_full import *
from Xlsx_operation import *
from Parsing_adj_not import *

#xlsxファイル読み取り
wb = openpyxl.load_workbook('origin_dic_emo.xlsx')

sheet = wb['感情分類']
sheet1 = wb['作業者A']
sheet2 = wb['作業者B']
sheet3 = wb['作業者C']

def get_value_list(t_2d):
    return([[cell.value for cell in row] for row in t_2d])

def get_list_2d(sheet, start_row, end_row, start_col, end_col):
    return get_value_list(sheet.iter_rows(min_row=start_row,
                                          max_row=end_row,
                                          min_col=start_col,
                                          max_col=end_col))

l_2d1 = get_list_2d(sheet, 2, 50, 1, 2)

#main処理
#モデル読み込み
model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)
#「非常にポジティブな単語」と「非常にネガティブな単語」を任意で指定
'''happy = ['喜び'], angle = ['怒り'], sad = ['悲しい'], joy = ['楽しい']'''

happy = []
angle = []
sad = []
joy = []

for i in l_2d1:
    if i[1] == '喜':
        happy.append(i[0])
    elif i[1] == '怒':
        angle.append(i[0])
    elif i[1] == '哀':
        sad.append(i[0])
    elif i[1] == '楽':
        joy.append(i[0])

x = ''
setup = Emotion(happy, angle, sad, joy, model)
sw = Split_word()

###___名詞用xlsx読み込み処理
xe = XlsxExist() #elsxファイルがあるか確認
xe.xlsxCheck() 
xwr = XlsxWR() #名詞用elsxファイルの読み書き
worddic = xwr.xlsxRead() #過去の名詞感情データ

### _GiNZAを使って構文解析する
ps = Parsing(spacy.load('ja_ginza'), setup)

#辞書更新に使うリスト
existword = []
newword = []
updateword = []

#メイン処理
print('終了する際は end と入力してください\n')
while True:
    result = []
    pos = 0
    neg = 0
    x = input()
    text = ps.word_pars(x,worddic)
    if x == 'end':
        break

    # xlsxfileのリストに代入処理 -------------------------------

    # worddicに入っているxlsxの内容と入力された単語の感情情報を付加したものを比較して更新
    # existである入力された単語をまとめる
    text = list(itertools.chain.from_iterable(text))
    for i in text:
        exist = [i for w in worddic if i[0]==w[0]]
        if exist != []:
            #if existword:
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
        if exlist != []:
            for e in exlist:
                if i[0] != e[0]:
                    newword.append(i)
                else:
                    print('else')


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

# 感情値の入ってない新しい単語と値を更新する単語の処理
for n in newword:
    worddic.append(n)
for u in updateword:
    worddic.append(u)
        
        # 構文解析
        #sline = ps.word_pars(w[0])

#名詞用の辞書に保存
xwr.xlsxWrite(worddic)

#print(posi_nega_score(x))
print('入力モード終了')

#xwr.xlsxWrite(worddic) #名詞感情データ保存
print('名詞感情データに保存しました。')

