import gensim
#fasttextのモデルを読み込む

class Emotion():
    def __init__(self, happy, angle, sad, joy, model):
        self.happy = happy
        self.angle = angle
        self.sad = sad
        self.joy = joy
        self.model = model
        
    def emotion_score(self, x):
        #度合いの判定
        #喜
        h = []
        for i in self.happy:
            try:
                n = self.model.similarity(i, x)
                h.append(n)
            except:
                continue
        try:
            h_mean = sum(h)/len(h)
            #print(h_mean)
        except:
            h_mean = 0
        #怒
        a = []
        for i in self.angle:
            try:
                n = self.model.similarity(i, x)
                a.append(n)
            except:
                continue
        try:
            a_mean = sum(a)/len(a)
            #print(a_mean)
        except:
            a_mean = 0
        #哀
        s = []
        for i in self.sad:
            try:
                n = self.model.similarity(i, x)
                s.append(n)
            except:
                continue
        try:
            s_mean = sum(s)/len(s)
            #print(s_mean)
        except:
            s_mean = 0
        #楽
        j = []
        for i in self.joy:
            try:
                n = self.model.similarity(i, x)
                j.append(n)
            except:
                continue
        try:
            j_mean = sum(j)/len(j)
            #print(j_mean)
        except:
            j_mean = 0

        if h_mean > a_mean and h_mean > s_mean and h_mean > j_mean:
            return '喜び', 1# + h_mean
            #return h_mean
        if a_mean > h_mean and a_mean > s_mean and a_mean > j_mean:
            return '怒り', -1# + a_mean
            #return a_mean
        if s_mean > h_mean and s_mean > a_mean and s_mean > j_mean:
            return '悲しみ', -1# + s_mean
            #return s_mean
        if j_mean > h_mean and j_mean > a_mean and j_mean > s_mean:
            return '楽しい', 1# + j_mean
            #return j_mean
        else:
            return 0

###クラス定義###


'''#main処理
#モデル読み込み
model = gensim.models.KeyedVectors.load_word2vec_format('model.vec', binary=False)
#「非常にポジティブな単語」と「非常にネガティブな単語」を任意で指定
happy = ['喜び','やったー']
angle = ['怒り']
sad = ['悲しい']
joy = ['楽しい']

x = '面白い'
setup = Emotion(happy, angle, sad, joy, model)
a = setup.emotion_score(x)
print(a)'''


'''#ループ処理
x = ''
print('終了する際は end と入力してください\n')
while True:
    x = input()
    if x == 'end':
        break
    print(emotion_score(x))
#print(posi_nega_score(x))
print('入力モード終了')
'''