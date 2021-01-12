import MeCab
import re

c = MeCab.Tagger("-Ochasen")
w = MeCab.Tagger("-Owakati")

while True:
    result = []
    fast = 0
    end = 0
    x = input()
    show = w.parse(x)
    print(show)

    if x == 'end':
        break
    