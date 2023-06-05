n=int(input())
s=list(map(int,input().split()))
if len(s)%2==0:
    print(*s)
else:
    print(*s,'0')