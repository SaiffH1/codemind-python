n=input()
m=[]
for i in n:
    if i not in m:
        m.append(i)
if len(m)==len(n):
    print("True")
else:
    print("False")