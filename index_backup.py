import MeCab
import openpyxl
import pprint
import itertools

from Emotions import *
#from Split_word import *
from Split_word_full import *
from Xlsx_operation import *

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
#pprint.pprint(l_2d1, width=40)


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
        #print(i[0])
        happy.append(i[0])
    elif i[1] == '怒':
        #print(i[0])
        angle.append(i[0])
    elif i[1] == '哀':
        #print(i[0])
        sad.append(i[0])
    elif i[1] == '楽':
        #print(i[1])
        joy.append(i[0])

x = ''
setup = Emotion(happy, angle, sad, joy, model)
sw = Split_word()

#名詞用xlsx読み込み処理
xe = XlsxExist() #elsxファイルがあるか確認
xe.xlsxCheck() 
xwr = XlsxWR() #名詞用elsxファイルの読み書き
worddic = xwr.xlsxRead() #過去の名詞感情データ
#t = ['昔', '名詞', 0]
#worddic.append(t)
#xwr.xlsxWrite(worddic) #名詞感情データ保存


#swfs = sw.firstSplit() #。がない文章だと区切ることができない
#noun, adj = sw.wordPartspeech() #こちらを使うことを推奨
print('終了する際は end と入力してください\n')
while True:
    result = []
    pos = 0
    neg = 0
    x = input()
    #swfs = sw.firstSplit(x)
    noun, adj = sw.wordPartspeech(x)

    #print(noun)
    #print(adj)

    if x == 'end':
        break
    #for i in noun:
        #print(setup.emotion_score(i[0]))
    for k in adj:
        print(setup.emotion_score(k[0]))
        print(k)
        result.append(setup.emotion_score(k[0]))
    
    if noun: 
        for i in result:
            if i == '嬉しい':
                pos += 1
            elif i == '楽しい':
                pos += 1
            elif i == '悲しみ':
                neg += 1
            elif i == '怒り':
                neg += 1
            print(i)
        if pos > neg :
            noun[0][-1] = 1
            print('p')
        elif neg > pos:
            noun[0][-1] = -1
            print('n')
        else:
            print('t')
        print(noun)
        #2次元のリストから1次元のリストに直す処理
        #print(list(itertools.chain.from_iterable(noun)))
        #noun = list(itertools.chain.from_iterable(noun))
        #worddic.append(noun)
    
    #名詞に感情付加
    #kns, ens, word_n = equal(noun, emotion_score)
    #test = sw.speechAdd(kns, ens, word_n, emotion_score)

    #print(setup.emotion_score(x))
#print(posi_nega_score(x))
print('入力モード終了')
print(worddic)
#xwr.xlsxWrite(worddic) #名詞感情データ保存
print('名詞感情データに保存しました。')


'''
x = '面白い'
setup = Emotion(happy, angle, sad, joy, model)
a = setup.emotion_score(x)
print(a)

sw = Split_word()
swfs = sw.firstSplit(word)
noun, adj = sw.wordPartspeech(word)
'''
