n=int(input())
s=list(map(int,input().split()))
a=sum(s)//len(s)
c=0
for i in s:
    if i<=a:
        c+=1
print(c)
        
    