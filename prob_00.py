#00. 文字列の逆順
#文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．

s="stressed"
#0   1   2   3   4   5   6   7   8
#| s | t | r | e | s | s | e | d |
#-9 -8  -7  -6  -5  -4  -3  -2  -1
#x[arg1:arg2:arg3]
#x[::-1]で逆順になる。
rev_s=s[::-1]
print(rev_s)
