a=int(input())
eve=0
odd=0
while a:
    d=a%10
    if(d%2==0):
        eve+=1
    else:
        odd+=1
    a=a//10
if eve==0:
    print('Odd')
elif odd==0:
    print('Even')
else:
    print('Mixed')