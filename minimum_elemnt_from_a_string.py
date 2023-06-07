n = input()
s = n.split()
k = s[-1]
m = min(k).lower()
if m in k:
    print(m)
else:
    print(min(k))
    