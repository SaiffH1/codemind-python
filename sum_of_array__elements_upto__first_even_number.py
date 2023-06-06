n=int(input())
s=list(map(int,input().split()))
a=[]
for i in s:
    if i%2!=0:
        a.append(i)
    else:
        break
print(sum(a))