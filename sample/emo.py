import gensim
#fasttextのモデルを読み込む
model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)

#「非常にポジティブな単語」と「非常にネガティブな単語」を任意で指定
#喜
happy = ['喜び', '誇らしい', '感動', '好き', '幸福感', '祝い', '願望', '快感']
#怒
angle = ['不満', '不安', '憂鬱', '辛さ', '嫌悪', '恥ずかしい', '焦り', '怒り', '恨み', '恐れ', '恐怖', '悔しさ', '興奮', '失望', '不快', '怠さ', 'あきれ', '緊張', '妬み', '憎い', '情けない']
#哀
sad = ['悲しい', '寂しい', '切ない', '苦しい', '困惑', 'きまずさ', '悩み', 'あわれみ', '見下し', '謝罪', 'ためらい', '心配', '残念']
#楽
joy = ['安らぎ', '楽しさ', '親しみ', '尊敬', '尊さ', '感謝', '気持ちが良い', '驚き', '穏やか']

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
        return '喜び '# + h_mean
        #return h_mean
    if a_mean > h_mean and a_mean > s_mean and a_mean > j_mean:
        return '怒り '# + a_mean
        #return a_mean
    if s_mean > h_mean and s_mean > a_mean and s_mean > j_mean:
        return '悲しみ '# + s_mean
        #return s_mean
    if j_mean > h_mean and j_mean > a_mean and j_mean > s_mean:
        return '楽しい '# + j_mean
        #return j_mean
    else:
        return 0

x = ''
print('終了する際は end と入力してください\n')
while True:
    x = input()
    if x == 'end':
        break
    print(emotion_score(x))
#print(posi_nega_score(x))
print('入力モード終了')