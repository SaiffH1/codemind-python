n=int(input())
lst=list(map(int,input().split()))
l1=[]
l2=[]
f=0
for i in lst:
    if lst.count(i)==i:
        l1.append(i)
for j in l1:
    if j not in l2:
        l2.append(j)
if len(l2)==0:
    print("-1")
else:
    print('{:.2f}'.format(sum(l2)/len(l2)))
    