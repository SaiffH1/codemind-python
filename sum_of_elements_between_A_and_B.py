n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in s:
    if i>=a and i<=b:
        c.append(i)
print(sum(c))