#10. 行数のカウント
#行数をカウントせよ．確認にはwcコマンドを用いよ．

#11. タブをスペースに置換
#タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

#12. 1列目をcol1.txtに，2列目をcol2.txtに保存
#各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

#13. col1.txtとcol2.txtをマージ
#12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．

#10
import io,sys
import subprocess
import codecs
import pandas as pd

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
print(len(codecs.open("hightemp.txt",encoding="utf-8").readlines()))
subprocess.call(["wc", "-l", "hightemp.txt"])

#11
f=open("hightemp.txt",encoding="utf-8")
line=f.readlines()
g=codecs.open("hightemp1.txt","w","utf-8")
g.close()
for l in line:
        g=codecs.open("hightemp1.txt","a","utf-8")
        g.write(l.replace("\t"," "))
        g.close()

#12
data=pd.read_table("hightemp.txt",sep="\t",header=None)
g=codecs.open("col1.txt","w","utf-8")
g.close()
g=codecs.open("col2.txt","w","utf-8")
g.close()
for i in data[0]:
    g=codecs.open("col1.txt","a","utf-8")
    g.write("%s\n" % i)
    g.close()
for i in data[1]:
    g=codecs.open("col2.txt","a","utf-8")
    g.write("%s\n" % i)
    g.close()

#13
f1=open("col1.txt",encoding="utf-8")
row1=f1.readlines()
f2=open("col2.txt",encoding="utf-8")
row2=f2.readlines()
for i in range(len(row1)):
    row1[i]=row1[i].replace("\n","")
for i in range(len(row2)):
    row2[i]=row2[i].replace("\n","")
row=[]
for (x,y) in zip(row1,row2):
    row.append(x+"\t"+y)
g=codecs.open("col.txt","w","utf-8")
g.close()
for r in row:
    print(r)
    g=codecs.open("col.txt","a","utf-8")
    g.write("%s\n" % r)
    g.close()
