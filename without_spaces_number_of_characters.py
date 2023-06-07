n=input()
x=n.split()
y=[]
for i in x:
    y.append(len(i))
print(sum(y))