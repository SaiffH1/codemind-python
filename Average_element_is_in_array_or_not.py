n=int(input())
s=list(map(int,input().split()))
a=sum(s)//len(s)
if a in s:
    print("True")
else:
    print("False")