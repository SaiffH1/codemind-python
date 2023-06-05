n=int(input())
s=list(map(int,input().split()))
a=[]
for i in s:
    if i not in a:
        a.append(i)
for j in a:
    print(j,s.count(j),end=' ')