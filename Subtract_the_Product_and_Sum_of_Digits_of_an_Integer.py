n=int(input())
sum=0
product=1
while n>0:
    d=n%10
    sum=sum+d
    product=product*d
    n=n//10
    v=product-sum
print(v)    