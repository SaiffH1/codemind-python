n=int(input())
a=list(map(int,input().split()))
for i in a:
    d=a.count(i)
    if d>(n//2):
        print(i)
        break