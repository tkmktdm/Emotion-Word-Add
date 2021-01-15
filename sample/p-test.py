# https://megagonlabs.github.io/ginza/
from ginza import *
import spacy
#from Emotions import *

class Parsing:
    def __init__(self,nlp, setup):
        self.nlp = nlp
        self.setup = setup

    def word_pars(self,doc,worddic):
        sndic = {}
        no = {}
        key_indexs = {}
        #snlist = []
        doc = self.nlp(doc)
        all_dic = {}
        pos_neg = 0
        for sent in doc.sents:
            for token in sent:
                all_dic[token.lemma_] = [token.i, token.pos_, token.tag_, pos_neg, token.head.i]
                #if token.pos_ in 'PROPN':
                #    token.pos_ = 'NOUN'
                if token.tag_ == '接尾辞-名詞的-一般':
                    print('pass')
                elif token.i != token.head.i and 'NOUN' in token.pos_ or 'PROPN' in token.pos_:
                    sndic[token.lemma_] = [token.i, 'NOUN', token.tag_, token.head.i]
                    #sndic[token.lemma_] = [token.i, token.pos_, token.tag_, token.head.i]
                #snlist.append([token.i, token.orth_, token.lemma_, token.pos_, token.tag_, token.dep_, token.head.i])
        print(sndic)
        print(all_dic)
        for k, v in all_dic.items():
            #keys
            key_indexs[v[0]] = k
            if v[0] != v[-1] and v[1] == 'ADJ' or v[1] == 'AUX' and k == 'ない':
                all_dic[key_indexs[v[-1]]][3] = -1

                #print(all_dic[v[-1]])
                #no[k[v-1]]=-1
            #if s[0] != s[-1] and 'NOUN' in s:
            #    nulldic
        print('all_dic')
        print(all_dic)
        
        #名詞とその後にかかっている単語をペアにする
        for s in snlist:
            if s[0] != s[-1] and 'NOUN' in s:
                nulldic = [s[2:4], snlist[s[-1]][2:4]]
                d_pair.append(nulldic)
        
            #否定形のペアを取り出し
            if s[0] != s[-1] and s[3] == 'ADJ' and s[2] == 'ない':
                no = [s[2:4], snlist[s[-1]][2:4]]
                n_pair.append(no)

        

        #元のもの
        d_pair = []
        n_pair = []
        rm_word = []
        #print('snlist')
        #print(snlist)
        
        #複合名詞　名詞、名詞となるものが入るとエラーになるので接尾辞を削除する
        for s in snlist:
            #judge_suffix = s[4].split('-')
            #if '接尾辞' in judge_suffix:
            #    snlist.remove(s)
            if s[4] == '接尾辞-名詞的-一般':
                snlist.remove(s)

            #名詞　固有名詞の値を同じにする
            if s[3] in 'PROPN':
                s[3] = 'NOUN'

        #名詞とその後にかかっている単語をペアにする
        for s in snlist:
            if s[0] != s[-1] and 'NOUN' in s:
                nulldic = [s[2:4], snlist[s[-1]][2:4]]
                d_pair.append(nulldic)
        
            #否定形のペアを取り出し
            if s[0] != s[-1] and s[3] == 'ADJ' and s[2] == 'ない':
                no = [s[2:4], snlist[s[-1]][2:4]]
                n_pair.append(no)
        



        #名詞と動詞、形容詞のペアに感情を付加
        pass_sub = 0
        pass_sub1 = 0
        for sub in d_pair:
            if sub[0][-1] == sub[1][-1]:
                #名詞同士が入ってる際に感情値がついているものであれば値を参照する
                # 未完成部分
                for i in worddic:
                    if sub[0][0] == i[0] and pass_sub == 0:
                        sub[0].append(i[-1])
                        pass_sub += 1
                    elif sub[1][0] == i[0] and pass_sub1 == 0:
                        sub[1].append(i[-1])
                        pass_sub1 += 1
                    elif pass_sub == 0 and pass_sub1 == 0 and i == worddic[-1] and i != None:
                        sub[0].append(0)
                        sub[1].append(0)
                #if sub[0][-1] == sub[1][-1]:
                #sub[0][-1]
                #sub[1][-1]

            '''else:
                #感情分析にかける
                if sub[0][-1] == 'NOUN':
                    emotion,pos_neg = self.setup.emotion_score(sub[1][0])
                    if n_pair != []:
                        for n in n_pair:
                            if n[-1][0] == sub[1][0]:
                                sub[0].append(pos_neg * -1)
                                sub[1].append(0)
                            else:
                                sub[0].append(pos_neg)
                                sub[1].append(0)
                        #sub[0].append(pos_neg)
                        #sub[1].append(0)
                        if sub[1][-1] != 'NOUN':
                            rm_word.append(sub[1])
                            sub.remove(sub[1])
                    else:
                        sub[0].append(pos_neg)
                        sub[1].append(0)
                        if sub[1][-1] != 'NOUN':
                            sub.remove(sub[1])
                    
                else:
                    emotion,pos_neg = self.setup.emotion_score(sub[0][0])

                    if n_pair != []:
                        for n in n_pair:
                            if n[-1][0] == sub[0][0]:
                                sub[1].append(pos_neg * -1)
                                sub[0].append(0)
                            else:
                                sub[1].append(pos_neg)
                                sub[0].append(0)
                        #sub[1].append(pos_neg)
                        #sub[0].append(0)
                        if sub[0][-1] != 'NOUN':
                            rm_word.append(sub[0])
                            sub.remove(sub[0])
                    else:
                        sub[1].append(pos_neg)
                        sub[0].append(0)
                        if sub[0][-1] != 'NOUN':
                            sub.remove(sub[0])'''
        print(d_pair)
        return d_pair


worddic = {None: [None, None], '葵': ['NOUN', 1], 'Windows': ['NOUN', -1], 'Linux': ['NOUN', 0], '方': ['NOUN', -1]}
setup = ''
ps = Parsing(spacy.load('ja_ginza'), setup)

while True:
    pos = 0
    neg = 0
    print('input text')
    x = input()
    text = ps.word_pars(x,worddic)

    if x == 'end':
        break