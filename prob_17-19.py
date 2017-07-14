#17
import sys
import codecs
import pandas as pd

args=sys.argv
f=codecs.open(args[1],"r","utf-8")
line=f.readline()
s=[]
while line:
    l=line.split("\t")
    if l[0] not in s:
        s.append(l[0])
    line=f.readline()
print(s)

#17 by pandas
df=pd.read_csv( args[1],header=None,delimiter='\t' )
unique=df[0].unique()
print(unique)

#18 by pandas
order=[]
print(df)
df=df.sort_values(by=2,ascending=False)
print(df)

#19
count=df[0].value_counts()
count=count.sort_values(ascending=False)
print(count)
