n=int(input())
a=list(map(int,input().split()))
count=0
print(max(set(a),key=a.count))