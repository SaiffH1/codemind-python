for i in range(int(input())):
    n,b=map(int,input().split())
    a=list(map(int,input().split()))
    sum=0
    d=[]
    f=0
    for i in range(n):
        for j in range(i,n):
            sum=0
            for k in range(i,j+1):
                sum=sum+a[k]
            if sum==b:
                f=1
                d.append(i+1)
                d.append(j+1)
    if f==1:
        print(d[0],d[1])
    if f==0:
        print("-1")