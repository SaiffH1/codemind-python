n=int(input())
a=list(map(int,input().split()))
f=0
for i in a:
    d=a.count(i)
    if d==1:
        f=1
        print(i,end=" ")
if f==0:
    print("-1")