n=int(input())
lst=list(map(int,input().split()))
a=[]
for i in lst:
    if lst.count(i)==i:
        a.append(i)
if len(a)==0:
    print("-1")
else:
    x=set(a)
    print(min(x),max(x))