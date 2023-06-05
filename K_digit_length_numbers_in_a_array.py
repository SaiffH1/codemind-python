n,m=map(int,input().split())
lst=list(map(int,input().split()))
a=[]
b=[]
c=0
for i in lst:
    a.append(abs(i))
for j in a:
    b.append(str(j))
for k in b:
    if len(k)==m:
        c+=1
print(c)