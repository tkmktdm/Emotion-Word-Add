import MeCab
mecab = MeCab.Tagger('-Ochasen')
#print(mecab.parse('便利なもの'))
print(mecab.parse('私はだめだと思った'))
print(mecab.parse('テーブルとイスとパソコンは揃えないとだね'))
print(mecab.parse('WindowsはLinuxに比べてUIがゴミだよね'))
#print(mecab.parse('linux使えよ'))
#print(mecab.parse('lineとtwitterの違いはやっぱり通話ができるところだよね'))
print(mecab.parse('アイスと扇風機とエアコンは夏はいいけど冬は寒くていやだよね'))
#print(mecab.parse('アイスと扇風機とエアコンを比べると扇風機は効果薄いよね'))

while True:
    result = []
    pos = 0
    neg = 0
    x = input()
    print(mecab.parse(x))





#mecabrc:(引数なし)
#-Ochasen: (ChaSen 互換形式)
#-Owakati: (分かち書きのみを出力)
#-Oyomi: (読みのみを出力)