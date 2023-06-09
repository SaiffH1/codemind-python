a,b=map(int,input().split())
x=[]
y=[]
z=[]
if a>b:
    for i in range(1,a):
        if a%i==0:
            x.append(i)
        if b%i==0:
            y.append(i)
        for i in x:
            if i in y:
                z.append(i)
    print(max(z))
else:
    for i in range(1,b):
        if a%i==0:
            x.append(i)
        if b%i==0:
            y.append(i)
        for i in x:
            if i in y:
                z.append(i)
    print(max(z))