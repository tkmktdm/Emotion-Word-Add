import MeCab
import re
'''
mecabrc: (デフォルト)
-Ochasen: (ChaSen 互換形式)
-Owakati: (分かち書きのみを出力)
-Oyomi: (読みのみを出力)
'''
x = "すもももももももものうち"
longword = 'カーボン製なので手入れや掃除がしやすいです。かなり横に広いのでスペースも充分なのと、ドリンクホルダーがとても便利です。組み立てもしやすかったです。使用する椅子によると思いますが、大きめの椅子だと机の右手前に付いているヘッドホンをかける部分が椅子に当たりがちです。自分はもう慣れましたが、気になる人はヘッドホン掛けを取り付けないか、大きすぎる椅子を使用しないなどの対策を取ると良いです。'

c = MeCab.Tagger("-Ochasen")
w = MeCab.Tagger("-Owakati")
words = []

#print(c.parse(longword))
#print(w.parse(longword))

wordlist = w.parse(longword)
output = wordlist.split('。')
p = re.compile('[\u3000-\u303F]+')
for i in output[:-1]:
    text = re.sub(r'、。！？', '', i)
    text = re.sub('、','', text)
    line = text.split(' ')
    for m in line:
        if m == '':
            line.remove('')
    words.append(line)
print(words)




'''
import openpyxl
import pprint

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
        
print(happy)
print(angle)
print(sad)
print(joy)
'''