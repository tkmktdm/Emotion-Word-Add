import openpyxl
import pprint
import itertools

from Emotions import *
from Xlsx_operation import *
from Parsing import *

# xlsxファイル読み取り
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

# モデル読み込み
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

### ___名詞用xlsx読み込み処理
xe = XlsxExist() # elsxファイルがあるか確認
xe.xlsxCheck()
xwr = XlsxWR() # 名詞用elsxファイルの読み書き
loaddata = xwr.xlsxRead() # 過去の名詞感情データ読み取り
print(loaddata)
worddic = {}  # 辞書作成 loaddataを入れる

# worddic辞書の形で既存の情報を読みとり
for l in loaddata: # key = 名詞 value = [NOUN, ポジネガの値]
    if None not in l:
        worddic[l[0]] = l[1:]

print('worddicの過去名詞感情データ')
print(worddic)

### _GiNZAを使って構文解析する
ps = Parsing(spacy.load('ja_ginza'), setup)

# メイン処理
print('終了する際は end と入力してください\n')
while True:
    x = input()
    text = ps.word_pars(x,worddic)
    if x == 'end':
        break
    # xlsxfileのリストに代入処理 -------------------------------

    # worddicに入っているxlsxの内容と入力された単語の感情情報を付加したものを比較して更新
    text = list(itertools.chain.from_iterable(text))
    # textの返り値
    # [[None, None, None], ['店', 'NOUN', -1], ['ごはん', 'NOUN', -1]] や [['Linux', 'NOUN', -1], ['Windows', 'NOUN', 0], ['ゴミ', 'NOUN', 0]]

    # 同じ言葉が二重に入っていた際に最後の値を残す
    for x,j in zip(text[:-1], text[1:]):
        if x[0] == j[0]:
            text.remove(x)
    
    # worddicに入力されたtextを代入、値が変わっていれば更新
    for w in text:
        if w[0] in worddic:
            pos_neg = worddic[w[0]][-1] + w[-1]
            if pos_neg < 0:
                pos_neg = -1
            elif pos_neg > 0:
                pos_neg = 1
            else:
                pos_neg = 0
            worddic[w[0]] = [w[1],pos_neg]
        else:
            worddic[w[0]] = w[1:]

print('最新辞書情報')
print(worddic)

# xlsxファイルに書き込むためリストに変更
wordall= []
for k, v in worddic.items():
    wordall.append([k,v[0],v[1]])
print(wordall)
xwr.xlsxWrite(wordall)

# 名詞感情データ保存
xwr.xlsxWrite(worddic)

print('名詞感情データに保存しました。')