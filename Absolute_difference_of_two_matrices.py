n=int(input())
mat1=[]
mat2=[]
for i in range(n):
    x=list(map(int,input().split()))
    mat1.append(x)
for j in range(n):
    y=list(map(int,input().split()))
    mat2.append(y)
mat3=[]
for i in range(n):
    a=[]
    for j in range(n):
        a.append(abs(mat1[i][j]-mat2[i][j]))
    mat3.append(a)
for i in mat3:
    print(*i)

        