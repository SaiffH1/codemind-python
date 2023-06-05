n=int(input())
lst=list(map(str,input().split()))
a=[]
for i in lst:
    if "-" in i:
        a.append(len(i)-1)
    else:
        a.append(len(i))
k=min(a)
print(a.count(k))