n=int(input())
s=list(map(int,input().split()))
a,b=map(int,input().split())
l1 = []
l2 = []
for i in s:
    if i>=a and i<=b:
        l1.append(i)
for j in s:
    if j not in l1:
        l2.append(j)
if len(l2) == 0:
    print("-1")
else:
    print(min(l2))
        