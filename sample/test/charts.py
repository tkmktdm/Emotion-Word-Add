import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#sns.set(font='IPAexGothic')
#%matplotlib inline
'''dataset = pd.DataFrame([[100, 200, 50], [300, 400, 600], [50, 300, 60]], 
                       columns=['A支店', 'B支店', 'C支店'], 
                       index=['4月', '5月', '6月'])

fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(dataset.columns, dataset.sum())
plt.show()'''


#感情分析
import gensim
#fasttextのモデルを読み込む
model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)

#「非常にポジティブな単語」と「非常にネガティブな単語」を任意で指定
happy = ['喜び']
angle = ['怒り']
sad = ['悲しい']
joy = ['楽しい']

def emotion_score(x):
    #度合いの判定
    #喜
    h = []
    for i in happy:
        try:
            n = model.similarity(i, x)
            h.append(n)
        except:
            continue
    try:
        h_mean = sum(h)/len(h)
    except:
        h_mean = 0
    #怒
    a = []
    for i in angle:
        try:
            n = model.similarity(i, x)
            a.append(n)
        except:
            continue
    try:
        a_mean = sum(a)/len(a)
    except:
        a_mean = 0
    #哀
    s = []
    for i in sad:
        try:
            n = model.similarity(i, x)
            s.append(n)
        except:
            continue
    try:
        s_mean = sum(s)/len(s)
    except:
        s_mean = 0
    #楽
    j = []
    for i in joy:
        try:
            n = model.similarity(i, x)
            j.append(n)
        except:
            continue
    try:
        j_mean = sum(j)/len(j)
    except:
        j_mean = 0

    if h_mean > a_mean and h_mean > s_mean and h_mean > j_mean:
        return '喜び ', h_mean, a_mean, s_mean, j_mean
        #return h_mean
    if a_mean > h_mean and a_mean > s_mean and a_mean > j_mean:
        return '怒り ', h_mean, a_mean, s_mean, j_mean
        #return a_mean
    if s_mean > h_mean and s_mean > a_mean and s_mean > j_mean:
        return '悲しみ ', h_mean, a_mean, s_mean, j_mean
        #return s_mean
    if j_mean > h_mean and j_mean > a_mean and j_mean > s_mean:
        return '楽しい ', h_mean, a_mean, s_mean, j_mean
        #return j_mean
    else:
        return 0

'''x = ''
print('終了する際は end と入力してください\n')
while True:
    x = input()
    if x == 'end':
        break
    print(emotion_score(x))
#print(posi_nega_score(x))
print('入力モード終了')'''

word = '面白い'
score = 0
x, scH, scA, scS, scJ = emotion_score(word)
print(x)

#喜　怒　哀　楽
dataset = pd.DataFrame([scH, scA, scS, scJ], 
                       columns=[word], 
                       index=['喜び', '怒り', '悲しみ','楽しみ'])

'''fig, ax = plt.subplots(figsize=(10, 8))
ax.bar(dataset.columns, dataset.sum())
plt.show()'''

fig, ax = plt.subplots(figsize=(10, 8))
for i in range(len(dataset)):
    ax.bar(dataset.columns, dataset.iloc[i], bottom=dataset.iloc[:i].sum())
ax.set(xlabel='x', ylabel='y')
ax.legend(dataset.index)
plt.show()