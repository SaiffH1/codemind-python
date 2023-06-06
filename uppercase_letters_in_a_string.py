n=input()
c=0
s='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in n:
    if i in s:
        c+=1
print(c)