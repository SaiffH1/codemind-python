n=input()
s=[]
for i in n:
    s.append(i)
if len(set(s))==len(n):
    print("Unique Number")
else:
    print("Not Unique Number")