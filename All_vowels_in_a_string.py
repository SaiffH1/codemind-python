n=input()
vo=["a","e","i","o","u"]
vow=["A","E","I","O","U"]
a=[]
b=[]
for i in n:
    if i in vo:
        a.append(i)
    elif i in vow:
        b.append(i)
if len(set(a))==5 or len(set(b))==5:
    print("True")
else:
    print("False")