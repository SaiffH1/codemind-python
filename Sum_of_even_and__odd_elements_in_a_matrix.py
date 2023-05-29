r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
e=[]
o=[]
for i in range(r):
    for j in range(c):
        if mat[i][j]%2==0:
            e.append(mat[i][j])
        else:
            o.append(mat[i][j])
print(sum(e),sum(o))