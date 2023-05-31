n=int(input())
s=list(map(int,input().split()))
c=0
for i in s:
    if i==0 or i==1:
        c+=1
if c==len(s):
    print("True")
else:
    print("False")
    
        