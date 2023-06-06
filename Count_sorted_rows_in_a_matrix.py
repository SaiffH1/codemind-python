r,c=map(int,input().split())
s=0
mat=[list(map(int,input().split())) for i in range(r)]
for i in range(r):
    a=[]
    for j in range(c):
        a.append(mat[i][j])
    b=sorted(a)
    if b==a:
        s+=1
    elif b[::-1]==a:
        s+=1
print(s)