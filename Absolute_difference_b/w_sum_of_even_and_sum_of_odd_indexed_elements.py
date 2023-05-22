n = int(input())
l= list(map(int,input().split()))
se= 0
so = 0
for i in range(n):
    if i%2!=0:
        so+=l[i]
    else:
        se+=l[i]
if se>so:
    print(se-so)
else:
    print(so-se)