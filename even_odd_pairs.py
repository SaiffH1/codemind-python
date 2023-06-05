n=int(input())
s=list(map(int,input().split()))
e=[]
o=[]
r=[]
for i in s:
    if i%2==0:
        e.append(i)
    else:
        o.append(i)
if len(o)>=len(e):
    for i in range(len(e)):
        r.append(e[i])
        r.append(o[i])
    r=r+o[len(e):len(o)]
if len(o)<len(e):
    for i in range(len(o)):
        r.append(e[i])
        r.append(o[i])
    r=r+e[len(o):len(e)]
if len(s)%2==0:
    print(*r)
else:
    r=r+[0]
    print(*r)