n=int(input())
rev=0
d=n**2
while n:
    r=n%10
    rev=rev*10+r
    n=n//10
k=rev**2
rev2=0
while k:
    r1=k%10
    rev2=rev2*10+r1
    k=k//10
if rev2==d:
    print("True")
else:
    print("False")