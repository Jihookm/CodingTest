n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)
ssum=0
for i in range(n):
    ssum=ssum+(a[i]*b[i])

print(ssum)