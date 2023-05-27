n=int(input())
lst=list(map(int,input().split()))
lst.append(lst[0])
lst.append(lst[1])
c=0
for i in range(1,len(lst)-1):
    if (lst[i-1]%2==0 and lst[i+1]%2!=0) or (lst[i-1]%2!=0 and lst[i+1]%2==0):
        c+=1
print(c)