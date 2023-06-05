n=int(input())
lst=list(map(int,input().split()))
a=[]
b=[]
c=[]
for i in lst:
    a.append(abs(i))
for j in a:
    b.append(str(j))
for k in b:
    c.append(len(k))
print(*c)