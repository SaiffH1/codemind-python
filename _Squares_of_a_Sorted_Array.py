n=int(input())
s=list(map(int,input().split()))
l1=[]
for i in s:
    l1.append(abs(i*i))
print(*sorted(l1))