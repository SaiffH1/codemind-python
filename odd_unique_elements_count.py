n=int(input())
s=list(map(int,input().split()))
x=set(s)
a=[]
for i in x:
    if i%2!=0:
        a.append(i)
print(len(a))