#03. 円周率
#"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."という文を
#単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
s=u"Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
s=s.replace(",","")
s=s.replace(".","")
slist=s.split(" ")
l=[]
for i in slist:
    l.append(len(i))
print(l)
