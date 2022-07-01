n,k=map(int,input().split())

s=0
count=0
temp=[0] * n
for i in range(n):
    temp[i]=int(input())
    if temp[i]<=k:
        s=i #시작 인덱스

while k:
    count=count+(k//temp[s])
    k=k%temp[s]
    s=s-1

print(count)