#06. 集合
#"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
#XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
import io,sys
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

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
x="paraparaparadise"
y="paragraph"
X=set(char_ngram(x,2))
Y=set(char_ngram(y,2))
X_or_Y=X|Y
X_and_Y=X&Y
X_sub_Y=X-Y
if "se" in X:
    print("se is in X")
if "se" in Y:
    print("se is in Y")
