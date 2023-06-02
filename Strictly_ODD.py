n=int(input())
s=list(map(int,input().split()))
a=0
for i in s:
    if i%2!=0 and s.index(i)%2==0:
        print("False")
        a=1
        break
if a== 0:
    print("True")