import MeCab
'''
mecabrc: (デフォルト)
-Ochasen: (ChaSen 互換形式)
-Owakati: (分かち書きのみを出力)
-Oyomi: (読みのみを出力)
'''
x = "すもももももももものうち"
m = MeCab.Tagger ("-Owakati")
#print(m.parse (x))
inputs = m.parse(x)
inputs = inputs.split(' ')
inputs = inputs[:-1]
#print(inputs)

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

#l_2d = get_list_2d(sheet, 2, 1979, 1, 3)
l_2d1 = get_list_2d(sheet, 2, 50, 1, 2)
'''
l_2d2 = get_list_2d(sheet1, 2, 1979, 1, 3)
l_2d3 = get_list_2d(sheet2, 2, 1979, 1, 3)
l_2d4 = get_list_2d(sheet3, 2, 1979, 1, 3)
'''
#pprint.pprint(l_2d1, width=40)
#print(l_2d1[1][1])

'''
pprint.pprint(l_2d2, width=40)
pprint.pprint(l_2d3, width=40)
pprint.pprint(l_2d4, width=40)
'''

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