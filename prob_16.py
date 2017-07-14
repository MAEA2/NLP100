#16
import sys
import codecs
args = sys.argv
f=codecs.open(args[1],encoding="utf-8")
lines=[]
line=f.readline()
l=1
N=int(args[2])
num=0
file_name=args[1].split(".")
while line:
    if l > N:
        num=num+1
        g=codecs.open(file_name[0]+"_%s.txt" % num,"w",encoding="utf-8")
        g.close()
        for l in lines:
            g=codecs.open(file_name[0]+"_%s.txt" % num,"a",encoding="utf-8")
            g.write(l)
            g.close()
        lines=[]
        l=1
    elif line==None:
        num=num+1
        g=codecs.open(file_name[0]+"_%s.txt" % num,"w",encoding="utf-8")
        g.close()
        for l in lines:
            g=codecs.open(file_name[0]+"_%s.txt" % num,"a",encoding="utf-8")
            g.write(l)
            g.close()
        lines=[]
        l=1
    else:
        lines.append(line)
        l=l+1
    line=f.readline()
f.close()
