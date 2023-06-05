n=int(input())
s=list(map(int,input().split()))
a=[]
for i in s:
    if s.count(i)==i:
        a.append(i)
x=set(a)
print(len(x))