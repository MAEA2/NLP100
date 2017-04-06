#05. n-gram
#与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
def word_ngram(s,n):
    s=s.replace(",","")
    s=s.replace(".","")
    sw=s.split(" ")
    ngram=[]
    for i in range(len(sw)-n+1):
        chank=""
        for j in range(i,i+n):
            if(j==i+n-1):
                chank+=sw[j]
            else:
                chank+=sw[j]+" "
        ngram.append(chank)
    return ngram

def char_ngram(s,n):
    s=s.replace(",","")
    s=s.replace(".","")
    sc=list(s.replace(" ",""))
    ngram=[]
    for i in range(len(sc)-n+1):
        chank=""
        for j in range(i,i+n):
            chank+=sc[j]
        ngram.append(chank)
    return ngram
