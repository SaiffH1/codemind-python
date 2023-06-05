n=int(input())
s=list(map(int,input().split()))
v=int(input())
a=[]
for i in s:
    if s.count(i)==v:
        a.append(i)
x=set(a)
if len(a)==0:
    print("-1")
else:
    print(*x)