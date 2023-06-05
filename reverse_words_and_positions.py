n=input()
s=n.split()
a=[]
for i in s:
    a.append(i[::-1])
print(*a[::-1])