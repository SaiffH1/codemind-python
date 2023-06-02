n=int(input())
s=list(map(int,input().split()))
a=[]
for i in s:
    if i not in a:
        a.append(i)
print(*a)