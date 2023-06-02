def prime(n):
    c=0
    for i in range(1,n+1):
        if n%i==0:
            c+=1
    if c==2:
        return True
    else:
        return False
a=int(input())
b=int(input())
l=[]
for i in range(a,b):
    x = prime(i)
    if prime(i)==True:
        print(i)