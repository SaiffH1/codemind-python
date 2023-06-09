n=int(input())
s=list(map(int,input().split()))
a=int(input())
x=max(s)
l1=[]
for i in s:
    if i+a<x:
        l1.append("False")
    else:
        l1.append("True")
print(*l1)