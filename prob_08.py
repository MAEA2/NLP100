#08. 暗号文
#与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

#英小文字ならば(219 - 文字コード)の文字に置換
#その他の文字はそのまま出力
#この関数を用い，英語のメッセージを暗号化・復号化せよ．
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
s="This is a 5000kg pen."

def encode(s):
    ss=list(s)
    sss=[]
    for i in ss:
        if i.islower():
            sss.append(chr(219-ord(i)))
        else:
            sss.append(i)
    s_code=""
    for i in sss:
        s_code+=i
    return s_code
def decode(s):
    ss=list(s)
    sss=[]
    for i in ss:
        if i.islower():
            sss.append(chr(219-ord(i)))
        else:
            sss.append(i)
    s_code=""
    for i in sss:
        s_code+=i
    return s_code

print(decode(encode(s)))
