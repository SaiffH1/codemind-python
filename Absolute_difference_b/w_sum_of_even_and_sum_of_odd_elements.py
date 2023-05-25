N = int(input())
arr = list(map(int,input().split()))
even =[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
p=sum(even)
q=sum(odd)
print(abs(p-q))