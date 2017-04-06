#04. 元素記号
#"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
#という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
#取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
s=u"Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
s=s.replace(",","")
s=s.replace(".","")
slist=s.split(" ")
n=len(slist)
dic={}
one=[1,5,6,7,8,9,15,16,19]
for i in range(n):
    if i+1 in one:
        dic[slist[i][0:1]]=i+1
    else:
        dic[slist[i][0:2]]=i+1
print(dic)
