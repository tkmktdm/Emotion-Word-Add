w = [['葵', 'NOUN', 0], ['ちゃん', 'NOUN', 0], ['ちゃん', 'NOUN', 0], ['ちゃん', 'NOUN', 1], ['ちゃん', 'NOUN', 1],['ちゃん', 'NOUN', 0], ['ちゃん', 'NOUN', 1], ['ちゃん', 'NOUN', -1]]
x = ['ちゃん', 'NOUN', 0]
n = []
count = 0
for i in w:
    '''print('i')
    print(i)
    print('x')
    print(x)'''

    if i in n[0]:
        print('i')
    else:
        n.append(i)
        print('add')
    print(n)
    '''if i[0] in x[0] and count > 0:
        print('in')
        
    else:
        n.append(i)
        count += 1'''
    #print(count)
print('n')
print(n)