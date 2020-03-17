n=int(input())
i=2
fi=0
f1=1
f2=0
while i!=n+1:
 fi=f1+f2
 f2=f1
 f1=fi
 i=i+1
print(fi)