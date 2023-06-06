def vowels(i):
    c=0
    for j in i:
        if j in"aeiou":
            c+=1
    return c
n=input()
s=n.split()
for i in s:
    x=vowels(i)
    print(x,end=' ')