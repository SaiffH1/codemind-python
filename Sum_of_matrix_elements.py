n=int(input())
m=int(input())
s=0
for i in range(n):
    b=list(map(int,input().split()))
    s=s+sum(b)
print(s)    