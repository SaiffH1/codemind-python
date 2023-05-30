n=int(input())
arr=list(map(int,input().split()))
p=int(input())
c=[]
for i in arr:
    if i<=p:
        c.append(i)
print(sum(c))

