n=input()
vowels=["a","e","i","o","u"]
a=[]
b=[]
lwr=n.lower()
for i in lwr:
    if i in 'aeiou':
        a.append(i)
for i in vowels:
    if i not in a:
        b.append(i)
if len(b)==0:
    print("0")
else:
    print(*b)