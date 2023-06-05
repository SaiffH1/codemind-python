n=int(input())
lst=list(map(str,input().split()))
a=[]
for i in lst:
    if "-" in lst:
        a.append(len(i)-1)
    else:
        a.append(len(i))
k=max(a)
print(a.count(k))