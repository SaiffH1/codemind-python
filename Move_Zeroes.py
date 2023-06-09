n=int(input())
s=list(map(int,input().split()))
l1=[]
c=0
for i in s:
    if i==0:
        c+=1
    else:
        l1.append(i)
for i in range(c):
    l1.append("0")
print(*l1)
