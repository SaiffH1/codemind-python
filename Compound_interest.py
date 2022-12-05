def ci(p,r,t):
    res=p*(1+(r/100))**t
    return res
p,r,t=map(int,input().split())
res=ci(p,r,t)
print('%.2f'%res)