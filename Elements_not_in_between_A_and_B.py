n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
c=[]
for i in range(0,len(s)):
    if s[i]<a or s[i]>b:
        c.append(s[i])
if len(c)==0:
    print("-1")
else:
    print(*c)