n=int(input())
a=list(map(int,input().split()))
for i in range(len(a)//2):
    print(a[i],end=" ")
    print(a[len(a)//2+i],end=" ")