n=input()
s=n.split()
a=[]
for i in s:
    a.append(i)
print(*a[::-1])