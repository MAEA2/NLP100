#02. 「パトカー」＋「タクシー」＝「パタトクカシーー」
#「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
s1=u"パトカー"
s2=u"タクシー"
s3=""
for (x,y) in zip(s1,s2):
    s3+=x+y
print(s3)
