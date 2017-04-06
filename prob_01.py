#01. 「パタトクカシーー」
#「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
s=u"パタトクカシーー"
s1=""
for i in [1,3,5,7]:
    s1+=s[i-1]
print(s1)
