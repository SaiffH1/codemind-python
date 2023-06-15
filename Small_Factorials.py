def fact(x):
    c=1
    for i in range(1,x+1):
        c=c*i
    return c
n=int(input())
for i in range(n):
    x=int(input())
    print(fact(x))
