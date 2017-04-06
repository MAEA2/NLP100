import io,sys
import codecs
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
argvs = sys.argv

#14
def head_out():
    N=int(argvs[1])
    file_name=argvs[2]
    f=open(file_name,encoding="utf-8")
    line=f.readlines()
    out=line[0:N]
    for l in out:
        print(l)

#15
def tail_out():
    N=int(argvs[1])
    file_name=argvs[2]
    f=open(file_name,encoding="utf-8")
    line=f.readlines()
    out=line[len(line)-N:len(line)]
    for l in out:
        print(l)

#16
f=codecs.open("hightemp.txt",encoding="utf-8")
lines=[]
line=f.readline()
l=1
N=5
num=0
while line:
    line=f.readline()
    if l>N:
        num=num+1
        g=codecs.open("hightemp0%s.txt" % num,"w",encoding="utf-8")
        g.close()
        for l in lines:
            g=codecs.open("hightemp0%s.txt" % num,"a",encoding="utf-8")
            g.write(l)
            g.close()
        lines=[]
        l=1
    elif line==None:
        num=num+1
        g=codecs.open("hightemp0%s.txt" % num,"w",encoding="utf-8")
        g.close()
        for l in lines:
            g=codecs.open("hightemp0%s.txt" % num,"a",encoding="utf-8")
            g.write(l)
            g.close()
        lines=[]
        l=1
    else:
        lines.append(line)
        l=l+1
f.close()
