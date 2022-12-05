def multiple(p,r,t):
    res=p*r*t//100
    return res
p,r,t=map(int,input().split())
res=multiple(p,r,t)
print(res)