n=input()
s=n.split()
x=[]
for i in s:
    x.append(len(i))
print(*x)