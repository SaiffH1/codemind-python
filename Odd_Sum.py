n = int(input())
lst=list(map(int,input().split()))
a=[]
for i in lst:
    if i%2!=0:
        a.append(i)
print(sum(a))