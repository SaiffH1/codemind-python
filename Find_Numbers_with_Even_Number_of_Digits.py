n=int(input())
lst=list(map(str,input().split()))
c=0
for i in lst:
    if len(i)%2==0:
        c+=1
print(c)