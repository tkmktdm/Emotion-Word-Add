import gensim
#fasttextのモデルを読み込む
model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)

#「非常にポジティブな単語」と「非常にネガティブな単語」を任意で指定
#喜
happy = ['喜び']
#怒
angle = ['怒り']
#哀
sad = ['悲しい']
#楽
joy = ['楽しい']

#
yes = ['うん','そう','いいよ']
no = ['だめ','いや','だけど','ちがう']

def emotion_score(x):
    #度合いの判定
    #yes
    ok = []
    for i in yes:
        try:
            n = model.similarity(i, x)
            ok.append(n)
        except:
            continue
    try:
        ok_mean = sum(ok)/len(ok)
    except:
        ok_mean = 0
   
    #楽
    ng = []
    for i in no:
        try:
            n = model.similarity(i, x)
            ng.append(n)
        except:
            continue
    try:
        ng_mean = sum(ng)/len(ng)
    except:
        ng_mean = 0

    if ok_mean > ng_mean:
        return '肯定', ok_mean
        #return h_mean
    if ng_mean > ok_mean:
        return '否定', ng_mean
        #return a_mean
    else:
        return 'NaN', 0

x = ''
print('終了する際は end と入力してください\n')
while True:
    x = input()
    if x == 'end':
        break
    w,i = emotion_score(x)
    print(w)
    print(i)
#print(posi_nega_score(x))
print('入力モード終了')