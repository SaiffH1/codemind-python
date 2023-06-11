def multiple(p,t,r):
    res=p*t*r//100
    return res
p,t,r=map(int,input().split())
res=multiple(p,t,r)
print(res)