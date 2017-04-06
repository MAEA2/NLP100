#09. Typoglycemia
#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
#それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
#ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
#（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）
#を与え，その実行結果を確認せよ．
import random
def rand_change(s):
    sss=s.split(" ")
    sentence=[]
    for i in sss:
        if "," in i:
            ii.insert()
        if len(i)>4:
            ii=list(i[1:len(i)-1])
            random.shuffle(ii)
            ii.insert(0,i[0:1])
            ii.append(i[len(i)-1:len(i)])
            sentence.append("".join(ii))
        else:
            sentence.append(i)
    s_rand=" ".join(sentence)
    return s_rand
s="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(rand_change(s))
