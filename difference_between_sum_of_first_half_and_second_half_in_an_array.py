n = int(input())
lst = list(map(int,input().split()))
l1 = []
l2 = []
for i in range(len(lst)//2):
    l1.append(lst[i])
for j in lst:
    if j not in l1:
        l2.append(j)
        
print(sum(l2)-sum(l1))