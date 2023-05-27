n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
m=[]
for i in range(n):
    if s[i]<a or s[i]>b:
        m.append(s[i])
if len(m)==0:
    print('-1')
else:
    print(max(m))
