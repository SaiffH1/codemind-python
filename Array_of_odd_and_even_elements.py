n=int(input())
s=list(map(int,input().split()))
a=[]
b=[]
for i in range(len(s)):
    if s[i]%2!=0:
        a.append(s[i])
    else:
        b.append(s[i])
print(*(a+b))
        