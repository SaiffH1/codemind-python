n=int(input())
arr=list(map(int,input().split()))
a=int(input())
for i in arr:
    if i==a:
        print("True")
        break
else:
    print("False")