n=int(input())
s=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(s)//2):
    a.append(s[i])
for j in s:
    if j not in a:
        b.append(j)
print(*b[::-1],*a)
        