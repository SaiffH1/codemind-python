n=int(input())
s=list(map(int,input().split()))
count=0
for i in range(1,len(s)-1):
    if s[i-1]%2==0 and s[i+1]%2==0:
        s[i]==0
        count+=1
print(count)