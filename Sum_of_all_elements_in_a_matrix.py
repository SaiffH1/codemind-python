r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
su=0
for i in range(r):
    for j in range(c):
        su+=mat[i][j]
print(su)